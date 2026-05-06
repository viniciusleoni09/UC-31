from flask import Flask, render_template_string

app = Flask(__name__)

# Questão 03
@app.route('/arearestrita/<int:id>')
def arearestrita(id):
    if id == 1:
        
        img_url = "https://cdn-icons-png.flaticon.com/512/61/61457.png"
        legenda = "Cadeado Fechado"
    elif id == 2:
        
        img_url = "https://cdn-icons-png.flaticon.com/512/61/61456.png"
        legenda = "Cadeado Aberto"
    else:
        img_url = ""
        legenda = "ID inválido"
    return render_template_string("""
        <h1>{{ legenda }}</h1>
        {% if img_url %}
            <img src="{{ img_url }}" width="150">
        {% else %}
            <p>ID deve ser 1 ou 2.</p>
        {% endif %}
    """, img_url=img_url, legenda=legenda)

# Questão 04
@app.route('/operacao/<tipo>/<int:op1>/<int:op2>')
def operacao(tipo, op1, op2):
    if tipo == "sum":
        resultado = op1 + op2
        operacao_nome = "Soma"
    elif tipo == "sub":
        resultado = op1 - op2
        operacao_nome = "Subtração"
    elif tipo == "mult":
        resultado = op1 * op2
        operacao_nome = "Multiplicação"
    elif tipo == "div":
        if op2 == 0:
            return "Erro: Divisão por zero não é permitida."
        resultado = op1 / op2
        operacao_nome = "Divisão"
    else:
        return "Operação inválida. Use sum, sub, mult ou div."
    return f"<h1>{operacao_nome}: {resultado}</h1>"

if __name__ == '__main__':
    app.run(debug=True)