import sqlite3

from flask import Flask, send_from_directory, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
db.create_all()

@app.route('/signUp', methods=['POST'])
def signup():
    email = request.form['email']
    name = request.form['name']
    surname = request.form['surname']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (email, name, surname, password) VALUES (?, ?, ?, ?)",
              (email, name, surname, password))
    conn.commit()
    conn.close()

    return 'User {} {} with email {} has been registered'.format(name, surname, email), render_template('profile.html')


@app.route('/')
def index():
    return render_template('signup.html')


@app.route('/images/<path:filename>')
def get_image(filename):
    return send_from_directory('images', filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
