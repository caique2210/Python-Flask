from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    name = "strange"  # Nome padrão
    if request.method == 'POST':
        name = request.form.get('name', 'strange')

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/style.css">
        <title>Flasky</title>
    </head>
    <body>
        <div class="navbar">
            <ul>
                <li><a href="/">Flasky</a></li>
                <li><a href="/">Home</a></li>
            </ul>
        </div>
        
        <div class="content">
            <h1>Hello, {{ name }}!</h1>
            <p>Pleased to meet you!</p>
            <hr>
            <form method="post">
                <label for="name"><b>What is your name?</b></label><br>
                <input type="text" id="name" name="name" required><br><br>
                <button type="submit">Submit</button>
            </form>
        </div>
    </body>
    </html>
    ''', name=name)

if __name__ == '__main__':
    app.run(debug=True)
