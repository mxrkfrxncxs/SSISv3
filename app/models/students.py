from flask_mysql_connector import MySQL

mysql = MySQL()

def get_students():
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    cursor.close()
    return students

def find_students(searchstudent):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + searchstudent + "%"
    cursor.execute("SELECT * FROM student WHERE id LIKE %s OR firstname LIKE %s OR lastname LIKE %s OR coursecode LIKE %s OR yearlevel LIKE %s OR gender LIKE %s", (search_query, search_query, search_query, search_query, search_query, search_query))
    students = cursor.fetchall()
    cursor.close()
    return students

def find_student(student_id):
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student WHERE id = %s", (student_id,))
    student = cursor.fetchone()
    cursor.close()
    return student

def check(student_id):
    cursor = mysql.connection.cursor()
    query = "SELECT id FROM student WHERE id = %s"
    cursor.execute(query, (student_id,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return True

def insert_student(student_id, first_name, last_name, course_code, year_level, gender, image_url):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO student (id, firstname, lastname, coursecode, yearlevel, gender, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s)", (student_id, first_name, last_name, course_code, year_level, gender, image_url))
    mysql.connection.commit()
    cursor.close()
    
def update_student(student_id, first_name, last_name, course_code, year_level, gender, image_url):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE student SET firstname = %s, lastname = %s, coursecode = %s, yearlevel = %s, gender = %s, image_url = %s WHERE id = %s"
    cursor.execute(update_query, (first_name, last_name, course_code, year_level, gender, image_url, student_id))
    mysql.connection.commit()
    cursor.close()

def remove_student(student_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM student WHERE id = %s", (student_id,))
    mysql.connection.commit()
    cursor.close()
    
def get_course_codes():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT coursecode FROM course"
    cursor.execute(query)
    course_code = cursor.fetchall()
    cursor.close()
    return course_code

def read_student(student_id):
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT student.id, student.firstname, student.lastname, student.yearlevel, student.gender, course.coursecode, course.coursename, college.collegecode, college.collegename FROM student JOIN course ON student.coursecode = course.coursecode JOIN college ON course.collegecode = college.collegecode WHERE student.id = %s"
    cursor.execute(query, (student_id,))
    result = cursor.fetchone()
    cursor.close()
    return result

