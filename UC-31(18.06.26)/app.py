from flask import Flask, session, redirect, url_for, request, render_template
from datetime import datetime

app = Flask(__name__)
app.secret_key = "turma-2024"

@app.route("/")
def index():
    recados = session.get("recados", [])
    return render_template("index.html", recados=recados)

@app.route("/recado", methods=["POST"])
def recado():
    nome = request.form.get("nome", "").strip()
    msg  = request.form.get("mensagem", "").strip()
    if nome and msg:
        recados = session.get("recados", [])
        recados.append({
            "nome": nome,
            "msg": msg,
            "hora": datetime.now().strftime("%H:%M")
        })
        session["recados"] = recados
        session.modified = True
    return redirect(url_for("index"))

@app.route("/apagar/<int:indice>")
def apagar(indice):
    recados = session.get("recados", [])
    if 0 <= indice < len(recados):
        recados.pop(indice)
        session["recados"] = recados
        session.modified = True
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)