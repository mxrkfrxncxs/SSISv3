from flask_mysql_connector import MySQL

mysql = MySQL()

def get_courses():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM course"
    cursor.execute(query)
    courses = cursor.fetchall()
    cursor.close()
    return courses

def insert_course(course_code, course_name, college_code):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO course (coursecode, coursename, collegecode) VALUES (%s, %s, %s)", (course_code, course_name, college_code))
    mysql.connection.commit()
    cursor.close()