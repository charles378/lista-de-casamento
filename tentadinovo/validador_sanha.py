import flet as ft
 
def validador(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
 
    # Função que será chamada ao clicar no botão de login
    def on_login_click(e):
        username = username_field.value
        password = password_field.value
 
        # Aqui você pode manipular os dados, como autenticação ou exibir mensagem
        print(f"Username: {username}, Password: {password}")
 
        if username == "admin" and password == "12345":
            info = ft.SnackBar(content=ft.Text("Login com sucesso!"), bgcolor=ft.colors.GREEN)
        else:
            info = ft.SnackBar(content=ft.Text("Login inválido!"), bgcolor=ft.colors.RED)
 
        page.open(info)
        page.update()
 
    # Campos de entrada de dados (usuário e senha)
    username_field = ft.TextField(label="Usuário")
    password_field = ft.TextField(label="Senha", password=True)
 
    # Botão de login
    login_button = ft.Row([ft.ElevatedButton('Canselar', on_click=lambda _: page.go('/')),
                           ft.ElevatedButton(text="Login", on_click=on_login_click), 
                           ])
 
    # Container para agrupar os campos e o botão
    login_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Tela de Login", theme_style="headlineMedium"),
                username_field,
                password_field,
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
 
# Executa o app
#ft.app(target=main)
