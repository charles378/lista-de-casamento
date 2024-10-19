from peewee import *

db = SqliteDatabase('clientes.db')

class Cliente(Model):
    nome = CharField()
    email = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([Cliente])
