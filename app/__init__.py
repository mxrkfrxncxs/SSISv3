from flask import Flask, render_template
from flask_mysql_connector import MySQL
from flask_bootstrap import Bootstrap
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL
from flask_wtf.csrf import CSRFProtect

mysql = MySQL()
bootstrap = Bootstrap()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_HOST=DB_HOST,
        #BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )
    bootstrap.init_app(app)
    mysql.init_app(app)
    CSRFProtect(app)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/students/')
    def students():
        # Connect to the MySQL database
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        # Perform a query to retrieve data
        query = "SELECT * FROM student"
        cursor.execute(query)
        students = cursor.fetchall()

        # Close the cursor and the database connection
        cursor.close()

        return render_template('students.html', students=students)
    
    @app.route('/courses/')
    def courses():
        return render_template('courses.html')
    
    @app.route('/colleges/')
    def colleges():
        return render_template('colleges.html')
    
    return app