# Importa a instância mysql criada no app.py
from __init__ import mysql

# Função responsável por inserir um cliente no banco de dados
def inserir_cliente(data):
    try:
        print("🛠️ Inserindo no banco:", data)
    # Obtém a conexão com o banco de dados MySQL
        conn = mysql.connection
        print(f"{conn}")

    # Cria um cursor para executar comandos SQL
        cursor = conn.cursor()
        cursor.execute("USE dados_formulario")

    # Define a query SQL de inserção (INSERT INTO) com placeholders (%s) para os dados
        query = """
            INSERT INTO dados (cliente, sip, ddr, lp, atposx, cabo, fibras, enlace, porta)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    # Preenche os valores com base no dicionário 'data' recebido
        valores = (
            data['cliente'],
            data['sip'],
            data['ddr'],
            data['lp'],
            data['atposx'],
            data['cabo'],
            data['fibras'],
            data['enlace'],
            data['porta']
        )

    # Executa a query com os valores passados
        cursor.execute(query, valores)

    # Salva as alterações no banco (confirma o INSERT)
        conn.commit()

    # Fecha o cursor para liberar recursos
        cursor.close()

    except Exception as e:        
        print("❌ Erro ao inserir cliente:", e)        
    raise

#def pesquisar_sip():
    # Obtém a conexão com o banco de dados MySQL
    #conn = mysql.connection

    # Cria um cursor para executar comandos SQL
    #cursor = conn.cursor()

    #Define a query de pesquisa(SELECT FROM) onde será procurado o valor do sip
    #query='''
    #    SELECT sip FROM dados WHERE sip = %s'''
    
    #Executa a query
    #cursor.execute(query)



