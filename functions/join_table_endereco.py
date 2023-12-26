import sqlite3
print("Hello world!")
def join_table(): 
    conn = sqlite3.connect('streaming.db')
    cursor = conn.cursor()
    print('Conectando ao banco de dados')

    join_query = cursor.execute(
        """ 
        SELECT id_Cliente, nome_Cliente, sobrenome_Cliente, CEP_Endereco, Bairro_Endereco, Cidade_Endereco
        FROM dados_Cliente
        LEFT JOIN endereco ON dados_Cliente.id_Endereco = endereco.id_Endereco
        """)
    list_endereco = join_query.fetchall()

    for assinatura in list_endereco:
        print(assinatura) 

    return list_endereco