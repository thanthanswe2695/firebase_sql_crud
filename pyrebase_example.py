import pyrebase
from getpass import getpass


firebaseConfig = {
    "apiKey": "AIzaSyCA50Nf8vhijKEaNaTipHtpO6Nq6lSYLEM",
    "authDomain": "mytest-3ad72.firebaseapp.com",
    "databaseURL": "https://mytest-3ad72.firebaseio.com",
    "projectId": "mytest-3ad72",
    "storageBucket": "mytest-3ad72.appspot.com",
    "messagingSenderId": "105708216028",
    "appId": "1:105708216028:web:703b2c6fbe4795c2ffde19",
    "measurementId": "G-NY5XDSE4Z4"
  }


firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

email = input("Please Enter Your Email :  \n")
password = input("Please Enter Your Password : \n")

user = auth.create_user_with_email_and_password(email,password)
print("Success ....")