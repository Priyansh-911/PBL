from flask import Flask, render_template, session, request, redirect
import pyrebase


app = Flask(__name__)
config = {
    'apiKey': "AIzaSyCQ_rHiRe5jylQi1Yv3XhaKpgG7GrDGDOg",
    'authDomain': "aktu-auth-424a7.firebaseapp.com",
    'projectId': "aktu-auth-424a7",
    'storageBucket': "aktu-auth-424a7.appspot.com",
    'messagingSenderId': "905549747775",
    'appId': "1:905549747775:web:1cd323bca4e3ecb4024a8a",
    'measurementId': "G-W6Z3QZ6Q78",
    'databaseURL' : ""
  }
firebase = pyrebase.initialize_app(config)
auth=firebase.auth()
app.secret_key='secret'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
     if request.method == 'POST':
        email=request.form.get('username')
        password=request.form.get('password')
        try:
           auth.sign_in_with_email_and_password(email,password)
           session['user']=email
           return render_template('dashboard.html')
        except:
            auth.sign_in_with_email_and_password(email,password)
            return 'hello'
     return render_template('login.html')
    
@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        email=request.form.get('username')
        password=request.form.get('password')
        try:
            auth.create_user_with_email_and_password(email,password)
            return render_template('login.html')
        except:
            return 'try Again'
    return render_template('register.html')

@app.route('/logout')
def logout():
    return redirect('/')

if __name__ == "__main__":
    app.run()