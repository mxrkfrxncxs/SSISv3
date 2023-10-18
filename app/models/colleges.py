from flask_mysql_connector import MySQL

mysql = MySQL()

def get_colleges():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM college"
    cursor.execute(query)
    colleges = cursor.fetchall()
    cursor.close()
    return colleges

def insert_college(college_code, college_name):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO college (collegecode, collegename) VALUES (%s, %s)", (college_code, college_name))
    mysql.connection.commit()
    cursor.close()