# import flet as ft
# from databaze import Casal

# def login(page: ft.Page):
#     if Casal.select().count() == 0:
#         page.go('/cadastrar_dono')
#     else:
#         return (ft.Column([
#             ft.Text("Tela de Login", size=30, weight=ft.FontWeight.BOLD),
#             email_input,
#             senha_input,
#             login_button
#         ]))

#     def on_login_click(e):
#         email = email_input.value
#         senha = senha_input.value
#         try:
#             casal = Casal.get(Casal.email == email, Casal.senha == senha)
#             page.session.set("convidado_id", casal.id)
#             info = ft.SnackBar(content=ft.Text("Login com sucesso!"), bgcolor=ft.colors.GREEN)
#             page.snack_bar = info
#             page.go('/casall')
#         except Casal.DoesNotExist:
#             info = ft.SnackBar(content=ft.Text("Email ou senha incorretos!"), bgcolor=ft.colors.RED)
#             page.snack_bar = info
#         page.update()

#     email_input = ft.TextField(label="Email", autofocus=True)
#     senha_input = ft.TextField(label="Senha", password=True, can_reveal_password=True)
#     login_button = ft.ElevatedButton(text="Login", on_click=on_login_click)
                                     
#  # Certifique-se de atualizar a página após adicionar os componentes

# # Certifique-se de que a função login seja chamada corretamente

# import flet as ft
# from databaze import Casal

# def login(page: ft.Page):
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.theme_mode = ft.ThemeMode.SYSTEM

#     if page.session.get("convidado_id"):
#         page.go('/cadastrar_dono')
#     if Casal.select().count() == 0:
#         page.go('/cadastrar_dono')

#     def on_login_click(e):
#         email = email_input.value
#         senha = senha_input.value
#         try:
#             casal = Casal.get(Casal.email == email, Casal.senha == senha)
#             page.session.set("convidado_id", casal.id)
#             info = ft.SnackBar(content=ft.Text("Login com sucesso!"), bgcolor=ft.colors.GREEN)
#             page.snack_bar = info
#             page.go('/casall')
#         except Casal.DoesNotExist:
#             info = ft.SnackBar(content=ft.Text("Email ou senha incorretos!"), bgcolor=ft.colors.RED)
#             page.snack_bar = info
#         page.update()

#     email_input = ft.TextField(label="Email", autofocus=True)
#     senha_input = ft.TextField(label="Senha", password=True, can_reveal_password=True)
#     login_button = ft.ElevatedButton(text="Login", on_click=on_login_click)

    
    
#     return(
#         ft.Column([
#             ft.Text("Tela de Login", size=30, weight=ft.FontWeight.BOLD),
#             email_input,
#             senha_input,
#             login_button
#         ])
#     )

# # Certifique-se de que a função login seja chamada corretamente
# #ft.app(target=login)

import flet as ft
from databaze import Casal

def login(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.SYSTEM

    # Verificar se o usuário já está logado
    if page.session.get("dono"):
        page.go('/casal')
        

    # Campos de entrada de dados (usuário e senha)
    email_input = ft.TextField(label="Email")
    senha_input = ft.TextField(label="Senha", password=True, can_reveal_password=True)

    # Função que será chamada ao clicar no botão de login
    def on_login_click(e):
        email = email_input.value
        senha = senha_input.value
        try:
            casal = Casal.get(Casal.email == email, Casal.senha == senha)
            page.session.set("dono", casal.id)
            info = ft.SnackBar(content=ft.Text("Login com sucesso!"), bgcolor=ft.colors.GREEN)
            page.go('/casal')
            page.snack_bar = info
            
        except Casal.DoesNotExist:
            info = ft.SnackBar(content=ft.Text("Email ou senha incorretos!"), bgcolor=ft.colors.RED)
            page.snack_bar = info
        page.update()
    # Botão de login
    login_button = ft.Row([
        ft.ElevatedButton('Cadastra', on_click=lambda _: page.go('/cadastra_dono')),
        ft.ElevatedButton(text="Login", on_click=on_login_click),
    ], alignment=ft.MainAxisAlignment.END)

    # Container para agrupar os campos e o botão
    login_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Tela de Login do dono", theme_style="headlineMedium"),
                email_input,
                senha_input,
                login_button,
            ],
        ),
        padding=50,
        width=400,
        height=300,
        border_radius=10,
        bgcolor=ft.colors.ON_SECONDARY,
    )

    # Adicionando o container à página
    return login_container
