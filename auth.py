import pyrebase 

config = {
    'apiKey' : "AIzaSyCb4i2IwnW4-Bh3QQA0O5OOiRg5I4oyv4o",
    'authDomain' : "aktu-auth.firebaseapp.com",
    'projectId' : "aktu-auth",
    'storageBucket' : "aktu-auth.appspot.com",
    'messagingSenderId' : "876112490224",
    'appId' : "1:876112490224:web:21be6c4fe345070a195c35",
    'measurementId' : "G-KBKBC66YVP",
    'databaseURL' : ""
}

firebase = pyrebase.initialize_app(config)
print("done")
