import flet as ft
from database import db, Usuario

db.connect()  # para fazer a chamada da ação

db.create_tables([Usuario])  # para criar a tablela caso ela nao exista e criar uma lista [Usuario, Anuncio]



def cadastrar(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def salvar(e):
        nome = nome_conv.value
        telefone = telefone_conv.value
        emaill = email.value
        senha = senha_conv
        try:
            Usuario.create(nome=nome,telefone=telefone, email=emaill, senha=senha)
            info = ft.SnackBar(content=ft.Text("Salvo com sucesso!"), bgcolor=ft.colors.GREEN)
            page.open(info)
        except:
            info = ft.SnackBar(content=ft.Text("e-mail existente!"), bgcolor=ft.colors.RED)
            page.open(info)

    nome_conv = ft.TextField(label='Nome')
    telefone_conv = ft.TextField(label='Telefone')
    email = ft.TextField(label='E_mail',)
    senha_conv = ft.TextField(label='criar senha')

    btn_botao = ft.Row(
        controls=[
            ft.ElevatedButton('Salvar', on_click=salvar),
            ft.TextButton(text='Canselar', style=ft.ButtonStyle(color=ft.colors.RED), on_click=lambda _: page.go('/convidado'))
            ]
        )

    leate = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Tela de Cadrasto", theme_style="headlineMedium"),
                nome_conv,
                telefone_conv,
                email,
                senha_conv,
                btn_botao,
            ],
        ),
        width=700,
        padding=50
    )
    #return leate
    page.add(leate)


ft.app(cadastrar)