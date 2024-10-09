import flet as ft


def Home(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    avatar = ft.CircleAvatar(
        col=3,  # cantida de coluna que vai o cupar
        foreground_image_url='https://www.naoviu.com.br/wp-content/uploads/2023/08/Spacex.jpg',
        height=240,
        width=180
    )

    carosel = ft.ResponsiveRow(
        controls=[
            ft.Container(
                image_src=f'htpps://picsum.photos/250/300?10'
                
            )
        ]
    )

    tela_foto = ft.Container(
        width=700,
        height=300,
        shadow=ft.BoxShadow(blur_radius=500),
        bgcolor=ft.colors.GREY_200,
        border_radius=ft.border_radius.all(10),
        content=carosel,
    )

    botao = ft.Row([
        ft.ElevatedButton('Minha lista', on_click=lambda _: page.go('/validador_sanha')), 
        ft.ElevatedButton('convidador', on_click=lambda _: page.go('/validador_sanha'))],
        alignment=ft.alignment.center, 
        )
    
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.Column([
            #foto
            avatar,
            ft.Container(
                content=botao,             
                alignment=ft.alignment.center,
                width=250,
                bgcolor=ft.colors.WHITE12,
                border_radius=50,
              ),
            tela_foto
           ],
           alignment=ft.alignment.center
        )
    )

'''ft.Row([ft.TextButton('Minha lista', on_click=lambda _: page.go('/validador_sanha')), 
           ft.TextButton('Convidado', on_click=lambda _: page.go('/validador_sanha'))],
                                alignment=ft.alignment.center, 
                                width=200,)'''