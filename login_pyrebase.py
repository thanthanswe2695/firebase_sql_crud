import pyrebase
from getpass import getpass


firebaseConfig = {
    "apiKey": "AIzaSyAEDLVohsgCfHc6EKFTCoqbdc2z6m9Of38",
    "authDomain": "mytest-95384.firebaseapp.com",
    "databaseURL": "https://mytest-95384.firebaseio.com",
    "projectId": "mytest-95384",
    "storageBucket": "mytest-95384.appspot.com",
    "messagingSenderId": "787114967067",
    "appId": "1:787114967067:web:279ffdc9c6a1aa5cc6b8be",
    "measurementId": "G-0GRGET477L"
  }


firebase = pyrebase.initialize_app(firebaseConfig);


auth = firebase.auth()

email = input("Please Enter Your Email :  \n")
password = getpass("Please Enter Your Password : \n")

# user = auth.create_user_with_email_and_password(email,password)

login = auth.sign_in_with_email_and_password(email,password)

# auth.send_email_verification(login['idToken'])

auth.send_password_reset_email(email)

print("Success ....")

