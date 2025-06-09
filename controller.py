from __init__ import mysql

from __init__ import mysql

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




def verificar_existencia(sip, ddr, lp):
    conn = mysql.connection
    cursor = conn.cursor()

    query = "SELECT * FROM dados WHERE sip = %s OR ddr = %s OR lp = %s"
    cursor.execute(query, (sip, ddr, lp))
    resultado = cursor.fetchone()

    cursor.close()
    return resultado is not None



def inserir_cliente(data):
    try:
        print("Inserindo no banco:", data)

        conn = mysql.connection
        print(f"{conn}")
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
        print("Erro ao inserir cliente:", e)
        raise
