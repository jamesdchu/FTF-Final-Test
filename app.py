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

# @app.route('/')
# @app.route('/index', methods= ["GET", "POST"])
# def index():
#     return render_template('index.html')

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
            collection.insert({"user_name":user_name,"user_email":user_email, "user_password": user_password,"user_password_repeat":user_password_repeat, "user_interest": user_interest, "user_education": user_education, "user_headline": user_headline, })
            # return redirect(url_for('homePage.html'))
            return render_template('homePage.html')
        return 'That email already exists! Try logging in.'
    return render_template('signUp.html')

@app.route('/signIn', methods= ["GET", "POST"])
def signIn():
    if request.method=="GET":
        return render_template('signIn.html')
    else:
        user_email = request.form["user_email"] 
        user_password = request.form["password"]
        ##Connecting to database
        collection = mongo.db.user_info      
        # checks to see if the info user provided is in the data base 
        login_user = collection.find_one({'user_email' : user_email})
        login_userPW = collection.find_one({'user_password' : user_password})
        #Checking to see if email in database
        if login_user is None: 
            return ("It seems like you do not have an account, please type your email correctly or sign up!")
        elif user_password != login_userPW or login_userPW is None:
            return "Incorrect password, please try again!"
        elif (user_email == login_user) and (user_password == login_userPW): 
            return render_template('homePage.html')
        return 'Invalid combination!'

@app.route('/add')

def add():
    # connect to the database
    collection = mongo.db.user_info
    # user_info = collection.find({})
    collection.insert({'user_name': "jameschu", "user_email":"james2@gmail.com", "user_password": "password"})
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


@app.route('/art_Meme')
def art_Meme():
    return render_template('art_Meme.html')

