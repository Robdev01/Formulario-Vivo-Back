# Função que retorna uma lista com os nomes dos campos da tabela 'clientes'
def get_cliente_fields():
    # Retorna uma lista contendo os nomes das colunas que representam os dados do cliente
    return ["id","cliente", "sip", "ddr", "lp", "atposx", "cabo", "fibras", "enlace", "porta"]

def get_cliente_fields_cadastro():
    # Retorna uma lista contendo os nomes das colunas que representam os dados do cliente
    return ["cliente", "sip", "ddr", "lp", "atposx", "cabo", "fibras", "enlace", "porta"]
def get_usuario_fields():
    return ['nome', 'login', 'senha', 'permissao']
