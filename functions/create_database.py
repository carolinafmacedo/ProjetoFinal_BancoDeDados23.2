import sqlite3

def create_database(database_name:str):
    """Create a database

    Args:
        database_name (str): A database's name.
    """
    sqlite3.connect(database_name)