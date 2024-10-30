# import flet as ft
# from databaze import Convidado, Casal

# def cadastrar(page: ft.Page):
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

#     def salvar(e):
#         nome = nome_conv.value
#         telefone = telefone_conv.value
#         emaill = email.value
#         senha = senha_conv.value  # Corrigido para obter o valor da senha

#         try:
#             if nome and telefone and emaill and senha:
#                 # Verificar quantos casais já estão cadastrados
#                 num_casais = Casal.select().count()
#                 print(num_casais)
#                 if num_casais < 2:
#                     Casal.create(nome=nome, telefone=telefone, email=emaill, senha=senha)
#                     info = ft.SnackBar(content=ft.Text("Casal salvo com sucesso!"), bgcolor=ft.colors.GREEN)
#                     page.open(info)
#                     return page.go('/casal')
#                 else:
#                     Convidado.create(nome=nome, telefone=telefone, email=emaill, senha=senha)
#                     info = ft.SnackBar(content=ft.Text("Convidado salvo com sucesso!"), bgcolor=ft.colors.GREEN)
#                     page.open(info)
#                     return page.go('/convidado')
#                 #page.open(info)
                
#         except Exception as ex:
#             print(f"Erro: {ex}")
#             info = ft.SnackBar(content=ft.Text("e-mail existente!"), bgcolor=ft.colors.RED)
#             page.open(info)

#     nome_conv = ft.TextField(label='Nome')
#     telefone_conv = ft.TextField(label='Telefone')
#     email = ft.TextField(label='E_mail')
#     senha_conv = ft.TextField(label='Criar senha')

#     btn_botao = ft.Row(
#         controls=[
#             ft.ElevatedButton('Salvar', on_click=salvar),
#             ft.TextButton(text='Cancelar', style=ft.ButtonStyle(color=ft.colors.RED), on_click=lambda _: page.go('/'))
#         ]
#     )

#     page.add(ft.Container(
#         content=ft.Column(
#             controls=[
#                 ft.Text("Tela de Cadastro", theme_style="headlineMedium"),
#                 nome_conv,
#                 telefone_conv,
#                 email,
#                 senha_conv,
#                 btn_botao,
#             ],
#         ),
#         width=700,
#         padding=50
#     ))

# # Inicie o aplicativo Flet
# ft.app(target=cadastrar)

import flet as ft
from databaze import Convidado, Casal

def cadastrar(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def salvar(e):
        nome = nome_conv.value
        telefone = telefone_conv.value
        emaill = email.value
        senha = senha_conv.value  # Corrigido para obter o valor da senha

        try:
            if nome and telefone and emaill and senha:
                Convidado.create(nome=nome, telefone=telefone, email=emaill, senha=senha)
                info = ft.SnackBar(content=ft.Text("Convidado salvo com sucesso!"), bgcolor=ft.colors.GREEN)
                page.open(info)
                return page.go('/convidado')
            #page.open(info)
                
        except Exception as ex:
            print(f"Erro: {ex}")
            info = ft.SnackBar(content=ft.Text("e-mail existente!"), bgcolor=ft.colors.RED)
            page.open(info)

    nome_conv = ft.TextField(label='Nome')
    telefone_conv = ft.TextField(label='Telefone')
    email = ft.TextField(label='E_mail')
    senha_conv = ft.TextField(label='Criar senha')

    btn_botao = ft.Row(
        controls=[
            ft.ElevatedButton('Salvar', on_click=salvar),
            ft.TextButton(text='Cancelar', style=ft.ButtonStyle(color=ft.colors.RED), on_click=lambda _: page.go('/'))
        ]
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Tela de Cadastro", theme_style="headlineMedium"),
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

# Inicie o aplicativo Flet
# ft.app(target=cadastrar)

