import flet as ft


def Home(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    avatar = ft.CircleAvatar(
        col=3,  # cantida de coluna que vai o cupar
        foreground_image_url='https://www.naoviu.com.br/wp-content/uploads/2023/08/Spacex.jpg',
        height=240,
        width=180
    )

    

    botao = ft.Row([ft.ElevatedButton('Criar lista'), ft.ElevatedButton('convidador')],)
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.Column([
            #foto
            avatar,
            ft.Container(
                content=ft.Row([ft.TextButton('Minha lista', on_click=lambda _: page.go('/validador_sanha')), 
                                ft.TextButton('Convidado', on_click=lambda _: page.go('/validador_sanha'))],
                                alignment=ft.alignment.center, 
                                width=200,),             
                alignment=ft.alignment.center,
                width=200,
                bgcolor=ft.colors.WHITE12,
                border_radius=50,
              ) 
           ]
        )
    )
