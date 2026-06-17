from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

# Chave secreta para assinar os dados da session
app.secret_key = "chave_super_secreta_2025"

# Credenciais fixas de usuários
USUARIOS = {
    "admin": {"senha": "admin123", "nome": "Administrador"},
    "aluno": {"senha": "senha456", "nome": "Maria Silva"},
    "professor": {"senha": "prof789", "nome": "Prof. João Santos"},
}


# ── Página Inicial ─────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


# ── Login ──────────────────────────────────────────────────────────────────────
@app.route("/login", methods=["GET", "POST"])
def login():
    # Se já estiver logado, vai direto ao dashboard
    if "usuario" in session:
        return redirect(url_for("dashboard"))

    erro = None

    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        senha = request.form.get("senha", "")

        if usuario in USUARIOS and USUARIOS[usuario]["senha"] == senha:
            # Login válido: salva dados na session
            session["usuario"] = usuario
            session["nome"] = USUARIOS[usuario]["nome"]
            return redirect(url_for("dashboard"))
        else:
            erro = "Usuário ou senha incorretos. Tente novamente."

    return render_template("login.html", erro=erro)


# ── Área Restrita ──────────────────────────────────────────────────────────────
@app.route("/dashboard")
def dashboard():
    # Protege a rota: redireciona se não estiver autenticado
    if "usuario" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html", nome=session["nome"])


# ── Logout ─────────────────────────────────────────────────────────────────────
@app.route("/logout")
def logout():
    session.clear()  # Encerra a sessão completamente
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)