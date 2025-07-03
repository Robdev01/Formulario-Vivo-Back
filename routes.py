from flask import Blueprint, request, jsonify
from controller import inserir_cliente, verificar_existencia, buscar_por_sip, buscar_por_ddr, buscar_por_lp, \
    cadastrar_usuarios, autenticar_usuario, verificar_login_existente, atualizar_cliente, deletar_cliente
from models import get_cliente_fields, get_usuario_fields, get_cliente_fields_cadastro

cadastro_routes = Blueprint('cadastro_routes', __name__)


@cadastro_routes.route('/cadastro', methods=['POST'])
def cadastrar_cliente():
    data = request.json
    for field in get_cliente_fields_cadastro():
        if field not in data or not data[field]:
            pass 
    try:
        if verificar_existencia(data['sip'], data['ddr'], data['lp']):
            return jsonify({'error': 'Já existe um registro com esse SIP, DDR ou LP'}), 409
        inserir_cliente(data)
        return jsonify({'message': 'Cliente cadastrado com sucesso!'}), 201
    except Exception as e:
        return jsonify({'error': f'Erro ao cadastrar cliente: {str(e)}'}), 500

@cadastro_routes.route('/buscar/sip', methods=['GET'])
def rota_sip():
    sip = request.args.get('sip')
    if not sip:
        return jsonify({'error': 'Parâmetro SIP ausente'}), 400
    try:
        resultados = buscar_por_sip(sip)
        return jsonify(resultados)
    except Exception as e:
        return jsonify({'error': f'Erro ao buscar por SIP: {str(e)}'}), 500

@cadastro_routes.route('/buscar/ddr', methods=['GET'])
def rota_ddr():
    ddr = request.args.get('ddr')
    if not ddr:
        return jsonify({'error': 'Parâmetro DDR ausente'}), 400
    try:
        resultados = buscar_por_ddr(ddr)
        return jsonify(resultados)
    except Exception as e:
        return jsonify({'error': f'Erro ao buscar por DDR: {str(e)}'}), 500

@cadastro_routes.route('/buscar/lp', methods=['GET'])
def rota_lp():
    lp = request.args.get('lp')
    if not lp:
        return jsonify({'error': 'Parâmetro LP ausente'}), 400
    try:
        resultados = buscar_por_lp(lp)
        return jsonify(resultados)
    except Exception as e:
        return jsonify({'error': f'Erro ao buscar por LP: {str(e)}'}), 500

@cadastro_routes.route('/api/cadastro_usuario', methods=['POST'])
def cadastrar_usuario():
    data = request.json
    for field in get_usuario_fields():
        if field not in data or not data[field]:
            return jsonify({'error': f'Campo obrigatório: {field}'}), 400
    try:
        if verificar_login_existente(data['login']):
            return jsonify({'error': 'Login já existe'}), 409
        cadastrar_usuarios(data)
        return jsonify({'message': 'Usuário cadastrado com sucesso!'}), 201
    except Exception as e:
        return jsonify({'error': f'Erro ao cadastrar usuário: {str(e)}'}), 500

@cadastro_routes.route('/api/login', methods=['POST'])
def login_usuario():
    data = request.json
    for field in ['login', 'senha']:
        if field not in data or not data[field]:
            return jsonify({'error': f'Campo obrigatório: {field}'}), 400
    try:
        usuario = autenticar_usuario(data['login'], data['senha'])
        if usuario:
            return jsonify({
                'message': 'Login realizado com sucesso!',
                'nome': usuario['nome'],
                'login': usuario['login'],
                'permissao': usuario['permissao']
            }), 200
        else:
            return jsonify({'error': 'Login ou senha inválidos'}), 401
    except Exception as e:
        return jsonify({'error': f'Erro ao realizar login: {str(e)}'}), 500

@cadastro_routes.route('/atualizar/cadastro/<int:id>', methods=['PUT'])
def atualizar_cliente_route(id):
    data = request.json
    try:
        atualizar_cliente(id, data)
        return jsonify({'message': 'Cliente atualizado com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': f'Erro ao atualizar cliente: {str(e)}'}), 500


@cadastro_routes.route('/cadastro/<int:id>', methods=['DELETE'])
def deletar_cliente_route(id):
    try:
        deletar_cliente(id)
        return jsonify({'message': 'Cliente deletado com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': f'Erro ao deletar cliente: {str(e)}'}), 500
