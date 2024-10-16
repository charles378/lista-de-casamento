from sqlalchemy import  create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session

Base = declarative_base()

class Convidado(Base):
    __tablename__ = "convidados"
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)
    telefone = Column('telefone', String)
    senha = Column('senha', String)

    def __init__(self, nome, telefone, senha):
        self.nome = nome
        self.telefone = telefone
        self.senha = senha

class item(Base):
    __tablename__ = "items"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)
    status = Column('status', String)
    dono = Column('dono', ForeignKey('convidado'))

    def __init__(self, nome, status, dono):
        self.nome = nome
        self.status = status
        self.dono = dono



Base.metadata.create_all(bind=db)

n= 'char'
t = '6556465'
s = 'dsfsd'

convi = Convidado(nome='char', telefone='char', senha='char')
session.add(convi)
session.commit()

lista_conv = session.query(Convidado).all()
print(lista_conv[1])