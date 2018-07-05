from flask import request, redirect, url_for, render_template, flash, session
from apps import app
from apps.services import get_home_message, register_lt
from apps.models import User


@app.route('/')
def index():
    """
    ホーム画面表示
    :return:
    """
    msg = get_home_message()
    message = msg['message']
    is_applied = msg['is_applied']
    users = User.query.order_by(User.id.desc()).all()
    for user in users:
        print(user.name)
        print(user.email)
    return render_template('home.html', message=message, is_applied=is_applied)


@app.route('/register', methods=['POST'])
def register():
    """
    LT登録
    :return:
    """
    try:
        lt_title = request.form['lt-title']
        lt_time = request.form['lt-time']
        # todo 登録処理
        register_lt(lt_title, lt_time)
        flash_message = f"参加登録しました"
        flash(flash_message)
        return redirect(url_for('index'))
    except KeyError:
        flash_message = f"登録失敗しました"
        flash(flash_message)
        return redirect(url_for('index'))


@app.route('/login')
def login():
    """
    ログイン画面表示
    :return:
    """
    return render_template('login.html')


@app.route('/logout')
def logout():
    # remove the username from session if exists
    session.pop('username', None)
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error/page_not_found.html')
