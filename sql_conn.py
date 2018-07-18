import psycopg2
import os

class SQLConn():
    def __init__(self):
        file = open('config/pw.txt', 'r')

        pw = file.readline()

        file.close()

        self.conn = psycopg2.connect(
                                dbname="postgres",
                                user="admin",
                                password=pw,
                                host="localhost",
                                port=5432
                            )
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def executeSQL(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            res = self.cur.fetchall()
            return True, res, ''
        except Exception as e:
            return False, [], str(e)


    def executeSQLFile(self, path):
        if not os.path.isfile(path):
            return False, 'File not found'

        file = open(path, 'r')

        try:
            self.cur.execute(file.read())
            self.conn.commit()
            res = self.cur.fetchall()
            file.close()
            return True, res, ''
        except Exception as e:
            file.close()
            return False, [], str(e)
