from peewee import *

db = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = db

class Cliente(BaseModel):
    nome = CharField()
    telefone = CharField()
    email = CharField()

class Produto(BaseModel):
    nome = CharField()
    marca = CharField()
    descricao = TextField()
    estoque = IntegerField(default=0)

db.connect()
db.create_tables([Cliente, Produto])
