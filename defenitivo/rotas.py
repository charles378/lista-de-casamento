import flet as ft
from homee import Home
from validador_sanha import validador
from casal import casall
from convidado import Convidador
from cadastro import cadastrar
from databaze import Casal, Convidado
from logintela import LoginPage
#from convi import Convidador


# Função fictícia para buscar o nome do usuário no banco de dados
def get_user_name(page):
    convidado_id = page.session.get("convidado_id")
    print(f'{convidado_id} home')
    if not convidado_id:
        return None
    
    convidado = Convidado.get_or_none(Convidado.id == convidado_id)
    if convidado:
        return convidado.nome
    return None

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #page.theme_mode = ft.ThemeMode.SYSTEM
    page.bgcolor = ft.colors.WHITE

    user_name = get_user_name(page)
    if user_name:
        user_initials = "".join([name[0] for name in user_name.split()[:2]]).upper()
    else:
        user_initials = "NN"  # Valor padrão caso o nome do usuário não seja encontrado

    def toggle_color(e):
        if page.bgcolor == ft.colors.BLACK:
            page.bgcolor = ft.colors.WHITE
        else:
            page.bgcolor = ft.colors.BLACK
        page.update()

    def show_user_data(e):
        # Função para buscar e mostrar os dados do usuário
        user_data = get_user_name(page)  # Aqui você pode buscar mais dados do usuário
        ft.dialog(title="Meus Dados", content=ft.Text(f"Nome: {user_data}")).show()

    def logout(e):
        # Função para sair e limpar a sessão
        page.window.close()
        page.session.remove("convidado_id")
        

    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                appbar=ft.AppBar(
                    title=ft.Text('Tela inicial'),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    toolbar_height=60,
                    color=ft.colors.AMBER,
                    leading=ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
                    leading_width=50,
                    actions=[
                        ft.IconButton(icon=ft.icons.SUNNY, 
                                    selected_icon=ft.icons.WB_SUNNY_OUTLINED, 
                                    selected=False,
                                    icon_color=ft.colors.WHITE, 
                                    on_click=toggle_color),
                        ft.CircleAvatar(content=ft.Text(user_initials)),
                        ft.PopupMenuButton(
                            items=[
                                ft.PopupMenuItem(text='Meu dados', on_click=show_user_data),
                                ft.PopupMenuItem(text='Voltar a tela inicial', on_click=lambda _: page.go('/')),
                                ft.PopupMenuItem(text='Sair', on_click=logout),
                            ]
                        )
                    ]
                ) ,
                  controls=[Home(page)],scroll=True)
        )

        if page.route == "/validador_sanha":
            page.views.append(
                ft.View(
                    route="/validador_sanha", 
                    appbar=ft.AppBar(
                    title=ft.Text('Tela de login'),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    toolbar_height=60,
                    color=ft.colors.AMBER,
                    leading=ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
                    leading_width=50,
                    actions=[
                        ft.IconButton(icon=ft.icons.SUNNY, 
                                    selected_icon=ft.icons.WB_SUNNY_OUTLINED, 
                                    selected=False,
                                    icon_color=ft.colors.WHITE, 
                                    on_click=toggle_color),
                        ft.CircleAvatar(content=ft.Text(user_initials)),
                        ft.PopupMenuButton(
                            items=[
                                ft.PopupMenuItem(text='Meu dados', on_click=show_user_data),
                                ft.PopupMenuItem(text='Voltar a tela inicial', on_click=lambda _: page.go('/')),
                                ft.PopupMenuItem(text='Sair', on_click=logout),
                            ]
                        )
                    ]
                ) , 
                    controls=[validador(page)],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER
                    )
            )
        if page.route == "/casal":
            page.views.append(
                ft.View(route="/casal",
                        appbar=ft.AppBar(
                            title=ft.Text('Controle da Lista de precentes'),
                            bgcolor=ft.colors.SURFACE_VARIANT,
                            toolbar_height=60,
                            color=ft.colors.AMBER,
                            leading=ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
                            leading_width=50,
                            actions=[
                                ft.IconButton(icon=ft.icons.SUNNY, 
                                            selected_icon=ft.icons.WB_SUNNY_OUTLINED, 
                                            selected=False,
                                            icon_color=ft.colors.WHITE, 
                                            on_click=toggle_color),
                                ft.CircleAvatar(content=ft.Text(user_initials)),
                                ft.PopupMenuButton(
                                    items=[
                                        ft.PopupMenuItem(text='Meu dados', on_click=show_user_data),
                                        ft.PopupMenuItem(text='Voltar a tela inicial', on_click=lambda _: page.go('/')),
                                        ft.PopupMenuItem(text='Sair', on_click=logout),
                                    ]
                                )
                            ]
                        ) ,  
                        controls=[casall(page)],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=True
                        )
            )
        if page.route == "/convidado":
            page.views.append(
                ft.View(route="/convidado",
                        appbar=ft.AppBar(
                        title=ft.Text('Lista de presentes'),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        toolbar_height=60,
                        color=ft.colors.AMBER,
                        leading=ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
                        leading_width=50,
                        actions=[
                            ft.IconButton(icon=ft.icons.SUNNY, 
                                        selected_icon=ft.icons.WB_SUNNY_OUTLINED, 
                                        selected=False,
                                        icon_color=ft.colors.WHITE, 
                                        on_click=toggle_color),
                            ft.CircleAvatar(content=ft.Text(user_initials)),
                            ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(text='Meu dados', on_click=show_user_data),
                                    ft.PopupMenuItem(text='Voltar a tela inicial', on_click=lambda _: page.go('/')),
                                    ft.PopupMenuItem(text='Sair', on_click=logout),
                                ]
                            )
                        ]
                    ) ,  
                        controls=[Convidador(page)],
                        scroll=True
                        )
            )
        if page.route == "/cadastro":
            page.views.append(
                ft.View(route="/cadastro",
                        appbar=ft.AppBar(
                        title=ft.Text('Lista de presentes'),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        toolbar_height=60,
                        color=ft.colors.AMBER,
                        leading=ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
                        leading_width=50,
                        actions=[
                            ft.IconButton(icon=ft.icons.SUNNY, 
                                        selected_icon=ft.icons.WB_SUNNY_OUTLINED, 
                                        selected=False,
                                        icon_color=ft.colors.WHITE, 
                                        on_click=toggle_color),
                            ft.CircleAvatar(content=ft.Text(user_initials)),
                            ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(text='Meu dados', on_click=show_user_data),
                                    ft.PopupMenuItem(text='Voltar a tela inicial', on_click=lambda _: page.go('/')),
                                    ft.PopupMenuItem(text='Sair', on_click=logout),
                                ]
                            )
                        ]
                    ) ,  
                        controls=[cadastrar(page)],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        scroll=True
                        )
            )
        page.update()

    
    page.on_route_change = route_change
    page.go(page.route)


if __name__ == "__main__":
    ft.app(main)
