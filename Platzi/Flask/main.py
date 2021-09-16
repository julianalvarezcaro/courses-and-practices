from flask import make_response, request, redirect, render_template, session, flash, url_for
from flask_login import login_required, current_user
import unittest

from app import create_app
from app.firestore_service import get_users, get_todos
from app.forms import LoginForm

app = create_app()

# todos = ['Comprar pan', 'Comprar leche', 'Comprar lo demás']

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/500')
def error_500():
    raise(Exception('500 error'))

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip

    return response

@app.route('/hello', methods=['GET'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username),
        'username': username
    }

    return render_template('hello.html', **context)