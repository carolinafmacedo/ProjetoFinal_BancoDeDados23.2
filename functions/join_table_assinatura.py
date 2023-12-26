import sqlite3
print("Hello world!")
def join_table(): 
    conn = sqlite3.connect('streaming.db')
    cursor = conn.cursor()
    print('Conectando ao banco de dados')

    join_query = cursor.execute(
        """ 
        SELECT 
            tipo_Assinatura, nome_Cliente, sobrenome_Cliente
        FROM 
            assinatura
        LEFT JOIN
            dados_Cliente ON assinatura.id_Cliente = dados_Cliente.id_Cliente
        """)
    list_assinatura = join_query.fetchall()

    for assinatura in list_assinatura:
        print(assinatura) 

    return list_assinatura