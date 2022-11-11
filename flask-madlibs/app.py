from flask import Flask, request, render_template
from random import choice, sample
from stories import Story, story

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"

debug = DebugToolbarExtension(app)

# words = ["place", "noun", "verb", "adjective", "plural_noun"]
# text = """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""

@app.route("/")
def index():
    "Show home the page"
    return render_template("base.html")

@app.route("/stories")
def show_story():
    "Shows new instance of story with the text filled in py user inputs"
    #the story is expecting a dict, html form will come back as a key/val pair
    text = request.args
    new_story = story.generate(text)
    return render_template("stories.html", story=new_story)
