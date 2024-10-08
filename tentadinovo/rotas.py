import flet as ft
from home import Home
from validador_sanha import validador
#from store import Store


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                appbar=ft.AppBar(
                    title=ft.Text('Lista de casamento'),
                    
                    bgcolor=ft.colors.SURFACE_VARIANT
                ), 
                controls=[Home(page)],)
        )

        if page.route == "/validador_sanha":
            page.views.append(
                ft.View(route="/validador_sanha", 
                        controls=[validador(page)],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)


if __name__ == "__main__":
    ft.app(main)
