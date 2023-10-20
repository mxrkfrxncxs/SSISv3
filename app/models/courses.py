from flask_mysql_connector import MySQL

mysql = MySQL()

def get_courses():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM course"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def find_courses(searchcourse):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + searchcourse + "%"
    cursor.execute("SELECT * FROM course WHERE coursecode LIKE %s OR coursename LIKE %s OR collegecode LIKE %s", (search_query, search_query, search_query))
    result = cursor.fetchall()
    cursor.close()
    return result

def check(course_code):
    cursor = mysql.connection.cursor()
    query = "SELECT coursecode FROM course WHERE coursecode = %s"
    cursor.execute(query, (course_code,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return True

def insert_course(course_code, course_name, college_code):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO course (coursecode, coursename, collegecode) VALUES (%s, %s, %s)", (course_code, course_name, college_code))
    mysql.connection.commit()
    cursor.close()
    
def update_course(course_code, course_name, college_code):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE course SET coursename = %s, collegecode = %s WHERE coursecode = %s"
    cursor.execute(update_query, (course_name, college_code, course_code))
    mysql.connection.commit()
    cursor.close()

def remove_course(course_code):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM course WHERE coursecode = %s", (course_code,))
    mysql.connection.commit()
    cursor.close()    
    
def get_college_codes():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT collegecode FROM college"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result