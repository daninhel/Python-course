import requests

api = "https://apiaulas.thiagodev502.repl.co/funcionarios"
cabecario = ['ID','Nome', 'Cargo', "Salario"]

requests.post(api, json={
    'nome': 'Jonas',
    'cargo': 'Jogador de futebol',
    'salario': '- R$100,00'
    })

