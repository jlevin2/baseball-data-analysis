import psycopg2
import os
import configparser

# Utility class that reads from config file
# and executes a SQL file or raw sql as specified user

class SQLConn():
    def __init__(self, config):
        conf = configparser.ConfigParser()

        conf.read('../../config/db-config.ini')

        self.conn = psycopg2.connect(
                                dbname=conf[config]['dbname'],
                                user=conf[config]['user'],
                                password=conf[config]['password'],
                                host=conf[config]['host'],
                                port=conf[config]['port']
                            )
        self.cur = self.conn.cursor()

    def __del__(self):
        if hasattr(self, 'cur'):
            self.cur.close()
            self.conn.close()

    def executeSQL(self, sql, fetch):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            if fetch:
                res = self.cur.fetchall()
                return True, res, ''
            else:
                return True, [], ''
        except Exception as e:
            return False, [], str(e)


    def executeSQLFile(self, path, fetch):
        if not os.path.exists(path):
            return False, [], 'File not found: {0}!'.format(path)

        file = open(path, 'r')

        try:
            self.cur.execute(file.read())
            self.conn.commit()
            file.close()
            if fetch:
                res = self.cur.fetchall()
                return True, res, ''
            else:
                return True, [], ''
        except Exception as e:
            file.close()
            return (False, [], str(e))
