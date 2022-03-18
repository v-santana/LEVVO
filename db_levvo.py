import email
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, insert, delete
import pymysql
from sqlalchemy.ext.declarative import declarative_base
   
#base para criação de engine
Base = declarative_base()
   
#Conectanto e criando a máquina para utilizar o sql alchemy
engine = create_engine('mysql+pymysql://b74s0om2wm3diiii:kaucriymr5qrj7oa@uyu7j8yohcwo35j3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/vxaohtuqm8mtxuxc')
Session = sessionmaker(bind=engine)
db_session = Session()
   
class Cliente(Base):
   __tablename__ = 'tb_cliente'
   id = Column(Integer, primary_key=True)
   nome = Column(String(100))
   email = Column(String(50))
   senha = Column(String(50))
   telefone = Column(String(20))
   
class Entregador(Base):
   __tablename__ = 'tb_entregador'
   id = Column(Integer, primary_key=True)
   nome = Column(String(100))
   email = Column(String(50))
   senha = Column(String(50))
   telefone = Column(String(20))
   placa = Column(String(10))
   
class Entrega(Base):
   __tablename__ = 'tb_entrega'
   id = Column(Integer, primary_key=True)
   descricao = Column(String(200))
   id_endereco_coleta = Column(Integer)
   id_endereco_final = Column(Integer)
   

class Endereco(Base):
   __tablename__ = 'tb_endereco'
   id = Column(Integer, primary_key=True)
   rua = Column(String(200))
   numero = Column(Integer)
   complemento = Column(String(200))
   cep = Column(String(10))
   id_bairro = Column(Integer)
   

#Realiza a criação das tabelas solicitadas
Base.metadata.create_all(engine)
   
############ CRUD #################

############ CLIENTE #################
def criarCliente(nome,email,senha,telefone):
   cliente = Cliente(nome = nome,email = email,senha = senha,telefone = telefone)
   db_session.add(cliente)
   db_session.commit()
   return cliente

def lerCliente(id):
   for cliente in db_session.query(Cliente).filter_by(id=id):
      return cliente

def lerClienteEmail(email):
   for cliente in db_session.query(Cliente).filter_by(email=email):
      return cliente


def editarNomeCliente(id,novoNome):
   cliente = db_session.query(Cliente).filter(Cliente.id == id).one()
   cliente.nome = novoNome
   db_session.commit()
   return cliente


def editarEmailCliente(id,novoEmail):
   cliente = db_session.query(Cliente).filter(Cliente.id == id).one()
   cliente.email = novoEmail
   db_session.commit()
   return cliente

def editarSenhaCliente(id,novaSenha):
   cliente = db_session.query(Cliente).filter(Cliente.id == id).one()
   cliente.senha = novaSenha
   db_session.commit()
   return cliente

def editarTelefoneCliente(id,novoTelefone):
   cliente = db_session.query(Cliente).filter(Cliente.id == id).one()
   cliente.telefone = novoTelefone
   db_session.commit()
   return cliente

############ ENTREGADOR #################

def criarEntregador(nome,email,senha,telefone, placa):
   entregador = Entregador(nome = nome,email = email,senha = senha,telefone = telefone,placa = placa)
   db_session.add(entregador)
   db_session.commit()
   return entregador

def lerEntregador(id):
   for entregador in db_session.query(Entregador).filter_by(id=id):
      return entregador

def editarNomeEntregador(id,novoNome):
   entregador = db_session.query(Entregador).filter(Entregador.id == id).one()
   entregador.nome = novoNome
   db_session.commit()
   return entregador

def editarEmailEntregador(id,novoEmail):
   entregador = db_session.query(Entregador).filter(Entregador.id == id).one()
   entregador.email = novoEmail
   db_session.commit()
   return entregador


def editarSenhaEntregador(id,novaSenha):
   entregador = db_session.query(Entregador).filter(Entregador.id == id).one()
   entregador.senha = novaSenha
   db_session.commit()
   return entregador

def editarTelefoneEntregador(id,novoTelefone):
   entregador = db_session.query(Entregador).filter(Entregador.id == id).one()
   entregador.telefone = novoTelefone
   db_session.commit()
   return entregador


############ ENTREGA #################

def criarEntrega(descricao,id_endereco_coleta,id_endereco_final):
   entrega = Entrega(descricao = descricao,id_endereco_coleta = id_endereco_coleta,id_endereco_final = id_endereco_final)
   db_session.add(entrega)
   db_session.commit()
   return entrega

def lerEntrega(id):
   for entrega in db_session.query(Entrega).filter_by(id=id):
      return entrega

def editarDescricaoEntrega(id,novaDescricao):
   entrega = db_session.query(Entrega).filter(Entrega.id == id).one()
   entrega.descricao = novaDescricao
   db_session.commit()
   return entrega

def editarEnderecoColetaEntrega(id,numero,complemento,cep,id_bairro):
   entrega = db_session.query(Entrega).filter(Entrega.id == id).one()
   novoEndereco = criarEndereco(numero,complemento,cep,id_bairro)
   entrega.id_endereco_coleta = novoEndereco.id
   db_session.commit()
   return entrega

def editarEnderecoFinalEntrega(id,numero,complemento,cep,id_bairro):
   entrega = db_session.query(Entrega).filter(Entrega.id == id).one()
   novoEndereco = criarEndereco(numero,complemento,cep,id_bairro)
   entrega.id_endereco_entrega = novoEndereco.id
   db_session.commit()
   return entrega

############ ENDERECO #################

def criarEndereco(rua,numero,complemento,cep,id_bairro):
   endereco = Endereco(rua = rua,numero = numero,complemento = complemento,cep = cep,id_bairro = id_bairro)
   db_session.add(endereco)
   db_session.commit()
   return endereco

def lerEndereco(id):
   for endereco in db_session.query(Endereco).filter_by(id=id):
      return endereco





#Insere dados do usuário na tabela usuários
# cliente = Cliente(nome="Vinicius",email="vinicius@gmail.com",senha="vinicius123",telefone="11991677867")
 
# db_session.add(cliente)
# db_session.commit()
 
#novoCliente = criarCliente("Gabriel Bastos","bastosgabriel312@gmail.com",123456, "11991111111")
#print(novoCliente)
#Select de dados dados