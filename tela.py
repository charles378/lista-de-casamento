import flet as ft


def  main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.appbar = ft.AppBar(
        title=ft.Text('Lista de casamento'),
        center_title=True,
        bgcolor=ft.colors.BLUE
    )

    #foto do casal

    #butao minha lista so quem ten asseso e o casal eo butao do convidado aulado
    butaos = ft.Container(
        content=ft.Row([ft.TextButton('Minha lista',icon_color=ft.colors.BLUE), ft.TextButton('Convidado')],alignment=ft.alignment.center),
        alignment=ft.alignment.center,
        width=200,
        bgcolor=ft.colors.WHITE12,
        border_radius=50
    )

    page.add(butaos)

ft.app(main)