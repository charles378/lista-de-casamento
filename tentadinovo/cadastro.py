import flet as ft


def cadastrar(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    nome_conv = ft.TextField(label='Nome')
    telefone_conv = ft.TextField(label='Telefone')
    senha_conv = ft.TextField(label='criar senha')

    btn_botao = ft.Row(controls=[ft.ElevatedButton('Salvar'),ft.TextButton(text='Canselar', style=ft.ButtonStyle(color=ft.colors.RED))])

    leate = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Tela de Cadrasto", theme_style="headlineMedium"),
                nome_conv,
                telefone_conv,
                senha_conv,
                btn_botao,
            ],
        ),
        width=700,
        padding=50
    )
    return leate
    #page.add(leate)


#ft.app(cadastrar)