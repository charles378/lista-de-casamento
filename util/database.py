# from peewee import *

# db = SqliteDatabase('presentes.db')

# class Presente(Model):
#     nome = CharField()
#     comprado = BooleanField(default=False)

#     class Meta:
#         database = db

# db.connect()
# db.create_tables([Presente])

# from peewee import *

# db = SqliteDatabase('presentes.db')

# class Presente(Model):
#     nome = CharField()
#     marca = CharField()
#     cor = CharField()
#     link = CharField()
#     comprado = BooleanField(default=False)

#     class Meta:
#         database = db

# db.connect()
# db.create_tables([Presente])


from peewee import *

db = SqliteDatabase('presentes.db')

class Presente(Model):
    nome = CharField()
    marca = CharField()
    cor = CharField()
    link = CharField()
    comprado = BooleanField(default=False)
    convidado_id = IntegerField(null=True)

    class Meta:
        database = db

db.connect()
db.create_tables([Presente])
