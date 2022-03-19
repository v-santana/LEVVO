from flask import Flask, make_response, request, render_template, redirect, send_from_directory, session
from db_levvo import lerClienteEmail
from db_levvo import *
# Cria o objeto principal do Flask.
app = Flask(__name__)

# Configura chave secreta para utilização da session no flask (Poderiam ser utilizados cookies para efetuar o login porém optei pela session)
SECRET_KEY = 'LEVAMOSATEVOCE!@#$@!(%&ssaas'
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def index():
    return redirect('/login')

@app.route("/login")
def login():
    session.clear()
    #Inicia validação somente se for enviado um post
    return render_template('userpick.html')


#Login Cliente
@app.route("/login/cliente", methods=['POST','GET'])
def loginCliente():
    session.clear()
    #Inicia validação somente se for enviado um post
    if request.method == "POST":
        email = request.form['email']
        user = lerClienteEmail(email)
        if email == user.email and request.form['password'] == user.senha:
            session['EMAIL'] = email
            session['NOME'] = user.nome
            session['TIPO_USUARIO'] = 'CLIENTE'
            return redirect("/home")
        else:
            return render_template('index.html',mensagem="Usuário ou senha incorretos. Por favor, tente outra vez.")
    return render_template('index.html', mensagem="")

# Login Entregador
@app.route("/login/entregador", methods=['POST','GET'])
def loginEntregador():
    session.clear()
    #Inicia validação somente se for enviado um post
    if request.method == "POST":
        email = request.form['email']
        user = lerEntregadorEmail(email)
        if email == user.email and request.form['password'] == user.senha:
            session['EMAIL'] = email
            session['NOME'] = user.nome
            session['TIPO_USUARIO'] = 'ENTREGADOR'
            return redirect("/home")
        else:
            return render_template('index.html',mensagem="Usuário ou senha incorretos. Por favor, tente outra vez.")
    return render_template('index.html', mensagem="")

#Home (somente logado)
@app.route("/home")
def home():
    #Se estiver logado exibe mensagem e nome de usuário, senão exibe acesso não permitido
    if 'NOME' in session:
        return render_template('home.html',mensagem=f"Bem vindo ao Levvo, {session['NOME'].split(' ')[0]}")
    else:
        return render_template('home.html',mensagem="Acesso não permitido")




@app.route("/cadastro/<entidade>")
def cadastroEntidade(entidade):
    return f"<h1>{entidade}<h1>"




if __name__ == "__main__":
    app.run(debug=True)