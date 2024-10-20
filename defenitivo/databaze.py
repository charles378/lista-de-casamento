from peewee import *

db = SqliteDatabase('databas.db')

class BaseModel(Model):
    class Meta:
        databas = db

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


db.connect()
db.create_tables([Casal, Convidado, Presente])