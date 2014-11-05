from pymongo import Connection

conn = Connection()

db = conn['sunmaria']

print db.collection_names()

##Checks if user already exists
def existingUser(user):
    if ((db.users.find_one({'user':user})) == None):
        return True
    else:
        return False

##Adds new user to db
def registerUser(name,pwrd):
    if ((db.users.find_one({'user':user}))==None) and pwrd!=None:
        db.users.insert({user:'user',pwrd:'password'})
        return True
    else:
        return False
print db.collection_names()

##Checks if you entered a valid username and password
def legitLogin(user,pword):
   if ((len(user) < 5) or (len(user) > 15)
       or (len(pword) < 7) or (len(pword) > 20)):
          return False
   else:
      return True
