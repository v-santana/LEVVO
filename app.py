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

@app.route("/userpick")
def userpickn():
    session.clear()
    #Inicia validação somente se for enviado um post
    return render_template('userpick.html')


#Index Login
@app.route("/login/cliente", methods=['POST','GET'])
def loginCliente():
    session.clear()
    #Inicia validação somente se for enviado um post
    if request.method == "POST":
        email = request.form['email']
        user = lerClienteEmail(email)
        print(user)
        if email == user.email and request.form['password'] == user.senha:
            session['EMAIL'] = email
            session['NOME'] = user.nome
            return redirect("/home")
        else:
            return render_template('index.html',mensagem="Usuário ou senha incorretos. Por favor, tente outra vez.")
    return render_template('index.html', mensagem="")


#Home (somente logado)
@app.route("/home")
def home():
    #Se estiver logado exibe mensagem e nome de usuário, senão exibe acesso não permitido
    if 'NOME' in session:
        return render_template('home.html',mensagem=f"Bem vindo ao Levvo, {session['NOME']}")
    else:
        return render_template('home.html',mensagem="Acesso não permitido")



@app.route("/cadastro/")
def cadastro():
    return "<h1>cadastro (apenas para testar link):<br> <a href='entregador'>Entregador</a><br> <a href='cliente'>Cliente</a><br> <a href='entrega'>Entrega</a><h1>"

@app.route("/cadastro/<entidade>")
def cadastroEntidade(entidade):
    return f"<h1>{entidade}<h1>"




if __name__ == "__main__":
    app.run(debug=True)