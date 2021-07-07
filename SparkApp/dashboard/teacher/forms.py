from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddStudentForm(FlaskForm):   # Form adding new student.
    style={'style': 'font-size: 10px'}
    style1={'style': 'font-size: 10px', 'readonly': True}
    username = StringField(label='Student Username:', validators=[DataRequired()],render_kw=style)
    submit = SubmitField(label='ADD',render_kw=style1)