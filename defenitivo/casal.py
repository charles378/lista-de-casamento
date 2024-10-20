import flet as ft
from databaze import Convidado, Presente


def casall(page: ft.Page):


    nome_presente = ft.TextField(label='Nome')
    marca_presente = ft.TextField(label='Marca', expand=True,)
    cor_presente = ft.TextField(label='cor')
    titulo = ft.Text('Cadastra Presentes',  size=30, color= ft.colors.AMBER)
    todos_list = ft.Column()
    concluidos_list = ft.Column()
    incompletos_list = ft.Column()

    butan = ft.Row(
        controls=[
            marca_presente,
            ft.FloatingActionButton(
                icon=ft.icons.ADD,
            )
        ]
    )

    tabs = ft.Tabs(
        selected_index=0,
        scrollable=True,
        tabs=[
            ft.Tab(text='todos'),
            ft.Tab(text='Compreto'),
            ft.Tab(text='incompreto'),
            ft.Tab(text='Lista de convidados')
        ]
    )

    page.add(titulo,nome_presente, cor_presente, butan, tabs)


ft.app(casall)