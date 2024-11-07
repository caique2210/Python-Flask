from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

# Página principal com layout atualizado
@app.route('/')
def home():
    current_time = datetime.now().strftime("%B %d, %Y %I:%M %p")
    minutes_ago = "27 minutes ago"  # Exemplo de tempo
    ip_address = request.remote_addr
    host_name = request.host
    
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/style.css">
        <title>Avaliação contínua</title>
    </head>
    <body>
        <div class="navbar">
            <ul>
                <li><a href="/">Avaliação contínua: Aula 050</a></li>
                <li><a href="/">Home</a></li>
            </ul>
        </div>
        
        <div class="content">
            <h1>Olá, {{ name }}!</h1>
            <p>A sua Instituição de ensino é: {{ institution }}</p>
            <p>Está cursando a disciplina de: {{ course }}</p>
            <p>O IP do computador remoto é: {{ ip_address }}</p>
            <p>O host da aplicação é: {{ host_name }}</p>
            
            <hr>
            <form action="/submit" method="post">
                <label for="name"><b>Informe o seu nome:</b></label><br>
                <input type="text" id="name" name="name" value="{{ name }}" required><br><br>
                
                <label for="surname"><b>Informe o seu sobrenome:</b></label><br>
                <input type="text" id="surname" name="surname" value="{{ surname }}" required><br><br>
                
                <label for="institution"><b>Informe a sua Instituição de ensino:</b></label><br>
                <input type="text" id="institution" name="institution" value="{{ institution }}" required><br><br>
                
                <label for="course"><b>Informe a sua disciplina:</b></label><br>
                <select id="course" name="course">
                    <option value="Desenvolvimento Web: Servidor" {% if course == "Desenvolvimento Web: Servidor" %}selected{% endif %}>Desenvolvimento Web: Servidor</option>
                    <option value="Sistemas de Informação" {% if course == "Sistemas de Informação" %}selected{% endif %}>Sistemas de Informação</option>
                    <option value="Redes de Computadores" {% if course == "Redes de Computadores" %}selected{% endif %}>Redes de Computadores</option>
                </select><br><br>
                
                <button type="submit">Submit</button>
            </form>
            
            <div class="datetime">
                <p>The local date and time is {{ current_time }}.</p>
                <p>That was {{ minutes_ago }}.</p>
            </div>
        </div>
    </body>
    </html>
    ''', name=request.cookies.get('name', 'estranho'),
       surname=request.cookies.get('surname', ''),
       institution=request.cookies.get('institution', ''),
       course=request.cookies.get('course', ''),
       ip_address=ip_address, host_name=host_name, current_time=current_time, minutes_ago=minutes_ago)


# Função para lidar com o formulário de envio
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get("name", "estranho")
    surname = request.form.get("surname", "")
    institution = request.form.get("institution", "")
    course = request.form.get("course", "")

    resp = app.make_response(render_template_string('''
    <h2>Bem-vindo, {{ name }} {{ surname }}!</h2>
    <p>Sua instituição: {{ institution }}</p>
    <p>Disciplina: {{ course }}</p>
    ''', name=name, surname=surname, institution=institution, course=course))
    
    resp.set_cookie('name', name)
    resp.set_cookie('surname', surname)
    resp.set_cookie('institution', institution)
    resp.set_cookie('course', course)
    
    return resp


if __name__ == '__main__':
    app.run(debug=True)
