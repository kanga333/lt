from flask import request, redirect, url_for, render_template, flash
from apps import app
from apps.services import get_home_message


@app.route('/')
def index():
    """
    ホーム画面表示
    :return:
    """
    message = get_home_message()
    return render_template('home.html', message=message)


@app.route('/login')
def login():
    """
    ログイン画面表示
    :return:
    """
    return render_template('login.html')
