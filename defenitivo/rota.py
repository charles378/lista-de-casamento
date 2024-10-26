import flet as ft
from logintela import LoginPage
from convi import Convidador

def main(page: ft.Page):
    page.title = "Lista de Presentes"

    def route_change(route):
        page.views.clear()
        if route == "/logintela":
            page.views.append(ft.View("/login", controls=[LoginPage(page)]))
        elif route == "/convi":
            page.views.append(ft.View("/convidador", controls=[Convidador(page)]))
        page.update()

    page.on_route_change = route_change
    page.go("/login")

ft.app(target=main)