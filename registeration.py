from firebase_admin import auth, credentials
import pyrebase
import json

firebase = pyrebase.initialize_app(json.load(open('aktuauth.json')))
authen = firebase.auth()

def reg(email, password):
  authen.create_user_with_email_and_password(email,password)
  authen.sign_in_with_email_and_password(email,password)
  result  = authen.sign_in_with_email_and_password(email,password)
  user = auth.verify_id_token(result['idToken'])
  uid = user['uid']
  
  


