from flask import *
from app.models.students import *
import re
from config import CLOUDINARY_FOLDER
import cloudinary
from cloudinary.uploader import upload as cloudinary_upload
from cloudinary.utils import cloudinary_url

students_bp = Blueprint('students', __name__)

@students_bp.route('/students/')
def students():
    students = get_students()
    return render_template('students.html', students=students)

@students_bp.route('/students/search', methods=['GET', 'POST'])
def search_student():
    students = []
    if request.method == 'POST':
        search_query = request.form.get('studentsearch')
        if search_query:
            students = find_students(search_query)
    return render_template('students.html', students=students, search_query=search_query)

@students_bp.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        first_name = request.form['first_name'].title()
        last_name = request.form['last_name'].title()
        course_code = request.form['course_code'].upper()
        year_level = request.form['year_level']
        image_url = request.form['image_url']
        gender = request.form['gender'].capitalize()
        if not re.match(r'^\d{4}-\d{4}$', student_id):
            flash('Invalid Student ID format. Follow YYYY-NNNN format.', 'error')
        elif check(student_id):
            flash('Student ID already exists!', 'error')
        elif len(student_id)> 10:
            flash('Student ID too long!', 'error')
        else:
            insert_student(student_id, first_name, last_name, course_code, year_level, gender, image_url)
            flash('Student added successfully!', 'success')
            return redirect('/students/') 
    courses = get_course_codes()
    return render_template('addstudent.html', courses=courses)

@students_bp.route('/edit_student/<string:id>', methods=['GET', 'POST'])
def edit_student(id):
    if request.method == 'POST':
        image_url = request.form.get('image_url') 
        student_id = request.form.get('student_id')
        first_name = request.form.get('first_name').title()
        last_name = request.form.get('last_name').title()
        course_code = request.form.get('course_code').upper()
        year_level = request.form.get('year_level')
        gender = request.form.get('gender').capitalize()
        update_student(student_id, first_name, last_name, course_code, year_level, gender, image_url)
        flash('Student updated successfully!', 'success')
        return redirect('/students/') 
    student_info = find_student(id)
    first_name = student_info['firstname']
    last_name = student_info['lastname']
    course_code = student_info['coursecode']
    year_level = student_info['yearlevel']
    gender = student_info['gender']
    image_url = student_info['image_url']
    courses = get_course_codes()
    return render_template('editstudent.html', student_id=id, first_name=first_name, last_name=last_name, course_code=course_code, year_level=year_level, gender=gender, courses=courses, image_url=image_url)

@students_bp.route('/delete_student/<string:student_id>', methods=['DELETE'])
def delete_student(student_id):
    if request.method == 'DELETE':
        remove_student(student_id)
        flash('Student deleted successfully!', 'success')
        return jsonify({'success': True})
    
@students_bp.route('/view_student/<string:student_id>')
def view_student(student_id):
    data = read_student(student_id)
    return render_template('studentinfo.html', data=data)

@students_bp.route('/upload/cloudinary/', methods=['POST'])
def upload_to_cloudinary():
    file = request.files.get('file')

    if file:
        upload_result = cloudinary_upload(
            file, folder=CLOUDINARY_FOLDER)

        return jsonify({
            'is_success': True,
            'url': upload_result['secure_url']
        })

    return jsonify({
        'is_success': False,
        'error': 'Missing file'
    })
