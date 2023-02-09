from flask import Flask, send_from_directory, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/images/<path:filename>')
def get_image(filename):
    return send_from_directory('images', filename)


# @app.route('/css/custom.css')
# def css():
#     return render_template('../static/css')

@app.route('/signup')
def signup_handler():
    return render_template('signup.html')


@app.route('/login')
def login_handler():
    return render_template('login.html')


@app.route('/profile')
def profile_handler():
    return render_template('profile.html')


@app.route('/index')
def index_handler():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
