import sqlite3
import string
import random
import datetime

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
var = lower + upper + num

def insertUser(username, email, password):
    key = f"{datetime.datetime.now().strftime('%d%m%Y%H%M%S')}{''.join(random.sample(var, 20))}"
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("insert into userdb (api_key, username, email, password) values (?,?,?,?)",(key, username, email, password))
    con.commit()
    con.close()

def retrieveUser():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("select * from userdb")
    users = cur.fetchall()
    con.close()
    return users