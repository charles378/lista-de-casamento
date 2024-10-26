import flet as ft
from databaze import Convidado

def LoginPage(page: ft.Page):
    def login(e):
        email = email_input.value
        senha = senha_input.value
        try:
            convidado = Convidado.get(Convidado.email == email, Convidado.senha == senha)
            page.client_storage.set("convidado_id", convidado.id)
            page.go("/convi")
        except Convidado.DoesNotExist:
            error_message.value = "Email ou senha incorretos"
            page.update()

    email_input = ft.TextField(label="Email")
    senha_input = ft.TextField(label="Senha", password=True)
    login_button = ft.ElevatedButton(text="Login", on_click=login)
    error_message = ft.Text(color=ft.colors.RED)

    return ft.Column(
        controls=[
            ft.Text("Login", size=30),
            email_input,
            senha_input,
            login_button,
            error_message
        ]
    )
