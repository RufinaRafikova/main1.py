import sqlite3

from flask import Flask, redirect, send_from_directory, render_template, request, url_for
from werkzeug.exceptions import abort

app = Flask(__name__)

# подключение к базе данных
conn = sqlite3.connect("users.db")
cursor = conn.cursor()


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # retrieve the entered email and password
        email = request.form['email']
        password = request.form['password']

        # check if the email and password match with the existing records
        if email == "user@example.com" and password == "secret":
            # redirect to profile.html if the credentials are correct
            return redirect(url_for("profile"))
        else:
            # show an error message if the credentials are incorrect
            error = "Incorrect email or password"
            return render_template("login.html", error=error)
    return render_template("login.html")


# сохранение изменений
conn.commit()

# закрытие подключения
conn.close()


@app.route('/images/<path:filename>')
def get_image(filename):
    return send_from_directory('images', filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
