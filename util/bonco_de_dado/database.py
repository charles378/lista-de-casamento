from sqlite3 import SQLITE_DBCONFIG_RESET_DATABASE
import flet as ft

#db = SqliteDatabase('freelancers.db')

def main(page: ft.Page):
    db = SQLITE_DBCONFIG_RESET_DATABASE('freelancers.db')


    # essa e a tabela do usuario
    class Usuario():
        # o propio peewee jera o seu propio id mas se quer comlocar e primary_key+True
        nome = ft.CharField()  # CharField() ele tem um limite de 255 caraquiteres
        email = ft.CharField(unique=True)  # para nao repeti email na tablela
        senha = ft.CharField()

        class Meta:  # para que o peewee saber qual banco de dado ele vai conversa
            database = db


    # essa e a tablela do anuncio
    class Anuncio():  # backref='usuarios' e para criar a referenca
        usuario = ft.ForeignKeyField(Usuario, backref='usuarios')  # para cliar areferencia com a tabela usuari que id
        titulo = ft.CharField()  # CharField() ele tem um limite de 255 caraquiteres
        descricao = ft.TextField()  # TextField() ele nao tem um limite de caraquiteres
        valor = ft.DecimalField()  # vai reseber um numero decimal

        class Meta:
            database = db
            
ft.app(main)