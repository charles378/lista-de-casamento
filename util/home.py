import flet as ft


def Home(page: ft.Page):
    return ft.Container(
        bgcolor='cyan',
        width=300,
        alignment=ft.alignment.center,
        content=ft.Column(controls=[
            ft.Text('Home', size=30),
            ft.ElevatedButton('Ir para a loja', on_click=lambda _: page.go('/store'))
            ]
        )
    )