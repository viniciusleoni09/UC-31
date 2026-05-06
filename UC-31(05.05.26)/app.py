from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    nome = "gaby"
    return render_template('contato.html', title='pagina inicial', nome=nome)

if __name__ == '__main__':
    app.run()


