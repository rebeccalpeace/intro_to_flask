from curses.ascii import SI
from app import app
from flask import render_template
from app.forms import SignUpForm
from app.models import User



@app.route('/')
def index():
    user_info = {
        'username': 'rebeccap',
        'email': 'rpeace@gmail.com'
    }
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return render_template('index.html', user=user_info, colors=colors)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    # if the form is submitted and all the data is valid
    if form.validate_on_submit():
        print('Form has been validated!')
        email = form.email.data
        username = form.username.data
        password = form.password.data
        new_user = User(email=email, username=username, password=password)
        print(f"{new_user.username} hass been created.")
    return render_template('signup.html', form=form)