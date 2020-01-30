
from firebase import firebase

firebase=firebase.FirebaseApplication("https://pythondbtest-f00a7.firebaseio.com/",None)



result=firebase.get("/pythondbtest-f00a7/Customer",'')
print(result)