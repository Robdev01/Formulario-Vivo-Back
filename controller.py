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

def entrar_login(data):
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("USE dados_formulario")

    query = """ INSERT INTO usuarios (nome, login, senha, permissao)
                VALUES (%s,%s,%s,%s)"""
    
    valores = ( 
                data["nome"],
                data["login"],
                data["senha"],
                data["permissao"])
    
    cursor.execute(query,valores)
    conn.commit()
    cursor.close()



def verificar_existencia(sip, ddr, lp):
    conn = mysql.connection
    cursor = conn.cursor()

    query = "SELECT * FROM dados WHERE sip = %s OR ddr = %s OR lp = %s"
    cursor.execute(query, (sip, ddr, lp))
    resultado = cursor.fetchone()

    cursor.close()
    return resultado is not None

def buscar_por_sip(sip):
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dados WHERE sip LIKE %s", (f"%{sip}%",))
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    cursor.close()
    return [dict(zip(columns, row)) for row in rows]

def buscar_por_ddr(ddr):
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dados WHERE ddr LIKE %s", (f"%{ddr}%",))
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    cursor.close()
    return [dict(zip(columns, row)) for row in rows]

def buscar_por_lp(lp):
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dados WHERE lp LIKE %s", (f"%{lp}%",))
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    cursor.close()
    return [dict(zip(columns, row)) for row in rows]




    



