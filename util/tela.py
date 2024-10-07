import flet as ft
<<<<<<< HEAD
from util.validador_senhaaaaa import main


def  maini(page: ft.Page):
    page.appbar = ft.AppBar(
                title=ft.Text('Lista de casamento'),
                center_title=True,
                bgcolor=ft.colors.BLUE
            )

    return ft.Container(
        alignment=ft.alignment.center,
        image=ft.Image(src='Captura de tela 2024-10-04 102641',),
        content=ft.Column(controls=[
            #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            
=======
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
>>>>>>> e53c78978c3b8b698fe3a85a6a94952580e11a80

        content=ft.Column(
            controls=[
            #foto do casal
<<<<<<< HEAD
            
=======
            avatar,
>>>>>>> e53c78978c3b8b698fe3a85a6a94952580e11a80
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
<<<<<<< HEAD
                    )
                ]
=======
                )
              ]
>>>>>>> e53c78978c3b8b698fe3a85a6a94952580e11a80
            )
    )