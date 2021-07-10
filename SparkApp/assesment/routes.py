from flask import render_template, redirect, url_for
from SparkApp.skills import analyze_skill
from SparkApp.assesment.forms import Answers
from SparkApp import app
from flask_login import current_user

@app.route("/assesment",methods = ['GET','POST'])
def assesment_page():
    if current_user.is_authenticated:
        form3 = Answers()   # Assesment page form.
        form3.ans_list = [[form3.a1.data,form3.a2.data,form3.a3.data,form3.a4.data,form3.a5.data,form3.a6.data]]   # Student's answers.
        if form3.validate_on_submit():
            prediction = analyze_skill.lacking_skill(form3.ans_list)   # ML function returns the skill that the student lacks based on test answers.
            if(prediction == "Critical thinking "):
                return redirect(url_for('critical_thinking_page'))   # Redirect user to page with game for improving critical thinking skills.
            else:
                return redirect(url_for('communication_page'))   # Redirect user to page with game for improving communication skills.
        return render_template('assesment/sample_assesment.html', form=form3)
    else:
        return redirect(url_for('login_page'))