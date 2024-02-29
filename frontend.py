from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

# Rota para exibir o formulário HTML
@app.route('/', methods=['GET'])
def index():
    return render_template('login.html')

# Rota para processar o formulário
@app.route('/authenticate', methods=['POST'])
def authenticate():
    email = request.form.get('email')
    password = request.form.get('password')

    # Envia os dados de autenticação para o módulo de autenticação
    response = requests.post('http://127.0.0.1:8000/authenticate', json={'email': email, 'password': password})

    if response.status_code == 200:
        return render_template('main_page.html')
    else:
        return "Erro na autenticação."
    
@app.route('/register')
def register():
    email = request.form.get('email')
    password = request.form.get('password')

    # Envia os dados de autenticação para o módulo de autenticação
    response = requests.post('http://127.0.0.1:8000/register', json={'email': email, 'password': password})

    if response.status_code == 200:
        return render_template('main_page.html')
    else:
        return "Erro na autenticação."

@app.route('/login', methods=['GET'])
def loginPage():
    return render_template('login.html')

@app.route('/registrar', methods=['GET'])
def registerPage():
    return render_template('registrar.html')

if __name__ == '__main__':
    app.run(port=5000)
