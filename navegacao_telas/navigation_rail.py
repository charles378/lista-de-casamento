import flet as ft 


def main(page: ft.Page):
    rail = ft.NavigationRail(
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME,
                label='Inicio'
            ),
            ft.NavigationRailDestination(
                label='Charat'
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label='Itens salvos'
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Container(bgcolor='red', width=20, height=20),
                selected_icon_content=ft.Container(bgcolor='green', width=20, height=20),
                label='fotos',
                padding=ft.padding.only(top=50)
            )
        ],
        bgcolor=ft.colors.GREY_900,
        selected_index=0,
        extended=True,
        min_extended_width=100,
        trailing=ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text='Cadastrasto'),
                ft.PopupMenuItem(text='Enviar em massa'),
            ]
        ),
        leading=ft.CircleAvatar(content=ft.Text(value='Pa')),

        on_change=lambda e: print(e.control.selected_index)
    )

    row = ft.Row(controls=[rail], expand=True)
    page.add(row)


if __name__ == '__main__':
    ft.app(main)