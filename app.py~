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
          return False
   else:
      return True
##This one isn't super neat and can use some work
def inDatabse(username):
   numCursors = db.sunmar.find({user:username})
   if (numCursors > 0):
      return True
   else:
      return False
@app.route('/',methods=["POST","GET"])
def home():
    return render_template("about.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
   if "user" not in session:
        if request.method == "GET":
           return render_template("login.html")
        else:
            user = request.form['user']
            pwrd = request.form['pwrd']
            if legitLogin(user,pwrd) == False: ##if there is an error
                flask("Invalid username or password")
                return render_template("login.html")
            else:
               session["user"]=user
               ##if they hit login from another page, it should rediect them back to that page somehow
               return redirect("/about")
   ##if they're already logged in
   else:
      return redirect("/about") ##we can change what it redirects to


@app.route("/logout")
def logout():
    session.pop('username',None)
    ##Do you need to pop the password too??
    return render_template("logout.html")

##stuck on how to add to db
@app.route("/register", methods=['POST', 'GET'])
def register():
   if "user" in session:
      flash("You're already logged in! If you want to register another account, logout first")
   else:
      if request.method == "GET":
         return render_template("register.html")
      else:
         user = request.form["user"]
         pword = request.form["pword"]
         if (not(legitLogin(user,pword))):
            flash("Invalid username or password")
            redirect("/register")   
         elif (inDatabase(user)):
            flash("That username is already taken, try another one")
            redirect("/register")
         else:
            session["user"] = user


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
    
        
