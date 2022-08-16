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


@app.route('/signup')
def signup():
    return render_template('signup.html')