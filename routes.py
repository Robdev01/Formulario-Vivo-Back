from flask import Blueprint, request, jsonify
from controller import inserir_cliente, verificar_existencia,buscar_por_sip, buscar_por_ddr, buscar_por_lp

from models import get_cliente_fields


cadastro_routes = Blueprint('cadastro_routes', __name__)

@cadastro_routes.route('/cadastro', methods=['POST'])
def cadastrar_cliente():
    data = request.json

    # Validação de campos obrigatórios
    for field in get_cliente_fields():
        if field not in data or not data[field]:
            return jsonify({'error': f'Campo obrigatório: {field}'}), 400

    # Validação de duplicidade
    if verificar_existencia(data['sip'], data['ddr'], data['lp']):
        return jsonify({'error': 'Já existe um registro com esse SIP, DDR ou LP'}), 409  # 409 Conflict

    try:
        print("📩 Dados recebidos no cadastro:", data)
        inserir_cliente(data)
        return jsonify({'message': 'Cliente cadastrado com sucesso!'}), 201
    except Exception as e:
        print("Erro interno ao cadastrar:", e)
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