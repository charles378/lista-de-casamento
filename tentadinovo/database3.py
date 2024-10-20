from peewee import *

db = SqliteDatabase('database3.db')

class BaseModel(Model):
    class Meta:
        database3 = db

class Casal(BaseModel):
    nome = CharField()
    telefone = CharField()
    email = CharField(unique=True)
    senha = CharField()

class Convidado(BaseModel):
    nome = CharField()
    telefone = CharField()
    email = CharField(unique=True)
    senha = CharField()

class Presente(BaseModel):
    nome = CharField()
    marca = CharField()
    cor = CharField()
    comprado = BooleanField(default=False)
    convidado_id = IntegerField(null=True)


class Produto(BaseModel):
    nome = CharField()
    marca = CharField()
    descricao = TextField()
    estoque = IntegerField(default=1)

db.connect()
db.create_tables([Casal, Convidado, Presente])