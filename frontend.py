from flask import Flask, request, render_template, redirect, url_for, jsonify
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
    
@app.route('/register', methods=['POST'])
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

@app.route('/api/dados', methods=['POST'])
def post_data():
    data = request.get_json()
    print('Dados recebidos do servidor JavaScript:', data)
    for poemas in data:
        textos.append(poemas)
    return jsonify({'status': 'success'})

# Lista para armazenar os textos
textos = []

@app.route('/adicionarTexto', methods=['POST'])
def adicionarTexto():
    texto = request.json.get('texto', '')
    textos.append(texto)
    print(textos)
    return jsonify(success=True)

@app.route('/getTextos', methods=['GET'])
def getTextos():
    # Retornar a lista de textos
    return jsonify(textos=textos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
