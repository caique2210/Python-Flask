from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1><b>Avaliação contínua: Aula 030</b></h1>
    <ul>
        <li><a href="/"><b>Home</b></a></li>
        <li><a href="/user/Caique%20Salmaso/PT3026663/IFSP"><b>Identificação</b></a></li>
        <li><a href="/contextorequisicao"><b>Contexto de Requisição</b></a></li>
    </ul>
    '''

@app.route('/user/<nome>/<prontuario>/<instituicao>')
def identificacao(nome, prontuario, instituicao):
    return f'''
    <h1><b>Avaliação contínua: Aula 030</b></h1>
    <h2><b>Aluno:</b> {nome}</h2>
    <h2><b>Prontuário:</b> {prontuario}</h2>
    <h2><b>Instituição:</b> {instituicao}</h2>
    <br>
    <a href="/"><b>Voltar</b></a>
    '''

@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-Agent')
    remote_ip = request.remote_addr
    host = request.host
    return f'''
    <h1><b>Avaliação contínua: Aula 030</b></h1>
    <h2><b>Seu navegador é:</b> {user_agent}</h2>
    <h2><b>O IP do computador remoto é:</b> {remote_ip}</h2>
    <h2><b>O host da aplicação é:</b> {host}</h2>
    <br>
    <a href="/"><b>Voltar</b></a>
    '''

if __name__ == '__main__':
    app.run(debug=True)
