from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddStudentForm(FlaskForm):   # Form adding new student.
    style={'style': 'font-size: 15px'}
    style1={'style': 'font-size: 15px', 'readonly': True}
    student_username = StringField(label='Student Username:', validators=[DataRequired()],render_kw=style)
    submit = SubmitField(label='ADD',render_kw=style1)