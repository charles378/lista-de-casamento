import flet as ft
from validador_senha import main


def  maini(page: ft.Page):
    page.appbar = ft.AppBar(
                title=ft.Text('Lista de casamento'),
                center_title=True,
                bgcolor=ft.colors.BLUE
            )

    return ft.Container(
        alignment=ft.alignment.center,
        image=ft.Image(src='Captura de tela 2024-10-04 102641',),
        content=ft.Column(controls=[
            #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            

            #foto do casal
            
            #butao minha lista so quem ten asseso e o casal eo butao do convidado aulado
            ft.Container(
                content=ft.Row([ft.TextButton('Minha lista',on_click=lambda _: page.go('/store')), ft.TextButton('Convidado')],alignment=ft.alignment.center),
                alignment=ft.alignment.center,
                width=200,
                bgcolor=ft.colors.WHITE12,
                border_radius=50,
                    )
                ]
            )
    )
