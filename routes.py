# Importa módulos do Flask para criar rotas, manipular requisições e retornar JSON
from flask import Blueprint, request, jsonify

# Importa a função que insere cliente no banco de dados
from controller import inserir_cliente, verificar_existencia, buscar_por_sip, buscar_por_ddr, buscar_por_lp, entrar_login

# Importa a função que retorna os nomes dos campos obrigatórios do cliente
from models import get_cliente_fields, get_usuario_fields

# Cria um blueprint chamado 'cadastro_routes' para agrupar rotas relacionadas ao cadastro
cadastro_routes = Blueprint('cadastro_routes', __name__)

pesquisa_routes = Blueprint('pesquisa_routes',__name__)

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
        
    # Validação de duplicidade
    if verificar_existencia(data['sip'], data['ddr'], data['lp']):
        return jsonify({'error': 'Já existe um registro com esse SIP, DDR ou LP'}), 409  # 409 Conflict

    try:
        # Tenta inserir o cliente no banco de dados usando a função importada
        inserir_cliente(data)

        # Retorna mensagem de sucesso com status 201 (Created)
        return jsonify({'message': 'Cliente cadastrado com sucesso!'}), 201

    except Exception as e:
        # Em caso de erro, retorna uma mensagem com status 500 (Internal Server Error)
        return jsonify({'error': str(e)}), 500
    
@cadastro_routes.route('/buscar/sip', methods=['GET'])
def rota_sip():
    sip = request.args.get('sip')
    if not sip:
        return jsonify({'error': 'Parâmetro SIP ausente'}), 400
    resultados = buscar_por_sip(sip)
    return jsonify(resultados)

@cadastro_routes.route('/buscar/ddr', methods=['GET'])
def rota_ddr():
    ddr = request.args.get('ddr')
    if not ddr:
        return jsonify({'error': 'Parâmetro DDR ausente'}), 400
    resultados = buscar_por_ddr(ddr)
    return jsonify(resultados)

@cadastro_routes.route('/buscar/lp', methods=['GET'])
def rota_lp():
    lp = request.args.get('lp')
    if not lp:
        return jsonify({'error': 'Parâmetro LP ausente'}), 400
    resultados = buscar_por_lp(lp)
    return jsonify(resultados)

@cadastro_routes.route('/api/login',methods=['POST'])
def login_usuario():
    data = request.json

    for field in ['login', 'senha']:
        if field not in data or not data[field]:
            # Retorna erro 400 (Bad Request) com mensagem indicando o campo ausente
            return jsonify({'error': f'Campo obrigatório: {field}'}), 400 

    try:
        # Tenta inserir o login no banco de dados usando a função importada
        entrar_login(data)
        
        # Retorna mensagem de sucesso com status 201 (Created)
        return jsonify({'message': 'Login cadastrado com sucesso!',
                        'permissao': data['permissao'],
                        'login':data['login'],
                        'senha':data['senha']}), 201
    
        
        

    except Exception as e:
        # Em caso de erro, retorna uma mensagem com status 500 (Internal Server Error)
        return jsonify({'error': str(e)}), 500
