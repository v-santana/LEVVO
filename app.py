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
def userpickn():
    session.clear()
    #Inicia validação somente se for enviado um post
    return render_template('userpick.html')


#Login Cliente
@app.route("/login/cliente", methods=['POST','GET'])
def loginCliente():
    session.clear()
    session['TIPO_USUARIO'] = 'cliente'
    #Inicia validação somente se for enviado um post
    if request.method == "POST":
        email = request.form['email']
        user = lerClienteEmail(email)
        if user is not None:
            if email == user.email and request.form['password'] == user.senha:
                session['EMAIL'] = email
                session['NOME'] = user.nome
                return redirect("/home")
            else:
                return render_template('index.html',mensagem="Usuário ou senha incorretos. Por favor, tente outra vez.")
        else:
            return render_template('index.html',mensagem="Usuário ou senha incorretos. Por favor, tente outra vez.")
    return render_template('index.html', mensagem="")

# Login Entregador
@app.route("/login/entregador", methods=['POST','GET'])
def loginEntregador():
    session.clear()
    session['TIPO_USUARIO'] = 'entregador'
    #Inicia validação somente se for enviado um post
    if request.method == "POST":
        email = request.form['email']
        user = lerEntregadorEmail(email)
        if user is not None:
            if email == user.email and request.form['password'] == user.senha:
                session['EMAIL'] = email
                session['NOME'] = user.nome
                return redirect("/home")
            else:
                return render_template('index.html',mensagem="Usuário ou senha incorretos. Por favor, tente outra vez.")
   
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




@app.route("/cadastro/cliente", methods=['POST','GET'])
def cadastroCliente():
    session.clear()
    #Inicia validação somente se for enviado um post
    if request.method == "POST":
        criarCliente(request.form['nome'],request.form['email'],request.form['password'],request.form['telefone'])
    return render_template("cadastro_cliente.html")

@app.route("/cadastro/entregador", methods=['POST','GET'])
def cadastroEntregador():
    session.clear()
    #Inicia validação somente se for enviado um post
    if request.method == "POST":
        criarEntregador(request.form['nome'],request.form['email'],request.form['password'],request.form['telefone'],request.form['placa'].upper())
    return render_template("cadastro_entregador.html")




if __name__ == "__main__":
    app.run(debug=True)