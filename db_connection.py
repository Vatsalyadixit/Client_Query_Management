import mysql.connector 

def get_connection(): # setting up the connection between python and SQL
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Vatsalya@235",
        database = "cqm"
    )