from flask import Flask, request
from controller import connect_db, pesquisar_dados


app = Flask(__name__)





if __name__=='__name__':
    app.run(debug=True)