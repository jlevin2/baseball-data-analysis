import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import sql_conn

# conn = sql_conn.SQLConn('josh')
#
# ok, res, err = conn.executeSQL(
#                     """
#                         SELECT
#                           home_team,
#                           date_part('isoyear', date) AS year,
#                           SUM(CASE WHEN home_score > visiting_score THEN 1 ELSE 0 END)/
#                             SUM(1.0) AS winpct
#                         FROM baseball.game_data
#                         GROUP BY home_team,
#                           date_part('isoyear', date)
#                         """,
#                     True
#                 )
# if not ok:
#     raise Exception('Error getting results' + err)




def win_pct():
    conn = sql_conn.SQLConn('josh')

    ok, res, err = conn.executeSQL(
                        """
                            SELECT
                              home_team,
                              date_part('isoyear', date) AS year,
                              SUM(CASE WHEN home_score > visiting_score THEN 1 ELSE 0 END)/
                                SUM(1.0) AS winpct
                            FROM baseball.game_data
                            GROUP BY home_team,
                              date_part('isoyear', date)
                            """,
                        True
                    )
    if not ok:
        raise Exception('Error getting results' + err)

    df = pd.DataFrame(res, columns=["team", "year", "win_pct"])

    df['win_pct'] = df['win_pct'].astype('float')
    #df['year'] = pd.to_datetime(df['year'])

    dct = {}
    for _, row in df.iterrows():
        if row['team'] not in dct:
            dct[row['team']] = [0.0] * 8
        dct[row['team']][(2010 - int(row['year']))] = row['win_pct']

    df = pd.DataFrame(dct, index=['2010', '2011', '2012','2013','2014',
                                  '2015', '2016', '2017'])


    df.plot()

    matplotlib.pyplot.show()

win_pct()
