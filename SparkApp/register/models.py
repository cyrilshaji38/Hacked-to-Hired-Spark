from enum import unique
from SparkApp import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):   # Returns unique user id number from database.
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):   # Table in database with all registered user's information.
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    mobile = db.Column(db.String(length=10), nullable=True, unique=False)
    profile = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(length=60), nullable=False)
    acctype = db.Column(db.Integer(), nullable=False)
    students = db.relationship('Students', backref='my_teacher', lazy=True)

    @property
    def epassword(self):
        return self.epassword

    @epassword.setter
    def epassword(self, plain_text_password):   # Hash encodes password before saving it to database.
        self.password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):   # Compares attempted password with hash encoded password in database for user to login.
        return bcrypt.check_password_hash(self.password, attempted_password)


class Students(db.Model):   # Table in database that stores all students and their assigned teachers.
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=True, unique=True)
    teacher = db.Column(db.Integer(), db.ForeignKey('user.id'))   # Assigned teacher's unique user id number.
    
    def __repr__(self):
        return f'Students {self.username}'