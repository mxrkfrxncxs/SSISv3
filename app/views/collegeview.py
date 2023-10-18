from flask import *
from app.models.colleges import * 
from flask_wtf import *

colleges_bp = Blueprint('colleges', __name__)

@colleges_bp.route('/colleges/')
def colleges():
    colleges = get_colleges()
    return render_template('colleges.html', colleges=colleges)


@colleges_bp.route('/add_college', methods=['GET', 'POST'])
def add_college():
    if request.method == 'POST':
        college_code = request.form['college_code']
        college_name = request.form['college_name']
        insert_college(college_code, college_name)
        return redirect('/colleges') 
    return render_template('addcollege.html')