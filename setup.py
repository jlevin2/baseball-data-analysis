import sql_conn


def main():
    con = sql_conn.SQLConn()

    con.executeSQLFile('sql/initialization.sql')

    con.executeSQLFile('ddl/game_data.sql')

    con.executeSQLFile('sql/baseball_load.sql')


if __name__ == "__main__":
    main()