import flet as ft


def valiador_senhas(page: ft.Page):

    usuario = ft.TextField(label='Nome')
    senha = ft.TextField(label='Senha')

    return ft.Container(
         bgcolor='cyan',
        width=300,
        alignment=ft.alignment.center,
        content=ft.Column(controls=[
            ft.Text('validador_senha', size=30),
            ft.ElevatedButton('Ir para a loja', on_click=lambda _: page.go('/store'))
            ]
        )
    )
      