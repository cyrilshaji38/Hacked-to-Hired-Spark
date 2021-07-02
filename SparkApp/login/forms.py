from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class SigninForm(FlaskForm):   # Form for login page.
    style={'style': 'font-size: 20px'}
    style1={'style': 'font-size: 30px', 'readonly': True}
    username = StringField(label='Username:', validators=[DataRequired()],render_kw=style)
    password = PasswordField(label='Password:', validators=[DataRequired()],render_kw=style)
    submit = SubmitField(label='Sign in',render_kw=style1)