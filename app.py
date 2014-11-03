##atm logout python stuff should be good, and we have something or other for login
from pymongo import Connection
from flask import Flask,flash, render_template, request, redirect, session
##Maria, you need to learn how to use redirect

conn = Connection()
db = conn["sunmar"]

app = Flask(__name__)


##Checks if you entered a valid username and password
def legitLogin(user,pword):
   if (len(user) < 5 or len(user) > 15
       or len(pword) < 7 or len(pword) > 20 ):
          return True ##the t/f values are a bit weird here
   else:
      return False

@app.route('/',methods=["POST","GET"])
def home():
    pass

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
    error = None
    if "username" not in session:
        if request.method == "POST":
            user = request.form['user']
            pword = request.form['pword']
            error =  legitLogin(user,pword)
            if error == True: 
                flash("Invalid username or password")
                return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop('username',None)
    ##Do you need to pop the password too??
    return render_template("logout.html")

##stuck on how to add to db
@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
      user = request.form["user"]
      pword = request.form["pword"]
    if (legitLogin(user,pword)):
        return render_template("register.html")

@app.route("/shhh")
def page1():
    return render_template("secret1.html")

@app.route("/shhh2")
def page2():
    return render_template("secret2.html")


if __name__ == "__main__":
    app.debug = True
    app.secret_key = "MTYIXatgAP2y6fIvq8MrAN8RKgHg2B8p"
    app.run()
    
        
