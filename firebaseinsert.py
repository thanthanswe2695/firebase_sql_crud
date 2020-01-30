from firebase import firebase

firebase=firebase.FirebaseApplication("https://pythondbtest-f00a7.firebaseio.com/",None)
data = {
	'Name':'San Thidar',
	'Email':'thannthannswe124509@gmail.com',
	'Phone':97958192131


}

result=firebase.post("/pythondbtest-f00a7/Customer",data)
print(result)