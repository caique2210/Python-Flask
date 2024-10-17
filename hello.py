from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

# Função para ajustar o horário de Brasília
def get_brasilia_time():
    now_utc = datetime.utcnow()  # Hora UTC
    brasilia_time = now_utc - timedelta(hours=3)  # Ajuste de 3 horas para o horário de Brasília
    return brasilia_time.strftime("%B %d, %Y %I:%M %p")

# Rota principal
@app.route('/')
def home():
    formatted_time = get_brasilia_time()
    return render_template('index.html', time=formatted_time)

# Rota de usuário sem Hello World
@app.route('/user/<name>')
def user(name):
    return render_template('index.html', user=name)

# Rota não encontrada sem Hello World
@app.route('/rotainexistente')
def not_found():
    return render_template('index.html', error=True)

if __name__ == '__main__':
    app.run()
