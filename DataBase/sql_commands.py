import sqlite3
from DataBase import sql
class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()


    def sql_create_tables(self):
        if self.connection:
            print('DataBase Connection')

        self.connection.execute(sql.CREATE_USER_TABLE)


    def sql_insert_users(self,telegram_id,username,first_name,last_name):
        self.cursor.execute(
            sql.INSERT_USER,
            (None,telegram_id,username,first_name,last_name)

        )
        self.connection.commit()
    def sql_answer_insert(self,answers):
        self.cursor.execute(
            sql.INSERT_ANSWER,
            (None,answers)
        )
        self.connection.commit()
