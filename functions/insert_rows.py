import sqlite3

def insert_one_row(
    database_name:str,
    table_name:str,  
    columns_name:str,
    values:str
) -> None:
    """ Insert one row in a table.

    Args:
        database_name(str): A database's name.
        table_name(str): A table's name.
        columns_name (str): Columns to insert the values.
        values (str): Values to insert.

    Example:
    ```{python}
        insert_one_row(
            'streaming.db', 'tabela',
            'titulo, nome',
            'Barbie, "Carol"'
        )
    ```    
    """

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO {table_name} ({columns_name}) VALUES ({values})
    """)

    conn.commit()
    conn.close()

def insert_many_rows(
    database_name:str,
    table_name:str,  
    columns_name:str,
    values_list:list        
) -> None:
    """ Insert many rows in a table.

    Args:
        database_name(str): A database's name.
        table_name(str): A table's name.
        columns_name (str): Columns to insert the values.
        values_list (list): A list with the values to insert.

    Example:
    ```{python}
        insert_many_rows(
            'streaming.db', 'tabela',
            'id, name, age',
            [(99, "Luiz", 53), (100, "Rafael", 20)]
        )
    ```    
    """

    conn = sqlite3.connect(database_name) 
    cursor = conn.cursor()

    placeholders = ', '.join(['?' for _ in range(len(values_list[0]))])

    query = f"INSERT INTO {table_name} ({columns_name}) VALUES ({placeholders})"

    cursor.executemany(query, values_list)

    conn.commit()
    conn.close()