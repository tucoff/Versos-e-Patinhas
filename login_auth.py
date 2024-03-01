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
db = firebase.database()

app = Flask(__name__)

# Rota para autenticar o usuário
@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    auth.sign_in_with_email_and_password(email,password)
    return jsonify({'token': 'autorizado'})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Criar um novo usuário
    user = auth.create_user_with_email_and_password(email, password)

    return jsonify({'token': 'autorizado'})

@app.route('/api/dados', methods=['GET', 'POST'])
def handle_data():
    try:
        if db.child("/").get().each()[0].val() is not None:
            data = db.child("/").get().each()[0].val()
            return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/armazenar', methods=['GET', 'POST'])
def armazenar():
    data = request.get_json()
    if data is not None:
        db.child("/").remove()
        db.push(data)
        print('Dados recebidos do servidor JavaScript:', data)
        return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
