import flet as ft


def Home(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.SYSTEM

    avatar = ft.CircleAvatar(
        col=3,  # cantida de coluna que vai o cupar
        foreground_image_url='https://www.naoviu.com.br/wp-content/uploads/2023/08/Spacex.jpg',
        height=240,
        width=180,
        offset=ft.Offset(x=1.5, y=-0.1)
    )

    data_falta = ft.Container(
        content=ft.Text('Falta tantos dias e 00.00.00 segundos'),
        offset=ft.Offset(x=1, y=-2),
    )

    def expand_image(e):
        for c in carousel.controls:
            c.col=1

        e.control.col = 12 - len(carousel.controls) + 1
        carousel.update()

    carousel = ft.ResponsiveRow(
        columns=12,
        spacing=5,
        controls=[
            ft.Container(
                col=1,
                image_src=f'https://picsum.photos/250/300?{num}',
                image_fit=ft.ImageFit.COVER,
                border_radius=ft.border_radius.all(5),
                on_click=expand_image
            ) for num in range(10, 18)
        ]
    )

    carousel.controls[0].col = 12 - len(carousel.controls) + 1

    tela_foto = ft.Container(
        width=700,
        height=300,
        shadow=ft.BoxShadow(blur_radius=500),
        bgcolor=ft.colors.GREY_200,
        border_radius=ft.border_radius.all(10),
        padding=ft.padding.all(5),
        content=carousel,
    )

    botao = ft.Row([
        ft.ElevatedButton('Minha lista', on_click=lambda _: page.go('/convidado')), 
        ft.ElevatedButton('convidador', on_click=lambda _: page.go('/casal'))],
        alignment=ft.alignment.center,
        )
    
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.Column([
            #foto
            avatar,
            data_falta,
            ft.Container(
                content=botao,             
                alignment=ft.alignment.center,
                width=250,
                bgcolor=ft.colors.WHITE12,
                border_radius=50,
                offset=ft.Offset(x=0.9, y=-0.5)
              ),
            tela_foto
           ],
           alignment=ft.alignment.center,
        )
    )
