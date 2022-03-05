from flask import Flask, jsonify, redirect, render_template
app = Flask(__name__)




@app.route("/")
def index():
    return redirect('/login')

@app.route("/login")
def login():
    return "<h1>login<h1>"


@app.route("/cadastro/")
def cadastro():
    return "<h1>cadastro (apenas para testar link):<br> <a href='entregador'>Entregador</a><br> <a href='cliente'>Cliente</a><br> <a href='entrega'>Entrega</a><h1>"

@app.route("/cadastro/<entidade>")
def cadastroEntidade(entidade):
    return f"<h1>{entidade}<h1>"




if __name__ == "__main__":
    app.run(debug=True)