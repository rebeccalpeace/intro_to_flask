from app import app
from flask import render_template


@app.route('/')
def index():
    user_info = {
        'username': 'rebeccap',
        'email': 'rpeace@gmail.com'
    }
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return render_template('index.html', user=user_info, colors=colors)


@app.route('/test')
def test():
    return 'This is a test'