import flet as ft


def Store(page: ft.Page):
    return ft.Container(
        bgcolor='amber',
        width=300,
        alignment=ft.alignment.center,
        content=ft.Column(controls=[
            ft.Text('Store', size=30),
            ft.ElevatedButton('voltar para home', on_click=lambda _: page.go('/'))
            ]
        )
    )