from database import db, Item

db.connect()  # para fazer a chamada da ação

db.create_tables([Item])  # para criar a tablela caso ela nao exista e criar uma lista [Usuario, Anuncio]

def salva(nom, marc, des):
    statu = "incomplete"
    Item.create(nom, marc, des, statu)

def printa():
    lista_usuario = Item.select()
    for u in lista_usuario:
        print('-', u.id, u.nome, u.status)

n = 'charles'
mar = 'maraco'
de = 'oils'
sta = "incomplete"

Item.create(nome=n, marca=mar  descricao=de, status=sts)
printa()