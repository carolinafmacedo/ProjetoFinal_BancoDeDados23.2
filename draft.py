from functions.create_database import create_database

create_database(
    database_name = 'streaming.db'
)


from functions.create_table import create_table

create_table(
    database_name = 'streaming.db',
    table_name = 'dados_Cliente',
    columns ='id_Cliente, nome_Cliente, sobrenome_Cliente, email_Cliente, celular_Cliente, id_Endereco, senha_Cliente, data_Criacao, id_Assinatura'
)

from functions.insert_rows import insert_many_rows

insert_many_rows(
'streaming.db', 'dados_Cliente',
'id_Cliente, nome_Cliente, sobrenome_Cliente, email_Cliente, celular_Cliente, id_Endereco, senha_Cliente, data_Criacao, id_Assinatura',
[(3211, "Mirella", "Santana", "mirellasantana@gmail.com", "8199998888", 3212, "belinha", "21/08/22", 3213), (3214, "Carolina", "Macedo", "carolinamacedo@gmail.com", "8188884444", 3215, "abcd123", "23/10/23", 3216)]
 )