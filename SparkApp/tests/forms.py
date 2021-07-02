from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Answers(FlaskForm):   # Form for the test paper page.
    style={'style': 'font-size: 20px'}
    style1={'style': 'font-size: 30px', 'readonly': True}
    a1 = StringField(validators=[DataRequired()],render_kw=style)
    a2 = StringField(validators=[DataRequired()],render_kw=style)
    a3 = StringField(validators=[DataRequired()],render_kw=style)
    a4 = StringField(validators=[DataRequired()],render_kw=style)
    a5 = StringField(validators=[DataRequired()],render_kw=style)
    a6 = StringField(validators=[DataRequired()],render_kw=style)
    ans_list = [[]]   # List of list since our ML function analyze_skill.py takes csv file as argument.
    submit = SubmitField(label='Submit',render_kw=style1)