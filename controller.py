from __init__ import mysql
import traceback

def buscar_por_sip(sip):
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dados WHERE sip LIKE %s", (f"%{sip}%",))
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        cursor.close()
        return [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        print(f"Erro em buscar_por_sip: {str(e)}")
        raise

def buscar_por_ddr(ddr):
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dados WHERE ddr LIKE %s", (f"%{ddr}%",))
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        cursor.close()
        return [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        print(f"Erro em buscar_por_ddr: {str(e)}")
        raise

def buscar_por_lp(lp):
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dados WHERE lp LIKE %s", (f"%{lp}%",))
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        cursor.close()
        return [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        print(f"Erro em buscar_por_lp: {str(e)}")
        raise

def verificar_existencia(sip, ddr, lp):
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        query = "SELECT * FROM dados WHERE sip = %s OR ddr = %s OR lp = %s"
        cursor.execute(query, (sip, ddr, lp))
        resultado = cursor.fetchone()
        cursor.close()
        return resultado is not None
    except Exception as e:
        print(f"Erro em verificar_existencia: {str(e)}")
        raise

def inserir_cliente(data):
    try:
        print("Inserindo no banco:", data)
        conn = mysql.connection
        print(f"Conexão MySQL: {conn}")
        cursor = conn.cursor()
        query = """
            INSERT INTO dados (cliente, sip, ddr, lp, atposx, cabo, fibras, enlace, porta)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
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
        cursor.execute(query, valores)
        conn.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao inserir cliente: {str(e)}\n{traceback.format_exc()}")
        raise


def cadastrar_usuarios(data):
    try:
        print("Inserindo usuário no banco:", data)
        conn = mysql.connection
        print(f"Conexão MySQL: {conn}")
        cursor = conn.cursor()
        query = """
            INSERT INTO usuarios (nome, login, senha, permissao)
            VALUES (%s, %s, %s, %s)
        """
        valores_user = (
            data['nome'],
            data['login'],
            data['senha'],
            data['permissao']
        )
        cursor.execute(query, valores_user)
        conn.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao inserir usuário: {str(e)}\n{traceback.format_exc()}")
        raise

def autenticar_usuario(login, senha):
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        query = "SELECT nome, login, permissao FROM usuarios WHERE login = %s AND senha = %s"
        cursor.execute(query, (login, senha))
        resultado = cursor.fetchone()
        cursor.close()
        if resultado:
            columns = ['nome', 'login', 'permissao']
            return dict(zip(columns, resultado))
        return None
    except Exception as e:
        print(f"Erro em autenticar_usuario: {str(e)}\n{traceback.format_exc()}")
        raise

def verificar_login_existente(login):
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE login = %s", (login,))
        resultado = cursor.fetchone()
        cursor.close()
        return resultado is not None
    except Exception as e:
        print(f"Erro em verificar_login_existente: {str(e)}\n{traceback.format_exc()}")
        raise