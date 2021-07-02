from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, RadioField
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
    style1={'style': 'font-size: 30px', 'readonly': True}
    username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()],render_kw=style)
    email = StringField(label='Email id:', validators=[Email(), DataRequired()],render_kw=style)
    password = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()],render_kw=style)
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password'), DataRequired()],render_kw=style)
    acctype = RadioField('Type of Account:', choices=[('1','Teacher'),('2','Student')],render_kw=style)
    submit = SubmitField(label='SignUp',render_kw=style1)