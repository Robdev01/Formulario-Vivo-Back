from flask import Flask
from flask_cors import CORS
from __init__ import mysql

def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"/*": {"origins": "*"}})

    app.config['MYSQL_HOST'] = '127.0.0.1'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'dados_formularios'


    print("📋 Conectando ao MySQL:")
    print(f"HOST: {app.config['MYSQL_HOST']}")
    print(f"USER: {app.config['MYSQL_USER']}")
    print(f"PASSWORD: {'(vazio)' if app.config['MYSQL_PASSWORD'] == '' else '********'}")
    print(f"DATABASE: {app.config['MYSQL_DB']}")

    try:
        mysql.init_app(app)
        with app.app_context():
            conn = mysql.connect()
            conn.close()
        print("✅ Conexão com o MySQL estabelecida com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao conectar ao MySQL: {str(e)}")

    from routes import cadastro_routes
    app.register_blueprint(cadastro_routes)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
    
    
