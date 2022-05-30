import sqlite3
import constants


# try:
#    sqliteCon = sqlite3.connect('Datebase_python.db')
#   query_create_table = '''CREATE TABLE mytable (
#                               id INTEGER PRIMARY KEY AUTOINCREMENT,
#                              coins INTEGER);'''


# except sqlite3.Error as error:
#   print("Error while creating the table - ", error)

# finally:
#   if (sqliteCon):
#      sqliteCon.close()
#      print("database connection is closed")

def insert_coins():
    sqliteCon = sqlite3.connect('Datebase_python.db')
    cursor = sqliteCon.cursor()
    print("Connected to the database")
    # cursor.execute(query_create_table)
    # sqliteCon.commit()
    # print("Database created")

    cursor.execute("INSERT INTO mytable (coins) VALUES (" + str(constants.current_coins) + ")")
    print(cursor.execute("SELECT * FROM mytable"))
    res = cursor.fetchall()
    for row in res:
        print(row[0])
        print(row[1])

    cursor.close()
