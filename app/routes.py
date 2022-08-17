from curses.ascii import SI
from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, PostForm, LoginForm
from app.models import User, Post



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
        # Before we add the user to the database, check to see if there is already a user with username or email
        existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
        if existing_user:
            flash('A user with that username or email already exist.', 'danger')
            return redirect(url_for('signup'))
        new_user = User(email=email, username=username, password=password)
        flash(f"{new_user.username} has been created.", "success")
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = PostForm()
    if form.validate_on_submit():
        # get the data from the form
        title = form.title.data
        body = form.body.data
        # create a new instance of Post with the form data
        new_post = Post(title=title, body=body, user_id=1)
        # flas a message saying the post was created
        flash(f"{new_post.title} has been created.", 'secondary')
        # redirect back to home page
        return redirect(url_for('index'))

    return render_template('createpost.html', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)