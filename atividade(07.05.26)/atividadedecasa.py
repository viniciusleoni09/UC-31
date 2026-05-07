from flask import Flask, render_template

app = Flask(__name__)

sabores = {
    "calabresa": {
        "nome": "Calabresa",
        "imagem": "https://www.receiteria.com.br/wp-content/uploads/receitas-de-pizza-de-calabresa-0.jpg"
    },
    "margherita": {
        "nome": "Margherita",
        "imagem": "https://www.receiteria.com.br/wp-content/uploads/receitas-de-pizza-margherita-0.jpg"
    },
    "frango": {
        "nome": "Frango",
        "imagem": "https://www.receiteria.com.br/wp-content/uploads/receitas-de-pizza-de-frango-0.jpg"
    }
}

@app.route('/pizzaria/<sabor>')
def pizzaria(sabor):
    if sabor in sabores:
        return render_template(f"{sabor}.html", nome=sabores[sabor]["nome"], imagem=sabores[sabor]["imagem"])
    else:
        return render_template("indisponivel.html", sabor=sabor), 404

if __name__ == '__main__':
    app.run(debug=True)