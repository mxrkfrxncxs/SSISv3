from flask_mysql_connector import MySQL

mysql = MySQL()

def get_students():
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    cursor.close()
    return students

def insert_student(student_id, first_name, last_name, course_code, year_level, gender):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO student (id, firstname, lastname, coursecode, yearlevel, gender) VALUES (%s, %s, %s, %s, %s, %s)", (student_id, first_name, last_name, course_code, year_level, gender))
    mysql.connection.commit()
    cursor.close()
    
def remove_student(student_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM student WHERE id = %s", (student_id,))
    mysql.connection.commit()
    cursor.close()