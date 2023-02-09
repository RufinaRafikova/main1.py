from flask import Flask, send_from_directory, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('profile.html')


@app.route('/images/<path:filename>')
def get_image(filename):
    return send_from_directory('images', filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)