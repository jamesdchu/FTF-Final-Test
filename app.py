# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import inDataBase
# from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"}
    ]

# name of database
# app.config['MONGO_DBNAME'] = 'database-name'

# URI of database
# app.config['MONGO_URI'] = 'mongo-uri'

# mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html', events = events)

@app.route('/signUp', methods= ["GET", "POST"])
def signUp():
    return render_template('signUp.html', )
# CONNECT TO DB, ADD DATA

@app.route('/signIn', methods= ["GET", "POST"])
def signIn():
    if request.method == "POST":
        print(request.form)
        user_name = request.form["username"]
        user_password = request.form["password"]
        confirm_info = inDataBase(user_name, user_password)
        # checks to see if the info user provided is in the data base, returns a bollean
        if(confirm_Info): 
            # need to code for in database
            return render_template('home.html', user_name = user_name, user_password=user_password)
        else:
            return ("Please re-enter your infomation")
    else:
        return "Error"
# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database

    # insert new data

    # return a message to the user
    return ""
