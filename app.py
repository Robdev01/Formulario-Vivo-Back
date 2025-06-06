# Importa a classe Flask para criar a aplicação web
from flask import Flask

# Importa o CORS para permitir requisições de outras origens (útil para frontend separado)
from flask_cors import CORS

# Importa o conector MySQL compatível com Flask
from flask_mysqldb import MySQL

# Importa a função para carregar variáveis de ambiente do arquivo .env
from dotenv import load_dotenv

# Importa o módulo os para acessar variáveis de ambiente
import os

# Instancia o objeto MySQL fora da função para usá-lo em outros módulos
mysql = MySQL()

# Função responsável por criar e configurar a aplicação Flask
def create_app():
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()

    # Cria uma instância do Flask
    app = Flask(__name__)

    # Habilita o CORS para a aplicação (permitindo que o frontend acesse a API)
    CORS(app)

    # Define as configurações do banco de dados usando variáveis do .env
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')             # Ex: "localhost"
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')             # Ex: "root"
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')     # Ex: "senha"
    app.config['MYSQL_DATABASE'] = os.getenv('MYSQL_DATABASE')     # Ex: "nome_do_banco"

    # Inicializa o MySQL com a app Flask
    mysql.init_app(app)

    # Importa e registra os blueprints com as rotas (ex: cadastro)
    from routes import cadastro_routes
    app.register_blueprint(cadastro_routes)

    # Retorna a instância configurada da aplicação Flask
    return app

# Verifica se o arquivo está sendo executado diretamente
if __name__ == '__main__':
    # Cria e inicializa o app
    app = create_app()

    # Roda o servidor Flask em modo debug
    app.run(debug=True)
