from flask import Flask, render_template, session, request, redirect
import pyrebase

app = Flask(__name__)
config = {
    'apiKey': "AIzaSyD-HUi7t4AxKJCjdZoJwXNh1QjGL4Emfx8",
    'authDomain': "my-first-project-903ae.firebaseapp.com",
    'projectId': "my-first-project-903ae",
    'storageBucket': "my-first-project-903ae.appspot.com",
    'messagingSenderId': "469417932442",
    'appId': "1:469417932442:web:8fd49fe77cbd1b0ece9123",
    'databaseURL' : ""
}
firebase = pyrebase.initialize_app(config)
auth=firebase.auth()
app.secret_key='secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authenticate')
def authenticate():
    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('passowrd')
        try:
            user = auth.sign_in_with_email_and_password(email,password)
            session['user']=email
        except:
            return 'Failed to login'
    if user in session:
        return 'Hello User '
    

@app.route('/login',methods=['POST','GET'])
def login():
     return render_template('login.html')
    
@app.route('/register',methods=['POST','GET'])
def register():

    return render_template('register.html')

@app.route('/logout')
def logout():
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=False)