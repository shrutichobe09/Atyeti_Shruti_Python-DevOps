import mysql.connector

def getConnection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='python'
    )
