#import necessary methods and set up configs
from flask import Flask, request, render_template, redirect, flash, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from surveys import satisfaction_survey

app = Flask(__name__)

app.config["SECRET_KEY"] = "not-so-secret-key"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

#intialize a list to store the answers
responses = []
questions = 

@app.route("/")
def show_survey():
    "Shows the survery with instructions"
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template("base.html", title=title, instructions=instructions)

@app.route("/questions/0")
def show_questions():
    "Shows the survey questionaire and the current question"

    question = satisfaction_survey.questions
    # choices = satisfaction_survey.choices
    return render_template("questions.html", questions=question)

@app.route('/answers')
def get_answers():
    """Logs the users answers"""
    responses.append(request.args)
    # raise
    return redirect("/questions")

#get the user input

#redirect to the next page

#flash message if not in order

#How to make it automatically preview the next question without hardcoding
#the questions are in a list so they can be accessed by its index
