# Connect mysql server to python file
import mysql.connector

class Database:
    @staticmethod
    def connect():
        return mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "krishdurga143@",
            database = "bookmyshow"
        )
    
    
    