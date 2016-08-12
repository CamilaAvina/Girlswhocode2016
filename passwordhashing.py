from hashlib import *


sha256('MYSTRING'.encode('utf-8')).hexdigest()
users = {}
status = ""

def displayMenu():
    status =input("Are you a registered user? y/n? Press q to quit: ")  
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()

def newUser():
    createLogin = raw_input("Create login name: ")

    if createLogin in users: # check if login name exists
        print ("\nLogin name already exist!\n")
    else:
        createPassw = raw_input("Create password: ")
        users[createLogin] = createPassw # add login and password
        print("\nUser created!\n")     

def oldUser():
    login = raw_input("Enter login name: ")
    passw = raw_input("Enter password: ")

    # check if user exists and login matches password
    if login in users and users[login] == passw: 
        print ("\nLogin successful!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")

while status != "q":            
    displayMenu()

 
# The above will give you a hash of MYSTRING


	#Python can be interactive by getting information from the user!
	#Use “input” to get information from the user and save it to a variable:

#x = input("What is your name?")
