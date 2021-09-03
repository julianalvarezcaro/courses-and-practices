from flask import Flask, make_response, request, redirect, render_template
from flask_bootstrap import Bootstrap, bootstrap_find_resource


app = Flask(__name__)

bootstrap = Bootstrap(app)

todos = ['Comprar pan', 'Comprar leche', 'Comprar lo demás']

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
    response.set_cookie('user_ip', user_ip)

    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos
    }

    return render_template('hello.html', **context)