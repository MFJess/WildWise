from flask import Flask, render_template, request
from datetime import datetime
from queries import *
import requests

app = Flask(__name__)

# Data do sistema no formato ISO
data_hora_atual = datetime.now()
data_formatada = data_hora_atual.strftime('%Y-%m-%d T %H: %M: %S')

# GraphDB endpoint
graphdb_endpoint = "http://localhost:7200/repositories/animals"

# Index
@app.route('/')
def index():
    return render_template('index.html', data = {"data": data_formatada})
  
#----------------------Consulta----------------------

# Consulta
@app.route('/consulta')
def consulta():
    return render_template('consulta.html', data = {"data": data_formatada})

# Animais
@app.route('/animais')
def animais():
    sparql_query = all_animals()

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        print(dados)
        return render_template('animais.html', data = {"data": data_formatada})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
  
#----------------------Aumentar----------------------  
  
# Aumentar
@app.route('/aumentar', methods=['POST','GET'])
def aumentar():
    if request.method == 'POST':
        forms = dict(request.form)

        return render_template('success.html', data = {"data": data_formatada,"name":forms['name']})
    else:
        return render_template('aumentar.html', data = {"data": data_formatada}) 

if __name__ == '__main__':
    app.run(debug=True)