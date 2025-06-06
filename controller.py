import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Lucas3306",
        database="dados_formulario")

#Função para implementar pesquisa
def pesquisar_dados(query):
    db = connect_db()
    cursor = db.cursor()
    # Implementar a lógica de pesquisa no banco de dados (SQL)
    cursor.execute(f"SELECT * FROM dados WHERE sip OR ddr OR lp LIKE '%{query}%'")
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

