from flask import *
from app.models.students import * 
from app.models.courses import *

students_bp = Blueprint('students', __name__)

@students_bp.route('/students/')
def students():
    students = get_students()
    return render_template('students.html', students=students)

@students_bp.route('/students/', methods=['GET', 'POST'])
def search_students():
    students = []
    if request.method == 'POST':
        search_query = request.form.get('studentsearch')
        if search_query:
            students = find_students(search_query)
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
    courses = get_course_codes()
    return render_template('addstudent.html', courses=courses)

@students_bp.route('/edit_student', methods=['GET', 'POST'])
def edit_student():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        first_name = request.form.get('first_name').title()
        last_name = request.form.get('last_name').title()
        course_code = request.form.get('course_code').upper()
        year_level = request.form.get('year_level')
        gender = request.form.get('gender').capitalize()
        print(student_id, first_name, last_name, course_code, year_level, gender)
        update_student(student_id, first_name, last_name, course_code, year_level, gender)
        return redirect('/students/') 
    student_id = request.args.get('student_id')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    course_code = request.args.get('course_code')
    year_level = request.args.get('year_level')
    gender = request.args.get('gender')
    courses = get_course_codes()
    return render_template('editstudent.html', student_id=student_id, first_name=first_name, last_name=last_name, course_code=course_code, year_level=year_level, gender=gender, courses=courses)

@students_bp.route('/delete_student/<string:student_id>', methods=['DELETE'])
def delete_student(student_id):
    print ("Deleting student")
    if request.method == 'DELETE':
        remove_student(student_id)
        return jsonify({'success': True})