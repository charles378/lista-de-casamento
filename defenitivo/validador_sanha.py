import flet as ft
from databaze import Convidado
from time import sleep
 
def validador(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
 
    # Função que será chamada ao clicar no botão de login
    def on_login_click(e):
        email = email_input.value
        senha = senha_input.value
 
        # Aqui você pode manipular os dados, como autenticação ou exibir mensagem
        print(f"Username: {email}, Password: {senha}")
 
        # if username == "admin" and password == "12345":
        #     info = ft.SnackBar(content=ft.Text("Login com sucesso!"), bgcolor=ft.colors.GREEN)
        #     page.open(info)
        #     sleep(1)
        #     return page.go('/convidado')
        # else:
        #     info = ft.SnackBar(content=ft.Text("Email ou senha incorretos\!"), bgcolor=ft.colors.RED)
        #     page.open(info)
        # page.update()
      

        try:
            convidado = Convidado.get(Convidado.email == email, Convidado.senha == senha)
            page.session.set("convidado_id", convidado.id)
            info = ft.SnackBar(content=ft.Text("Login com sucesso!"), bgcolor=ft.colors.GREEN)
            page.open(info)
            sleep(1)
            page.go('/convidado')
        except Convidado.DoesNotExist:
            info = ft.SnackBar(content=ft.Text("Email ou senha incorretos\!"), bgcolor=ft.colors.RED)
            page.open(info)
        page.update()
 
    # Campos de entrada de dados (usuário e senha)
    email_input = ft.TextField(label="Email")
    senha_input = ft.TextField(label="Senha", password=True)
 
    # Botão de login
    login_button = ft.Row([ft.ElevatedButton('Cadastra', on_click=lambda _: page.go('/cadastro')),
                           ft.ElevatedButton(text="Login", on_click=on_login_click), 
                           ], alignment=ft.MainAxisAlignment.END)
 
    # Container para agrupar os campos e o botão
    login_container = ft.Container(
        content=ft.Column(
            controls=[
                
                ft.Text("Tela de Login", theme_style="headlineMedium"),
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
    #page.add(login_container)
    return login_container
 
# Executa o app
#ft.app(target=validador)