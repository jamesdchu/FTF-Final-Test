# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import inDataBase
from flask_pymongo import PyMongo
import model

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'users'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:8pcd0XmbvbLDNpCf@cluster0.6gvi8.mongodb.net/users?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
# @app.route('/index')
# def index():
#     return render_template('index.html', events = events)

@app.route('/homePage', methods= ["GET", "POST"])
def homePage():
    return render_template('homePage.html')

@app.route('/signUp', methods= ["GET", "POST"])
def signUp():
    # add mongo db stuff so that it adds user information when they sign up
    # users>> user, user_password, userbirthday etc
    if request.method == "POST":
        print(request.form)
        user_email = request.form["user_email"]
        user_password = request.form["password"]
    return render_template('signUp.html', )
# CONNECT TO DB, ADD DATA

@app.route('/signIn', methods= ["GET", "POST"])
def signIn():
    if request.method == "GET":
        return render_template('signIn.html')
    else:
        user_email = request.form["user_email"] 
        user_password = request.form["password"]
        ##Connecting to database
        collection = mongo.db.user_info        
        confirm_info = model.inDataBase(user_email, user_password, collection) #render_template('signIn.html', user_email = user_email, user_password=user_password)

        # checks to see if the info user provided is in the data base, returns a bollean
        if(confirm_Info): 
            return "Success!"
        else: 
            return"FAiL!"
        #     # need to code for in database

        # return render_template('signIn.html')# user_email = user_email, user_password=user_password)
        # else:
        # return ("Please re-enter your infomation")
        
    # else:
    #     return "Error"
# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    collection = mongo.db.user_info
    collection.insert({"user_email":"james@gmail.com", "user_password": "password"})
    # insert new data
    # return a message to the user
    return "Done!"


# @app.route('/signUp', methods = ["GET", "POST"])
# def signUp():

@app.route('/discussionPage')#, methods= ["GET", "POST"])
def discussionPage():
    return render_template('discussionPage.html')

@app.route('/resourcesPage', methods= ["GET", "POST"])
def resourcesPage():
    return render_template('resourcesPage.html')

@app.route('/profilePage', methods= ["GET", "POST"])
def profilePage():
    return render_template('profilePage.html')

