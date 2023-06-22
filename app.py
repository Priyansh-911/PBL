from flask import Flask, render_template, session, request, redirect, url_for
import pyrebase
import firebase_admin
from firebase_admin import credentials, auth
import json
from registeration import reg

#initialize app
app = Flask(__name__)




#connecting to firebase
cred = credentials.Certificate("aktu-auth-424a7-firebase-adminsdk-fzyqv-da854a3261.json")
firebase_admin.initialize_app(cred)
firebase = pyrebase.initialize_app(json.load(open('aktuauth.json')))
authen = firebase.auth()
app.secret_key='secret'






@app.route('/')
def index():
    return render_template('lastindex.html')








@app.route('/login',methods=['POST','GET'])
def login():
     if request.method == 'POST':
        email=request.form.get('username')
        password=request.form.get('password')
        try:
           authen.sign_in_with_email_and_password(email,password)
           session['user']=email
           result  = authen.sign_in_with_email_and_password(email,password)
           user = auth.verify_id_token(result['idToken'])
           uid = user['uid']
           return redirect(url_for('dashboard'))
        except:
            authen.sign_in_with_email_and_password(email,password)
            return render_template('login.html')
     return render_template('login.html')







@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        email = request.form.get('username')
        password = request.form.get('password')
        try:
            # authen.create_user_with_email_and_password(email,password)
            reg(email, password)
            return redirect(url_for('dashboard'))
        except:
            return 'try Again'
    return render_template('register.html')







@app.route('/dashboard')
def dashboard():
    if 'user' in session:
      user = session['user']
    #   print(user)
    #   print(session['user'])
    #   print(session)
      return render_template('dashboard.html', name = user)







@app.route('/profile')
def profile():
    print('hello world!')






@app.route('/logout')
def logout():
    return redirect('/')

if __name__ == "__main__":
    app.run()