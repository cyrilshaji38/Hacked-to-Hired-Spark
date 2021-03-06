from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


class Answers(FlaskForm):   # Form for the assesment page.
    style1={'style': 'font-size:10px'}
    style2={'style': 'font-size: 20px'}
    a1 = SelectField('Answer', choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)],render_kw=style1)
    a2 = SelectField('Answer', choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)],render_kw=style1)
    a3 = SelectField('Answer', choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)],render_kw=style1)
    a4 = SelectField('Answer', choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)],render_kw=style1)
    a5 = SelectField('Answer', choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)],render_kw=style1)
    a6 = SelectField('Answer', choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)],render_kw=style1)
    ans_list = [[]]   # List of list since our ML function analyze_skill.py takes csv file as argument.
    submit = SubmitField(label='Submit',render_kw=style2)