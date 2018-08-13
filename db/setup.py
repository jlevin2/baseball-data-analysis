from db.util import sql_conn

# Run on fresh postgres DB to setup permissions/schemas/etc.

def main():
    print('Starting!\n')
    con = sql_conn.SQLConn('super')
    print('Initializing!\n')
    ok, _, err = con.executeSQLFile('/Users/JoshLevin/PycharmProjects/' +
                                    'baseball-data-analysis/sql/initialization.sql',
                                    False)
    if not ok:
        raise Exception(err)

    ok, _, err = con.executeSQLFile('/Users/JoshLevin/PycharmProjects/' +
                                    'baseball-data-analysis/ddl/game_data.sql',
                                    False)
    if not ok:
        raise Exception(err)

    ok, _, err = con.executeSQLFile('/Users/JoshLevin/PycharmProjects/' +
                                    'baseball-data-analysis/ddl/prices.sql',
                                    False)

    if not ok:
        raise Exception(err)

    # ok, _, err = con.executeSQLFile('/Users/JoshLevin/PycharmProjects/' +
    #                                 'baseball-data-analysis/sql/baseball_load.sql',
    #                                 False)
    # if not ok:
    #     raise Exception(err)
    print('Complete DB setup')


if __name__ == "__main__":
    main()