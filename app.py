from crypt import methods
import requests
import json
from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
from xmlrpc.client import ResponseError
from flask import Flask, render_template, request, make_response, redirect, url_for
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from flask_bootstrap import Bootstrap

# for ass4
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# from .models import User


app = Flask(__name__)
# creating an API object

app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
Bootstrap(app)

api=Api(app)


app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin@localhost/tarot'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db=SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class Data(db.Model):
        __tablename__="names"  
        id=db.Column(db.Integer, primary_key=True)
        sign=db.Column(db.String(120))
        # date=db.Column(db.Date)

        description = db.Column(db.String(600))
        date_range = db.Column(db.String(600))

        lucky_number = db.Column(db.Integer)
        compatibility = db.Column(db.String(120))

        authenticated = db.Column(db.Boolean, default=False)

        def is_active(self):
                """True, as all users are active."""
                return True

        def get_id(self):
                """Return the email address to satisfy Flask-Login's requirements."""
                return self.username

        def is_authenticated(self):
                """Return True if the user is authenticated."""
                return self.authenticated

        def is_anonymous(self):
                """False, as anonymous users aren't supported."""
                return False


    
        def __init__(self, sign, description,date_range, lucky_number,compatibility):
                self.sign=sign
                # self.date=date
                self.description=description
                self.date_range=date_range
                self.lucky_number=lucky_number
                self.compatibility=compatibility
                

        # {'date_range': 'Sep 23 - Oct 22', 'current_date': 'October 16, 2022',
        # 'description': "Still shopping? Still getting crazy with the charge cards? Well, it might be time to stop that nonsense 
        # -- just for a day or two. If you're not sure you can manage it, hire a bodyguard. A charge-guard, so to speak.", 
        #  'compatibility': 'Pisces', 'mood': 'Productive', 'color': 'Silver', 'lucky_number': '81', 'lucky_time': '6pm'}
                    


class User(UserMixin, db.Model):
    __tablename__="u_h"  
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(600))



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])





@app.route('/', methods=['GET', 'POST'])
def index():

        if request.method=='POST':

            sign=request.form.get('sign')
            # date=request.form.get('date_type')
            print(sign)
            

            url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
            querystring = {"sign": sign,"day":"today"}

            headers = {
                "X-RapidAPI-Key": "0459c6f8a8mshc3aaf65a2576dc5p19c1b1jsndc488967f473",
                "X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com"
            }

            response = requests.request("POST", url, headers=headers, params=querystring)

            # {'date_range': 'Sep 23 - Oct 22', 'current_date': 'October 16, 2022',
            # 'description': "Still shopping? Still getting crazy with the charge cards? Well, it might be time to stop that nonsense 
            # -- just for a day or two. If you're not sure you can manage it, hire a bodyguard. A charge-guard, so to speak.", 
            #  'compatibility': 'Pisces', 'mood': 'Productive', 'color': 'Silver', 'lucky_number': '81', 'lucky_time': '6pm'}
            
            date_range = response.json()["date_range"]
            description = response.json()["description"]
            lucky_number = response.json()["lucky_number"]
            compatibility = response.json()["compatibility"]

        
            data=Data(sign, description, date_range,lucky_number,compatibility)
            db.session.add(data)
            db.session.commit()

            print(data)


            return render_template("dashboard.html", sign=sign, description=description, 
                    date_range=date_range, lucky_number=lucky_number,compatibility=compatibility)

        
        return render_template('index.html')
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()
        if user:
            
            if check_password_hash(user.password, form.password.data):
                
                user.authenticated = True

                login_user(user, remember=form.remember.data)
                return redirect(url_for('main'))

        return '<h1>Invalid username or password</h1>'
        
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)


@app.route('/signup',methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():

      
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1> <p><a href="http://127.0.0.1:5000">Back to Main Page)</a></p></h1>'
        
        # return '<h1>' + form.username.data + ' ' + form.email.data + form.password.data + '</h1>'

    return render_template('signup.html', form=form)



@app.route('/main')
@login_required
def main():
    return render_template('main.html', name = current_user.username)

@app.route('/logout')

def logout():

    # user = current_user
    # user.authenticated = False

    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/unconfirmed')
@login_required
def unconfirmed():
    if not current_user.username:
        return redirect('/')
    return render_template('login.html')





with app.app_context():
    db.create_all()        

if __name__ == '__main__':
    db.create_all()
    app.debug=True
    app.run()