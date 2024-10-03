# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, redirect, abort, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> Hello, World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1> Hello, {}</h1>'.format(name)

@app.route('/contextorequisicao')
def contexto_requisicao():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/codigostatusdiferente')
def codigo_status_diferente():
    return "Bad Request", 400

@app.route('/objetoresposta')
def objeto_resposta():
    return "<h1>This document carries a cookie!</h1>", 200, {'Set-Cookie': 'cookie_name=cookie_value'}

@app.route('/redirecionamento')
def redirecionamento():
    return redirect("https://ptb.ifsp.edu.br/")

@app.route('/abortar')
def abortar():
    abort(404)

