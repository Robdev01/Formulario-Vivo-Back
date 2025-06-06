# Importa módulos do Flask para criar rotas, manipular requisições e retornar JSON
from flask import Blueprint, request, jsonify

# Importa a função que insere cliente no banco de dados
from controller import inserir_cliente

# Importa a função que retorna os nomes dos campos obrigatórios do cliente
from models import get_cliente_fields

# Cria um blueprint chamado 'cadastro_routes' para agrupar rotas relacionadas ao cadastro
cadastro_routes = Blueprint('cadastro_routes', __name__)

# Define a rota POST /api/cadastro para cadastrar um novo cliente
@cadastro_routes.route('/api/cadastro', methods=['POST'])
def cadastrar_cliente():
    # Captura os dados enviados no corpo da requisição em formato JSON
    data = request.json

    # Validação básica: verifica se todos os campos obrigatórios estão presentes e preenchidos
    for field in get_cliente_fields():
        if field not in data or not data[field]:
            # Retorna erro 400 (Bad Request) com mensagem indicando o campo ausente
            return jsonify({'error': f'Campo obrigatório: {field}'}), 400

    try:
        # Tenta inserir o cliente no banco de dados usando a função importada
        inserir_cliente(data)

        # Retorna mensagem de sucesso com status 201 (Created)
        return jsonify({'message': 'Cliente cadastrado com sucesso!'}), 201

    except Exception as e:
        # Em caso de erro, retorna uma mensagem com status 500 (Internal Server Error)
        return jsonify({'error': str(e)}), 500
