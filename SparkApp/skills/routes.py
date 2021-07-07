from flask import render_template,redirect, url_for
from SparkApp import app
from flask_login import current_user


@app.route("/communication")
def communication_page():
    if current_user.is_authenticated:
        return render_template('skills/communication.html')
    else:
        return redirect(url_for('login_page'))

@app.route("/critical_thinking")
def critical_thinking_page():
    if current_user.is_authenticated:
        return render_template('skills/critical_thinking.html')
    else:
        return redirect(url_for('login_page'))