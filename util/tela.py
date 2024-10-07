import flet as ft
from validador_senha import valiador_senhas


def  maini(page: ft.Page):
    def validasao_senha(e):
        pass
    
    avatar = ft.CircleAvatar(
        col=3,  # cantida de coluna que vai o cupar
        foreground_image_url='https://www.naoviu.com.br/wp-content/uploads/2023/08/Spacex.jpg',
        height=240,
        width=180
    )
    
    return ft.Container(
        alignment=ft.alignment.center,

        content=ft.Column(
            controls=[
            #foto do casal
            avatar,
            #butao minha lista so quem ten asseso e o casal eo butao do convidado aulado
            ft.Container(
                
                content=ft.Row([ft.TextButton('Minha lista', on_click=lambda _: page.go('/validador_senha')), 
                                ft.TextButton('Convidado')],
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

