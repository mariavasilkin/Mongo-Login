import random, re

from flask import Flask, render_template, request

app = Flask(__name__)
app.session_interface = MongoSessionInterface(db=***put name here***)#not 100% on this

@app.route('/',methods=["POST","GET"])
def home():

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    returnrender_template("login.html")

@app.route("/logout")
def logout():
    return render_template("logout.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/shhh")
def page1():
    return render_template("secret1.html")

@app.route("/shhh2")
def page2():
    return render_template("secret2.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
 
        
