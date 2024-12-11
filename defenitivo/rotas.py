import flet as ft
from homee import Home
from validador_sanha import validador
from casal import casall
from convidado import Convidador
from cadastro import cadastrar
from cadastra_dono import cadastrar_dono
from databaze import Casal, Convidado
from validador_senha_dono import login
from configue import onfique



# Função para buscar o nome do usuário no banco de dados e retornar as iniciais  QXDxf_9DSNtb:D7
def get_user_initials(page):
    convidado_id = page.session.get("convidado_id")
    print(f"Convidado ID: {convidado_id}")  # Adicione esta linha para depuração
    if not convidado_id:
        return "NN"  # Valor padrão caso o ID do convidado não seja encontrado
    
    convidado = Convidado.get_or_none(Convidado.id == convidado_id)
    if convidado:
        nome = convidado.nome
        print(f"Nome do Convidado: {nome}")  # Adicione esta linha para depuração
        # Pegar as duas primeiras letras do nome
        iniciais = "".join([name[0] for name in nome.split()[:2]]).upper()
        return iniciais
    return "NN"  # Valor padrão caso o nome do convidado não seja encontrado

# Função para buscar a cor de fundo do usuário no banco de dados
def get_user_bgcolor(page):
    convidado_id = page.session.get("convidado_id")
    if not convidado_id:
        return ft.colors.WHITE  # Valor padrão caso o ID do convidado não seja encontrado
    
    convidado = Convidado.get_or_none(Convidado.id == convidado_id)
    if convidado and convidado.bgcolor:
        return convidado.bgcolor
    return ft.colors.WHITE  # Valor padrão caso a cor não seja encontrada

# Função para salvar a cor de fundo do usuário no banco de dados
def save_user_bgcolor(page, color):
    convidado_id = page.session.get("convidado_id")
    if convidado_id:
        Convidado.update(bgcolor=color).where(Convidado.id == convidado_id).execute()


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #page.theme_mode = ft.ThemeMode.SYSTEM
    #page.bgcolor = ft.colors.WHITE

    user_initials = get_user_initials(page)
    print(f"User initials: {user_initials}")  # Adicione esta linha para depuração

    page.bgcolor = get_user_bgcolor(page)  # Usar a cor de fundo do usuário ao carregar a página

    def toggle_color(e):
        if page.bgcolor == ft.colors.BLACK:
            page.bgcolor = ft.colors.WHITE
        else:
            page.bgcolor = ft.colors.BLACK
        save_user_bgcolor(page, page.bgcolor)  # Salvar a nova cor de fundo no banco de dados
        page.update()


    def show_user_data(e):
        # Função para buscar e mostrar os dados do usuário
        user_data = user_initials  # Aqui você pode buscar mais dados do usuário
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
        if page.route == "/validador_senha_dono":
            page.views.append(
                ft.View(
                    route="/validador_senha_dono", 
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
                    controls=[login(page)],
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
                                        ft.PopupMenuItem(text='onfiguração fotos', on_click=lambda _: page.go('/configue')),
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
        if page.route == "/cadastra_dono":
            page.views.append(
                ft.View(route="/cadastra_dono",
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
                        controls=[cadastrar_dono(page)],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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
        if page.route == "/configue":
            page.views.append(
                ft.View(
                    route="/configue",
                    appbar=ft.AppBar(
                        title=ft.Text('Configuracao das fotos'),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        toolbar_height=60,
                        color=ft.colors.AMBER,
                        leading=ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
                        leading_width=50,
                        actions=[
                            ft.IconButton(
                                icon=ft.icons.SUNNY, 
                                selected_icon=ft.icons.WB_SUNNY_OUTLINED, 
                                selected=False,
                                icon_color=ft.colors.WHITE, 
                                on_click=toggle_color
                            ),
                            ft.CircleAvatar(content=ft.Text(user_initials)),
                            ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(text='Meu dados', on_click=show_user_data),
                                    ft.PopupMenuItem(text='Voltar a tela inicial', on_click=lambda _: page.go('/')),
                                    ft.PopupMenuItem(text='Sair', on_click=logout),
                                ]
                            )
                        ]
                    ),
                    controls=[onfique(page)],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    scroll=True
                )
            )

        page.update()

    
    page.on_route_change = route_change
    page.go(page.route)


if __name__ == "__main__":
    ft.app(main, view=ft.AppView.WEB_BROWSER, port=8080)
