from flask import *
from app.models.colleges import * 
from flask_wtf import *

colleges_bp = Blueprint('colleges', __name__)

@colleges_bp.route('/colleges/')
def colleges():
    colleges = get_colleges()
    return render_template('colleges.html', colleges=colleges)

@colleges_bp.route('/colleges/search', methods=['GET', 'POST'])
def search_college():
    colleges = []
    if request.method == 'POST':
        search_query = request.form.get('collegesearch')
        if search_query:
            colleges = find_colleges(search_query)
    return render_template('colleges.html', colleges=colleges, search_query=search_query)

@colleges_bp.route('/add_college', methods=['GET', 'POST'])
def add_college():
    if request.method == 'POST':
        college_code = request.form['college_code']
        college_name = request.form['college_name']
        if check(college_code):
            flash('College Code already exists!', 'error')
        elif len(college_code)> 20:
            flash('College Code too long!', 'error')
        else:
            insert_college(college_code, college_name)
            flash('College added successfully!', 'success')
            return redirect('/colleges') 
    return render_template('addcollege.html')

@colleges_bp.route('/edit_college', methods=['GET', 'POST'])
def edit_college():
    if request.method == 'POST':
        college_code = request.form.get('college_code')
        college_name = request.form.get('college_name')
        print(college_code, college_name)
        update_college(college_code, college_name)
        flash('College updated successfully!', 'success')
        return redirect('/colleges/') 
    college_code = request.args.get('college_code')
    college_name = request.args.get('college_name')
    return render_template('editcollege.html', college_code=college_code, college_name=college_name)

@colleges_bp.route('/delete_college/<string:college_code>', methods=['DELETE'])
def delete_college(college_code):
    if request.method == 'DELETE':
        remove_college(college_code)
        flash('College deleted successfully!', 'success')
        return jsonify({'success': True})