// Função para enviar dados
function sendData(data) {
    fetch('http://127.0.0.1:5000/api/dados', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Erro na resposta do servidor');
        }
    })
    .then(data => {
        console.log('Resposta do servidor Python:', data);
    })
    .catch((error) => {
        console.error('Erro:', error);
    });
}

function requestData() {
    fetch('http://127.0.0.1:8000/api/dados', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.text())  // Alterado para response.text()
    .then(text => {
        try {
            const data = JSON.parse(text);
            console.log('Dados recebidos do servidor Python:', data);
            sendData(data);
        }
            catch (error) {
            console.error('Erro ao analisar o JSON:', error);
            console.log('Resposta do servidor:', text);
        }
    })
    .catch((error) => {
        console.error('Erro:', error);
    });
}

function storeData(data) {
    fetch('http://127.0.0.1:8000/armazenar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (response.headers.get('content-type').includes('application/json')) {
            return response.json();
        } else {
            throw new Error('Resposta do servidor não é um JSON válido');
        }
    })
    .then(data => {
        console.log('Resposta do servidor Python:', data);
    })
    .catch((error) => {
        console.error('Erro:', error);
    });
}

fetch('http://127.0.0.1:5000/getTextos')
    .then(response => response.json())
    .then(responseData => {        
        data = responseData.textos;
        console.log(data);
        if (data != null){storeData(data);}       
    });

requestData();