from flask import Flask, render_template, request, url_for
from datetime import datetime
from queries import *
import requests
import re

regex = re.compile(r'[A-Z]?[a-z]+')

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
  
###############CONSULTA###################

# Consulta
@app.route('/consulta')
def consulta():
    return render_template('consulta.html', data = {"data": data_formatada})

#----------------------Animais----------------------

# Animais
@app.route('/animais')
def animais():
    sparql_query = all_animals()

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('animais.html', data = {"data": data_formatada, 
                                                       "dados": dados,
                                                       "tag": "Todos"})
    else:
        return render_template('empty.html', data = {"data": data_formatada})

# Animal unico
@app.route('/animais/<id>')
def animal(id):
    sparql_query = animal_characteristics(id)

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})

    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']

        info = list()
        
        for k,v in dados[0].items():
            col = regex.findall(k)
            coluna = ' '.join([c.capitalize() for c in col])
            valor = v['value']

            info.append((coluna,valor))

        return render_template('animal.html', data = {"data": data_formatada, 
                                                       "info": info, 
                                                       "tag": id})
    else:
        return render_template('empty.html', data = {"data": data_formatada})

#----------------------Reinos----------------------

# Reinos
@app.route('/reinos')
def reinos():
    sparql_query = all_kingdoms()

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('reinos.html', data = {"data": data_formatada, 
                                                       "dados": dados})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
    
# Reino Unico
@app.route('/reinos/<reino>')
def reino(reino):
    sparql_query = animal_by_kingdom(reino)

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('animais.html', data = {"data": data_formatada, 
                                                       "dados": dados,
                                                       "tag": reino})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
    
#----------------------Filos----------------------

# Filos
@app.route('/filos')
def filos():
    sparql_query = all_phylums()

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('filos.html', data = {"data": data_formatada, 
                                                       "dados": dados})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
    
# Filo Unico
@app.route('/filos/<filo>')
def filo(filo):
    sparql_query = animal_by_phylums(filo)

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('animais.html', data = {"data": data_formatada, 
                                                       "dados": dados,
                                                       "tag": filo})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
  
#----------------------Classes----------------------

# Classes
@app.route('/classes')
def classes():
    sparql_query = all_classes()

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('classes.html', data = {"data": data_formatada, 
                                                       "dados": dados})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
    
# Classe Unica
@app.route('/classes/<classe>')
def classe(classe):
    sparql_query = animal_by_classes(classe)

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('animais.html', data = {"data": data_formatada, 
                                                       "dados": dados,
                                                       "tag": classe})
    else:
        return render_template('empty.html', data = {"data": data_formatada})

#----------------------Ordens----------------------

# Ordens
@app.route('/ordens')
def ordens():
    sparql_query = all_orders()

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('ordens.html', data = {"data": data_formatada, 
                                                       "dados": dados})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
    
# Ordem Unica
@app.route('/ordens/<ordem>')
def ordem(ordem):
    sparql_query = animal_by_orders(ordem)

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('animais.html', data = {"data": data_formatada, 
                                                       "dados": dados,
                                                       "tag": ordem})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
    
#----------------------Familias----------------------

# Familias
@app.route('/familias')
def familias():
    sparql_query = all_families()

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('familias.html', data = {"data": data_formatada, 
                                                       "dados": dados})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
    
# Familia Unica
@app.route('/familias/<familia>')
def familia(familia):
    sparql_query = animal_by_families(familia)

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('animais.html', data = {"data": data_formatada, 
                                                       "dados": dados,
                                                       "tag": familia})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
    
#----------------------Generos----------------------

# Generos
@app.route('/generos')
def generos():
    sparql_query = all_genus()

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('generos.html', data = {"data": data_formatada, 
                                                       "dados": dados})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
    
# Genero Unico
@app.route('/generos/<genero>')
def genero(genero):
    sparql_query = animal_by_genus(genero)

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('animais.html', data = {"data": data_formatada, 
                                                       "dados": dados,
                                                       "tag": genero})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
    
#----------------------Localizacoes----------------------

# Localizacoes
@app.route('/localizacoes')
def localizacoes():
    sparql_query = all_locals()

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('locais.html', data = {"data": data_formatada, 
                                                       "dados": dados})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
    
# Local Unico
@app.route('/localizacoes/<local>')
def localizacao(local):
    sparql_query = animal_locations(local)

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('animais.html', data = {"data": data_formatada, 
                                                       "dados": dados,
                                                       "tag": local})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
    
#----------------------Habitats----------------------

# Habitats
@app.route('/habitats')
def habitats():
    sparql_query = all_habitat()

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('habitats.html', data = {"data": data_formatada, 
                                                       "dados": dados})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
    
# Habitat Unico
@app.route('/habitats/<habitat>')
def habitat(habitat):
    sparql_query = animal_habitats(habitat)

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('animais.html', data = {"data": data_formatada, 
                                                       "dados": dados,
                                                       "tag": habitat})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
    
#----------------------Cores----------------------

# Cores
@app.route('/cores')
def cores():
    sparql_query = all_colors()

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('cores.html', data = {"data": data_formatada, 
                                                       "dados": dados})
    else:
        return render_template('empty.html', data = {"data": data_formatada})
    
# Cor Unica
@app.route('/cores/<cor>')
def cor(cor):
    sparql_query = animal_colors(cor)

    resposta = requests.get(graphdb_endpoint,
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('animais.html', data = {"data": data_formatada, 
                                                       "dados": dados,
                                                       "tag": cor})
    else:
        return render_template('empty.html', data = {"data": data_formatada})

###############AUMENTAR################### 
  
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