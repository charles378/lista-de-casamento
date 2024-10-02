import flet as ft


def  maini(page: ft.Page):
    
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.Column(controls=[
            #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            ft.AppBar(
                title=ft.Text('Lista de casamento'),
                center_title=True,
                bgcolor=ft.colors.BLUE
            ),

            #foto do casal

            #butao minha lista so quem ten asseso e o casal eo butao do convidado aulado
            ft.Container(
                content=ft.Row([ft.TextButton('Minha lista',on_click=lambda _: page.go('/store')), ft.TextButton('Convidado')],alignment=ft.alignment.center),
                alignment=ft.alignment.center,
                width=200,
                bgcolor=ft.colors.WHITE12,
                border_radius=50)])
    )

