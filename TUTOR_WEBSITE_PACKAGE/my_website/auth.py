from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout<p/>"

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        fullname = request.form.get('fullname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) <= 5:
            flash('Email address must be greater than 5 characters', category='error')
        elif len(email) > 254:
            flash('Email address must be less than 255 characters', category='error')
        elif len(fullname) > 70:
            flash('Fullname must be less than 70 characters', category='error')
        elif password1 != password2:
            flash("Passwords do not match", category='error')
        elif len(password1) < 8:
            flash("Password must be a minimum of 8 characters", category='error')
        else: 
            flash('You have created an account', category= 'success')
    return render_template("sign_up.html")