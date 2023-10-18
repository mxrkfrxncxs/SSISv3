from flask import *
from app.models.courses import * 

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses/')
def courses():
    courses = get_courses()
    return render_template('courses.html', courses=courses)

@courses_bp.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_code = request.form['course_code']
        course_name = request.form['course_name']
        college_code = request.form['college_code']
        insert_course(course_code, course_name, college_code)
        return redirect('/courses') 
    return render_template('addcourse.html')