import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import sql_conn

conn = sql_conn.SQLConn('josh')

ok, res, err = conn.executeSQL(
                    """SELECT
                          home_team,
                          date_trunc('year', date) AS year,
                          SUM(CASE WHEN home_score > visiting_score THEN 1 ELSE 0 END)/
                            SUM(1.0) AS winpct
                        FROM baseball.game_data
                        GROUP BY home_team,
                          date_trunc('year', date)""",
                    True
                )
if not ok:
    raise Exception('Error getting results' + err)

df = pd.DataFrame(res, columns=["team", "year", "win_pct"])

df['win_pct'] = df['win_pct'].astype('float')
df['year'] = pd.to_datetime(df['year'])

to_show = pd.DataFrame(index=df['year'].unique().sort_values('ascending'))


to_show = to_show.plot.line()

matplotlib.pyplot.show()


