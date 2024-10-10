import flet as ft
from home import Home
from validador_sanha import validador
from casal import ToDo
from convidado import Precente


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.SYSTEM
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                appbar=ft.AppBar(
                    title=ft.Text('Lista de casamento'),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    toolbar_height=100,  # a altura do aapBar
                    color=ft.colors.AMBER,  # cor doa conponentes
                    leading=ft.Icon(ft.icons.HOME),  # para colocar o icom ou a sua logo usa o ft,Image()
                    leading_width=100,  # espasso dos elementos entre eles
                    actions=[  # para adisionar funçoes
                        ft.IconButton(icon=ft.icons.SUNNY),
                        ft.IconButton(icon=ft.icons.NOTIFICATIONS),
                        ft.CircleAvatar(content=ft.Text('PA')),  # para colocar o avatar do usuario
                        ft.PopupMenuButton(  # para colocar os tres pontinho
                            items=[
                                ft.PopupMenuItem(text='Meu dados'),
                                ft.PopupMenuItem(text='Cofigurações'),
                                ft.PopupMenuItem(text='Sair'),
                            ]
                        )
                    ]
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
        if page.route == "/casal":
            page.views.append(
                ft.View(route="/casal",
                        appbar=ft.AppBar(
                    title=ft.Text('Controle da Lista de precentes'),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    toolbar_height=100,  # a altura do aapBar
                    color=ft.colors.AMBER,  # cor doa conponentes
                    leading=ft.Icon(ft.icons.HOME),  # para colocar o icom ou a sua logo usa o ft,Image()
                    leading_width=100,  # espasso dos elementos entre eles
                    actions=[  # para adisionar funçoes
                        ft.IconButton(icon=ft.icons.SUNNY),
                        ft.IconButton(icon=ft.icons.NOTIFICATIONS),
                        ft.CircleAvatar(content=ft.Text('PA')),  # para colocar o avatar do usuario
                        ft.PopupMenuButton(  # para colocar os tres pontinho
                            items=[
                                ft.PopupMenuItem(text='Meu dados'),
                                ft.PopupMenuItem(text='Cofigurações'),
                                ft.PopupMenuItem(text='Sair'),
                            ]
                        )
                    ]
                ),  
                        controls=[ToDo(page)],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
            )
        if page.route == "/convidado":
            page.views.append(
                ft.View(route="/convidado",
                        appbar=ft.AppBar(
                    title=ft.Text('Lista de presentes'),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    toolbar_height=100,  # a altura do aapBar
                    color=ft.colors.AMBER,  # cor doa conponentes
                    leading=ft.Icon(ft.icons.HOME),  # para colocar o icom ou a sua logo usa o ft,Image()
                    leading_width=100,  # espasso dos elementos entre eles
                    actions=[  # para adisionar funçoes
                        ft.IconButton(icon=ft.icons.SUNNY),
                        ft.IconButton(icon=ft.icons.NOTIFICATIONS),
                        ft.CircleAvatar(content=ft.Text('PA')),  # para colocar o avatar do usuario
                    ]
                ),  
                        controls=[Precente(page)]
                        )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)


if __name__ == "__main__":
    ft.app(main)
