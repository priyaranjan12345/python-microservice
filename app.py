from werkzeug.utils import redirect
from flask import Flask, render_template, request, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "MySQL@1234"
app.config["MYSQL_DB"] = "student"

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student")
    data = cur.fetchall()
    print(data)
    cur.close()
    
    return render_template('index.html', students=data)

@app.route('/insert', methods = ['POST'])
def insert():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    print(name, email, phone)
    return redirect(url_for('index'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    return redirect(url_for('index'))

@app.route('/update', methods= ['POST', 'GET'])
def update():
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)