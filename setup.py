import psycopg2




def main():

    file = open('config/pw.txt', 'r')

    pw = file.readline()

    file.close()

    conn = psycopg2.connect(
        dbname="postgres",
        user="admin",
        password=pw,
        host="localhost",
        port=5432
    )

    cur = conn.cursor()
    # Create an analyst group
    cur.execute(
        "CREATE GROUP analyst;"
    )
    conn.commit()
    # Create the first analyst
    cur.execute(
        "CREATE USER josh PASSWORD 'p@assword' IN GROUP analyst;"
    )
    conn.commit()
    # Create the schema for data
    cur.execute(
        "CREATE SCHEMA baseball;"
    )
    conn.commit()
    # Grant only select to analysts
    # Data load should be done by superuser
    cur.execute(
        "GRANT SELECT ON ALL TABLES IN SCHEMA baseball TO analyst;"
    )
    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()