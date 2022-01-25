import sqlite3

def insertTempDetails(sessionID, username, email, password, tempOTP):
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("insert into registrationdb (sessionID, username, email, password, tempOTP) values (?,?,?,?,?)", (sessionID, username, email, password, tempOTP))
    con.commit()
    con.close()

def retrieveTempDetails():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("select * from registrationdb")
    details = cur.fetchall()
    con.close()
    return details
    
def updateTempDetails(tempOTP,sessionID,username):
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("update registrationdb set tempOTP = (?), sessionID = (?) where username = (?)", (tempOTP, sessionID,username))
    con.commit()
    con.close()

def deleteTempDetails(username):
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("delete from registrationdb where username = (?)",(username,))
    con.commit()
    con.close()