# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, session, url_for
# from bson.objectid import ObjectId
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

@app.route('/welcomePage', methods= ["GET", "POST"])
def welcomePage():
    return render_template('welcomePage.html')

@app.route('/homePage', methods= ["GET", "POST"])
def homePage():
    return render_template('homePage.html')

@app.route('/signUp', methods= ["GET", "POST"])
def signUp():
    # add mongo db stuff so that it adds user information when they sign up
    # users>> user, user_password, userbirthday etc
    if request.method == "GET":
        return render_template('signUp.html')
    else:
        user_name = request.form["user_name"]
        user_interest = request.form["user_interest"]
        user_education = request.form["user_education"]
        user_headline = request.form["user_headline"]
        user_email = request.form["user_email"]
        user_password = request.form["psw"]
        user_password_repeat = request.form["psw-repeat"]
        ##Checking if the email is already registered and connecting to database
        collection = mongo.db.user_info
        existing_user = collection.find_one({'user_email' : user_email})
        if existing_user is None: 
            #Checking that user entered same password
            if not (user_password == user_password_repeat): 
                return ("You entered different passwords, please try again!")
            #Adding new user to database
            collection.insert({"user_email":user_email, "user_password": user_password, "user_interest": user_interest, "user_education": user_education, "user_headline": user_headline, "user_password_repeat":user_password_repeat})
            return redirect(url_for('homePage'))
        return 'That email already exists! Try logging in.'
    return render_template('signup.html')

@app.route('/signIn', methods= ["POST"])
def signIn():

        user_email = request.form["user_email"] 
        user_password = request.form["password"]
        ##Connecting to database
        collection = mongo.db.user_info      
        # checks to see if the info user provided is in the data base 
        login_user = users.find_one({'user_email' : user_email}) 
        if login_user: 
            if user_password == login_user['password']:
                return "Logged in!"
        return 'Invalid combination!'

        
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
    collection.insert({"user_email":"james2@gmail.com", "user_password": "password"})
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

