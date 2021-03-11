import sqlite3

def execute_command():
    connection = sqlite3.connect("C:/Users/Sergio/Desktop/UrlShort/urlShort/db.sqlite3")
    cursor = connection.cursor()
    sql_file = open("sample.sql")
    sql_as_string = sql_file.read()
    cursor.execute(sql_as_string)
    print(cursor.fetchall())

if __name__ == "__main__":
    execute_command()