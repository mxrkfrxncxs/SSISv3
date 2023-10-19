from flask import *
from app.models.courses import * 

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses/')
def courses():
    courses = get_courses()
    return render_template('courses.html', courses=courses)

@courses_bp.route('/courses/search', methods=['GET', 'POST'])
def search_course():
    courses = []
    if request.method == 'POST':
        search_query = request.form.get('coursesearch')
        if search_query:
            courses = find_courses(search_query)
    return render_template('courses.html', courses=courses)

@courses_bp.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_code = request.form['course_code'].upper()
        course_name = request.form['course_name']
        college_code = request.form['college_code'].upper()
        insert_course(course_code, course_name, college_code)
        return redirect('/courses') 
    colleges = get_college_codes()
    return render_template('addcourse.html', colleges=colleges)

@courses_bp.route('/edit_course', methods=['GET', 'POST'])
def edit_course():
    if request.method == 'POST':
        course_code = request.form.get('course_code')
        course_name = request.form.get('course_name')
        college_code = request.form.get('college_code').upper()
        print(course_code, course_name, college_code)
        update_course(course_code, course_name, college_code)
        return redirect('/courses/') 
    course_code = request.args.get('course_code')
    course_name = request.args.get('course_name')
    college_code = request.args.get('college_code')
    colleges = get_college_codes()
    return render_template('editcourse.html', course_code=course_code, course_name=course_name, college_code=college_code, colleges=colleges)

@courses_bp.route('/delete_course/<string:course_code>', methods=['DELETE'])
def delete_student(course_code):
    if request.method == 'DELETE':
        remove_course(course_code)
        return jsonify({'success': True})