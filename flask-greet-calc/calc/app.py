# Put your app in here.
from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)

#do not hardcode the variables
@app.route('/add')
def get_add():
    "Shows the sum of a and b to the page"
    #flask turns every thing to a string, get the request and perform the opperation
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = str(add(a,b))
    return f"Your total is: {total}"

@app.route('/sub')
def get_sub():
    "Shows the difference of a and b to the page"
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = str(sub(a,b))
    return f"Your total is: {total}"

@app.route('/mult')
def get_mult():
    "Shows the product of a and b to the page"
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = str(mult(a,b))
    return f"Your total is: {total}"

@app.route('/div')
def get_div():
    "Shows the remainder of a and b to the page"
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = str(div(a,b))
    return f"Your total is: {total}"