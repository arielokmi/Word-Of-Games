import mysql.connector
def add_score(DIFFICULTY):
    POINTS_OF_WINNING = (int(DIFFICULTY)  *  3) + 5

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='db',
                                             user='root',
                                             password='example')
        mySql_insert_query = f"""INSERT INTO games.users_score (score) 
                               VALUE 
                               ("{POINTS_OF_WINNING}") """
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into users_score table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into users_score {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


add_score(3)