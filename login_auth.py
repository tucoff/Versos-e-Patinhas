from flask import Flask, request, jsonify, render_template
import pyrebase
import requests

config = {
  "apiKey": "AIzaSyAcDcWz4tFnOqnrUHowC4FhrLcAdy7BXAM",
  "authDomain": "versos-e-patinhas.firebaseapp.com",
  "databaseURL": "https://versos-e-patinhas-default-rtdb.firebaseio.com",
  "projectId": "versos-e-patinhas",
  "storageBucket": "versos-e-patinhas.appspot.com",
  "messagingSenderId": "487991932820",
  "appId": "1:487991932820:web:ab0208c3457eb8e7a60181",
  "measurementId": "G-LWXRESG2SV"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app = Flask(__name__)

# Rota para autenticar o usuário
@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    auth.sign_in_with_email_and_password(email,password)
    return jsonify({'token': 'autorizado'})

# Rota para autenticar o usuário
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    auth.create_user_with_email_and_password(email,password)
    return jsonify({'token': 'autorizado'})

if __name__ == '__main__':
    app.run(port=8000)

# def signup():
#   print("Sign up...")
#   email = input("Enter email: ")
#   password = input("Enter password: ")
#   try:
#     user = auth.create_user_with_email_and_password(email,password)
#   except:
#     print()
#   return