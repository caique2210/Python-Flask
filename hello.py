from flask import Flask, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%B %d, %Y %I:%M %p")
    return '''
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="/static/style.css">
            <title>Avaliação contínua</title>
        </head>
        <body>
            <div class="navbar">
                <ul>
                    <li><a href="/">Avaliação contínua: Aula 040</a></li>
                    <li><a href="/">Home</a></li>
                    <li><a href="/identificacao">Identificação</a></li>
                    <li><a href="/contextorequisicao/Caique%20Salmaso">Contexto de requisição</a></li>
                </ul>
            </div>
            <div class="content">
                <h2>Dados da última utilização:</h2>
                <hr>
                <p>The local date and time is {}<br>
                That was in a few seconds.</p>
            </div>
        </body>
    </html>
    '''.format(current_time)

@app.route('/identificacao')
def identificacao():
    return redirect(url_for('user', name="Caique Salmaso", prontuario="PT3026663", instituicao="IFSP PIRITUBA"))

@app.route('/user/<name>/<prontuario>/<instituicao>')
def user(name, prontuario, instituicao):
    return '''
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="/static/style.css">
            <title>Identificação</title>
        </head>
        <body>
            <div class="navbar">
                <ul>
                    <li><a href="/">Avaliação contínua: Aula 040</a></li>
                    <li><a href="/">Home</a></li>
                    <li><a href="/identificacao">Identificação</a></li>
                    <li><a href="/contextorequisicao/Caique%20Salmaso">Contexto de requisição</a></li>
                </ul>
            </div>
            <div class="content">
                <h2 style="font-weight: normal;">Olá, {}!</h2>
                <hr>
                <h2 style="font-weight: normal;">Prontuário: {}</h2>
                <h2 style="font-weight: normal;">Instituição: {}</h2>
            </div>
        </body>
    </html>
    '''.format(name, prontuario, instituicao)

@app.route('/contextorequisicao/<name>')
def context(name):
    user_agent = request.headers.get('User-Agent')
    remote_ip = request.remote_addr
    host = request.host

    return '''
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="/static/style.css">
            <title>Contexto de Requisição</title>
        </head>
        <body>
            <div class="navbar">
                <ul>
                    <li><a href="/">Avaliação contínua: Aula 040</a></li>
                    <li><a href="/">Home</a></li>
                    <li><a href="/identificacao">Identificação</a></li>
                    <li><a href="/contextorequisicao/Caique%20Salmaso">Contexto de requisição</a></li>
                </ul>
            </div>
            <div class="content">
                <h2 style="font-weight: normal;">Olá, {}!</h2>
                <hr>
                <p>Seu navegador é: {}</p>
                <p>O IP do computador remoto é: {}</p>
                <p>O host da aplicação é: {}</p>
            </div>
        </body>
    </html>
    '''.format(name, user_agent, remote_ip, host)

if __name__ == '__main__':
    app.run(debug=True)

