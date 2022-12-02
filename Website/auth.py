from flask import Blueprint ,url_for,redirect,render_template,request,flash
from .model import User
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,login_required,logout_user,current_user

auth=Blueprint("auth",__name__)

@auth.route('/')
def home():
    return render_template('login.html')

@auth.route('/', methods=['POST'])
def login():
    email=request.form.get('email')
    password1=request.form.get('password1')
    user=User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password,password1):
            flash("logged in successfull!",category="success")
            login_user(user,remember=True)
            return redirect(url_for("views.home"))
            #return render_template('home.html',user=current_user)
        else:
            flash("incorect password!",category="error")
    else:
        return render_template('login.html')

    return render_template('login.html')


@auth.route('/register')
def register():
    return render_template('register.html')

@auth.route('/register', methods=['POST'])
def userRegistration():
    first_name=request.form.get('firstname')
    last_name=request.form.get('lastname')
    identity=request.form.get('identity')
    gendar=request.form.get('gender')
    email=request.form.get('email')
    tel=request.form.get('tel')
    type=request.form.get('type')
    password1=request.form.get('password1')
    password2=request.form.get('password2')

    user=User.query.filter_by(email=email).first()
    if user:
        flash("invalid email",category="error")
    elif len(email) <4:
        flash("invalid email",category="error")
    elif len(first_name)<2:
        flash("must not be empty",category="error")
    elif password1 != password2:
        flash("password does not match",category="error")
    else:
        new_user=User(first_name=first_name,last_name=last_name,email=email,gender=gendar,identity=identity
        ,tel=tel,type=type,password=generate_password_hash(password1,method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash("Account created",category="success")
        return render_template('login.html')
        
    return render_template('register.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('login.html')