from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
import registrationModel
import mailOTP
import Scraper
import models as SQLHandler
import SessionID

app = Flask(__name__)
sessionID = SessionID.createSessionID()

@app.route("/", methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template("index.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = SQLHandler.retrieveUser()
        loginStat = "First Run"
        for i in range(len(users)):
            if users[i][1] == username and users[i][3] == password:
                loginStat = True
                key = users[i][0]
                break
            else:
                loginStat = False
                key = "public"
                continue

        return  render_template("login.html", loginStat = loginStat, key = key)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        otp, res = mailOTP.createSendOTP(username, email)
        details = registrationModel.retrieveTempDetails()
        alreadyExist= False
        for i in range(len(details)):
            if username  == details[i][1]:
                alreadyExist = True
                break
            else:
                alreadyExist = False
                continue
        if alreadyExist:
            registrationModel.updateTempDetails(otp, sessionID,username)
        else:
            registrationModel.insertTempDetails(sessionID, username, email, password, otp)
        return render_template("verification.html", res=res, username=username, email=email, otp=otp)

@app.route("/verification", methods=['GET','POST'])
def verification(): 
    if request.method == 'GET':
        return render_template("verification.html")
    elif request.method == 'POST':
        userOTP = request.form['otp']
        tempDetail = registrationModel.retrieveTempDetails()
        for i in range(len(tempDetail)):
            if sessionID == tempDetail[i][0]:
                usernameTemp = tempDetail[i][1]
                emailTemp = tempDetail[i][2]
                passwordTemp = tempDetail[i][3]
                otpTemp = tempDetail[i][4]
                break
            else:
                continue

        if userOTP == otpTemp:
            SQLHandler.insertUser(usernameTemp, emailTemp, passwordTemp)
            registrationModel.deleteTempDetails(usernameTemp)
            return render_template("verified.html")
        else:
            regis = False
            return redirect(url_for("register"))

@app.route("/api", methods=['GET'])
def scrap():
    key = request.args.get('key')
    if request.method == 'GET':
        users = SQLHandler.retrieveUser()
        for i in range(len(users)):
            if users[i][0] == key:
                res = Scraper.scrapCircular()
                break
            else:
                res = "API Key is not valid"
                continue

        return render_template("scrap.html",res = res)

if __name__ == "__main__":
    app.run(debug=True)