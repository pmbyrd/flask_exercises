from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    "Shows the welcome page"
    return "Welcome"

@app.route('/welcome/home')
def welcome_home():
    "Shows welcome home page"
    return "Welcome home"

@app.route('/welcome/back')
def welcome_back():
    "Shows welcome back page"
    return "Welcome back"