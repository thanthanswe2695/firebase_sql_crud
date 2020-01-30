from firebase import firebase


firebase=firebase.FirebaseApplication("https://pythondbtest-f00a7.firebaseio.com/",None)

firebase.delete("/pythondbtest-f00a7/Customer/",'-LzL5Gv2wRnWg2TVjAZh')
print("Record deleted")
