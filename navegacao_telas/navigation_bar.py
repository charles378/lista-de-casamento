import flet as ft


def main(page: ft.Page):
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.HOME,
                label='Home'
            ),
            ft.NavigationBarDestination(label='Chat'),
            ft.NavigationBarDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label='Cofigora',
                tooltip="olar"
            ),
            ft.NavigationBarDestination(
                icon_content=ft.Container(bgcolor='red0', height=20, width=20),
                selected_icon_content=ft.Container(bgcolor='green', height=20, width=20),
                label='Con',
                tooltip='ague'
            )
        ],
        selected_index=1,
        indicator_color=ft.colors.PINK,
        indicator_shape=ft.RoundedRectangleBorder(radius=5),

        on_change=lambda e: print(e.control.selected_index)
    )
    page.add(ft.Text('oi'))
    page.update

if __name__ == '__main__':
    ft.app(main)