# Importa a instância mysql criada no app.py
from app import mysql

# Função responsável por inserir um cliente no banco de dados
def inserir_cliente(data):
    # Obtém a conexão com o banco de dados MySQL
    conn = mysql.connection

    # Cria um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Define a query SQL de inserção (INSERT INTO) com placeholders (%s) para os dados
    query = """
        INSERT INTO clientes (sip, ddr, lp, nome, bairro, endereco, numero, referencia)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Preenche os valores com base no dicionário 'data' recebido
    valores = (
        data['sip'],
        data['ddr'],
        data['lp'],
        data['nome'],
        data['bairro'],
        data['endereco'],
        data['numero'],
        data['referencia']
    )

    # Executa a query com os valores passados
    cursor.execute(query, valores)

    # Salva as alterações no banco (confirma o INSERT)
    conn.commit()

    # Fecha o cursor para liberar recursos
    cursor.close()