from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from SparkApp.register.models import User


class SignupForm(FlaskForm):   # Form for register page.
    def validate_username(self, username_to_check):   # To ensure username is not used.
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email(self, email_address_to_check):   # To ensure email id entered is not already registered.
        email = User.query.filter_by(email=email_address_to_check.data).first()
        if email:
            raise ValidationError('Email Address already exists! Please try a different email address')

    style={'style': 'font-size: 20px'}
    style1={'style': 'font-size: 20px', 'readonly': True}
    style3={'style': 'height: 30px'}
    username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()],render_kw=style)
    email = StringField(label='Email id:', validators=[Email(), DataRequired()],render_kw=style)
    mobile = StringField(label='Mobile No:', validators=[Length(min=0, max=10)],render_kw=style)
    profile = FileField('Upload Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    password = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()],render_kw=style)
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password'), DataRequired()],render_kw=style)
    acctype = SelectField('Type of Account:', choices=[('2','Student'),('1','Teacher')],render_kw=style3)
    submit = SubmitField(label='SignUp',render_kw=style1)