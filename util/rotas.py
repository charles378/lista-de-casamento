import flet as ft
from home import Home
from store import Store
from tela import maini


def main(page: ft.Page):
    page.appbar = ft.AppBar(
                    title=ft.Text('Lista de casamento'),
                    center_title=True,
                    bgcolor=ft.colors.BLUE
                ),
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                appbar=ft.AppBar(
                    title=ft.Text('Lista de casamento'),
                    
                    bgcolor=ft.colors.SURFACE_VARIANT
                ), 
                controls=[maini(page)],)
        )

        if page.route == "/store":
            page.views.append(
                ft.View(route="/store", controls=[Store(page)])
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)


if __name__ == "__main__":
    ft.app(main)
