<<<<<<< HEAD
from flask import Flask, request
from controller import pesquisar_dados

app = Flask(__name__)

@app.route('/')
def index():
   

@app.route('/login')
def login():
   

@app.route('/pesquisa',methods=['GET', 'POST'])
def pesquisa():
    if request.method == 'POST':
        query = request.form['campo_de_pesquisa']
        return pesquisar_dados(query)
   


@app.route('/admin')
def admin():
   


=======
from flask import Flask, request
from controller import pesquisar_dados

app = Flask(__name__)

@app.route('/')
def index():
   

@app.route('/login')
def login():
   

@app.route('/pesquisa',methods=['GET', 'POST'])
def pesquisa():
    if request.method == 'POST':
        query = request.form['campo_de_pesquisa']
        resultados = pesquisar_dados(query)
   


@app.route('/admin')
def admin():
   


>>>>>>> 4665025c03959af20def22a9d033fea9eac0f70d
