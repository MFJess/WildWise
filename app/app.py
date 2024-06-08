from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)

# Data do sistema no formato ISO
data_hora_atual = datetime.now()
data_formatada = data_hora_atual.strftime('%Y-%m-%d T %H: %M: %S')

# Index
@app.route('/')
def index():
    return render_template('index.html', data = {"data": data_formatada})

# Consulta
@app.route('/consulta')
def consulta():
    return render_template('consulta.html', data = {"data": data_formatada})

# Animais
@app.route('/animais')
def animais():
    return render_template('animais.html', data = {"data": data_formatada})

if __name__ == '__main__':
    app.run(debug=True)