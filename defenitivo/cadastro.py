# import flet as ft
# from databaze import Convidado
# def cadastrar(page: ft.Page):
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

#     def salvar(e):
#         nome = nome_conv.value
#         telefone = telefone_conv.value
#         emaill = email.value
#         senha = senha_conv
#         try:
#             if nome and telefone and emaill:
#                 Convidado.create(nome=nome,telefone=telefone, email=emaill, senha=senha)
#                 info = ft.SnackBar(content=ft.Text("Salvo com sucesso!"), bgcolor=ft.colors.GREEN)
#                 page.open(info)
#                 return page.go('/convidado')
#         except:
#             info = ft.SnackBar(content=ft.Text("e-mail existente!"), bgcolor=ft.colors.RED)
#             page.open(info)

#     nome_conv = ft.TextField(label='Nome')
#     telefone_conv = ft.TextField(label='Telefone')
#     email = ft.TextField(label='E_mail',)
#     senha_conv = ft.TextField(label='criar senha')

#     btn_botao = ft.Row(
#         controls=[
#             ft.ElevatedButton('Salvar', on_click=salvar),
#             ft.TextButton(text='Canselar', style=ft.ButtonStyle(color=ft.colors.RED), on_click=lambda _: page.go('/'))
#             ]
#         )

#     leate = ft.Container(
#         content=ft.Column(
#             controls=[
#                 ft.Text("Tela de Cadrasto", theme_style="headlineMedium"),
#                 nome_conv,
#                 telefone_conv,
#                 email,
#                 senha_conv,
#                 btn_botao,
#             ],
#         ),
#         width=700,
#         padding=50
#     )
#     return leate
    #page.add(leate)


#ft.app(cadastrar)

import flet as ft
from databaze import Convidado

def cadastrar(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def salvar(e):
        nome = nome_conv.value
        telefone = telefone_conv.value
        emaill = email.value
        senha = senha_conv.value  # Corrigido para obter o valor da senha

        # Instruções de depuração
        print(f"Nome: {nome}, Telefone: {telefone}, Email: {emaill}, Senha: {senha}")
        print(f"Tipos: {type(nome)}, {type(telefone)}, {type(emaill)}, {type(senha)}")

        try:
            if nome and telefone and emaill:
                Convidado.create(nome=nome, telefone=telefone, email=emaill, senha=senha)
                info = ft.SnackBar(content=ft.Text("Salvo com sucesso!"), bgcolor=ft.colors.GREEN)
                page.open(info)
                return page.go('/convidado')
        except Exception as ex:
            print(f"Erro: {ex}")
            info = ft.SnackBar(content=ft.Text("e-mail existente!"), bgcolor=ft.colors.RED)
            page.open(info)

    nome_conv = ft.TextField(label='Nome')
    telefone_conv = ft.TextField(label='Telefone')
    email = ft.TextField(label='E_mail')
    senha_conv = ft.TextField(label='criar senha')

    btn_botao = ft.Row(
        controls=[
            ft.ElevatedButton('Salvar', on_click=salvar),
            ft.TextButton(text='Cancelar', style=ft.ButtonStyle(color=ft.colors.RED), on_click=lambda _: page.go('/'))
        ]
    )

    leate = ft.Container(
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
    return leate

def route_change(route):
    if route == '/convidado':
        return cadastrar(page)
    # Adicione outras rotas conforme necessário
    return ft.Text("Rota não encontrada")

# Certifique-se de que a função `route_change` está sendo chamada corretamente
#page.on_route_change = route_change

