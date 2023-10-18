from flask import *
from app.models.students import * 

students_bp = Blueprint('students', __name__)

@students_bp.route('/students/')
def students():
    students = get_students()
    return render_template('students.html', students=students)

@students_bp.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        first_name = request.form['first_name'].title()
        last_name = request.form['last_name'].title()
        course_code = request.form['course_code'].upper()
        year_level = request.form['year_level']
        gender = request.form['gender'].capitalize()
        insert_student(student_id, first_name, last_name, course_code, year_level, gender)
        return redirect('/students/') 
    return render_template('addstudent.html')

@students_bp.route('/delete_student/<string:student_id>', methods=['DELETE'])
def delete_student(student_id):
    if request.method == 'DELETE':
        remove_student(student_id)
        return redirect('/students/') 