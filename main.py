from flask import Flask
from flask import render_template
from flask import request
import Scraper
import models as SQLHandler

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        res = Scraper.scrapCircular()
        return render_template("index.html", res = res)

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
        SQLHandler.insertUser(username, email, password)
        userStat = True

        return render_template("register.html", userStat = userStat)

@app.route("/api", methods=['GET', 'POST'])
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