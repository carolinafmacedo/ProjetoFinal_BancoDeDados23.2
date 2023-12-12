from functions.create_database import create_database

create_database(
    database_name = 'streaming.db'
)


from functions.create_table import create_table

create_table(
    database_name = 'streaming.db',
    table_name = 'dados de cadastro',
    columns ='nome, e-mail, endereco, '
)

from functions.insert_rows import insert_many_rows

insert_many_rows(
'streaming.db', 'dados de cadastro',
'nome, e-mail, endereco',
[("99", "Luiz", 53), (100, "Rafael", 20)]
 )