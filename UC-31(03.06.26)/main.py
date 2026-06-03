@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/validação', methods=['POST'])
def cadastro():
    nome = request.form.get('nome', '').strip().title()
    email = request.form.get('email', '').strip().lower()
    senha = request.form.get('senha', '').strip().title()

    return f"""
    Nome: {nome}<br>
    Email: {email}<br>
    Cidade: {cidade}
    """

if __name__ == '__main__':
    app.run(debug=True)
    