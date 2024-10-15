from peewee import *

db = SqliteDatabase('freelancers.db')


# essa e a tabela do usuario
class Usuario(Model):
    # o propio peewee jera o seu propio id mas se quer comlocar e primary_key+True
    nome = CharField()  # CharField() ele tem um limite de 255 caraquiteres
    telefone = CharField()
    email = CharField(unique=True)  # para nao repeti email na tablela
    senha = CharField()

    class Meta:  # para que o peewee saber qual banco de dado ele vai conversa
        database = db

# essa e a tablela do anuncio
class Anuncio(Model):  # backref='usuarios' e para criar a referenca
    usuario = ForeignKeyField(Usuario, backref='usuarios')  # para cliar areferencia com a tabela usuari que id
    titulo = CharField()  # CharField() ele tem um limite de 255 caraquiteres
    descricao = TextField()  # TextField() ele nao tem um limite de caraquiteres
    valor = DecimalField()  # vai reseber um numero decimal

    class Meta:
        database = db
        
class Item(Model):  # backref='usuarios' e para criar a referenca
    nome = CharField()  # para cliar areferencia com a tabela usuari que id
    #marca = CharField()  # CharField() ele tem um limite de 255 caraquiteres
   # descricao = TextField()  # TextField() ele nao tem um limite de caraquiteres
    #status = CharField()  # vai reseber um numero decimal

    class Meta:
        database = db
        