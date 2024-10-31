from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
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
                <h2>Hello, {{ name }}!</h2>
                <hr>
                <form method="post" action="/setname">
                    <label for="name"><b>What is your name?</b></label><br>
                    <input type="text" id="name" name="name" required style="width: 90%; height: 30px;"><br><br>
                    <button type="submit">Submit</button>
                </form>
            </div>
        </body>
    </html>
    ''', name="Caique")  # Nome padrão como "Caique"

@app.route('/setname', methods=['POST'])
def set_name():
    name = request.form['name']
    return render_template_string('''
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
                <h2>Hello, {{ name }}!</h2>
                <hr>
                <form method="post" action="/setname">
                    <label for="name"><b>What is your name?</b></label><br>
                    <input type="text" id="name" name="name" required style="width: 90%; height: 30px;"><br><br>
                    <button type="submit">Submit</button>
                </form>
            </div>
        </body>
    </html>
    ''', name=name)

if __name__ == '__main__':
    app.run(debug=True)

