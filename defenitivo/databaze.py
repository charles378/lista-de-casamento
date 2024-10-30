# from peewee import *

# db = SqliteDatabase('meuBanco.db')

# class BaseModel(Model):
#     class Meta:
#         database = db

# class Casal(BaseModel):
#     nome = CharField()
#     senha = CharField()

# class Convidado(BaseModel):
#     nome = CharField()
#     telefone = CharField()
#     email = CharField(unique=True)
#     senha = CharField()

# class Presente(BaseModel):
#     nome = CharField()
#     marca = CharField()
#     cor = CharField()
#     compra = BooleanField(default=False)
#     convidado_id = IntegerField(null=True)

# db.connect()
# db.create_tables([Casal, Convidado, Presente])


from peewee import *

db = SqliteDatabase('meuBanco.db')

class BaseModel(Model):
    class Meta:
        database = db

class Casal(BaseModel):
    nome = CharField()
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
    compra = BooleanField(default=False)
    convidado_id = IntegerField(null=True)

db.connect()
db.create_tables([Casal, Convidado, Presente])
