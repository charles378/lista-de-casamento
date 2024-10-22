import flet as ft
from databaze import Convidado, Presente


def Convidador(page: ft.Page):
    page.bgcolor = ft.colors.WHITE
    
    def delete_cliente(convidado_id):
        cliente = Convidado.get(Convidado.id == convidado_id)
        cliente.delete_instance()
        caregar_presente()
    
    def marcar_comprado(e, presente_id):
        presente = Presente.get_by_id(presente_id)
        presente.compra = not presente.compra
        presente.save()
        caregar_presente()
    
    def deletar_presente(e, presente_id):
        presente = Presente.get_by_id(presente_id)
        presente.delete_instance()
        caregar_presente()

    def caregar_presente():
        todos_presentes = Presente.select()
        concluidos_presentes = Presente.select().where(Presente.compra == True)
        incompletos_presentes = Presente.select().where(Presente.compra == False)

        todos_list.controls.clear()
        concluidos_list.controls.clear()
        incompletos_list.controls.clear()

        for presente in todos_presentes:
            checkbox = ft.Checkbox(
                label=f"Nome: {presente.nome}      Marca: {presente.marca}      Cor: {presente.cor}",
                value=presente.compra,
                on_change=lambda e, id=presente.id: marcar_comprado(e, id),
                label_style=ft.TextStyle(color=ft.colors.AMBER)
            )
            
            todos_list.controls.append(ft.Row([checkbox],scroll=True))

        for presente in concluidos_presentes:
            checkbox = ft.Checkbox(
                label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
                value=presente.compra,
                on_change=lambda e, id=presente.id: marcar_comprado(e, id),
                check_color=ft.colors.AMBER_200
            )
            
            concluidos_list.controls.append(ft.Row([checkbox],scroll=True))

        for presente in incompletos_presentes:
            checkbox = ft.Checkbox(
                label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
                value=presente.compra,
                on_change=lambda e, id=presente.id: marcar_comprado(e, id)
            )
            
            incompletos_list.controls.append(ft.Row([checkbox],scroll=True))

        page.update()




    titulo = ft.Text('Lista de Presentes',  size=30, color= ft.colors.AMBER)

    todos_list = ft.Column(scroll=True)
    concluidos_list = ft.Column(scroll=True)
    incompletos_list = ft.Column(scroll=True)


    tabs = ft.Tabs(
        selected_index=0,
        scrollable=True,
        tabs=[
            ft.Tab(
                text='todos',
                content=ft.Column([
                        ft.Text("Todos os Presentes:"),
                        todos_list
                    ],scroll=True)
                   ),
            ft.Tab(
                text='Compreto',
                content=ft.Column([
                        ft.Text("Presentes Concluídos:"),
                        concluidos_list],scroll=True)
                ),
            ft.Tab(
                text='incompreto',
                content=ft.Column([
                        ft.Text("Presentes Incompletos:"),
                        incompletos_list
                    ],scroll=True)
                ),
            ft.Tab(
                text='Presente selecionado',
                content=ft.Column(
                    scroll=True,
                    controls=[
                        ft.ListView(
                            controls=[
                                ft.ListTile(
                                    title=ft.Text(convidado.nome),
                                    subtitle=ft.Text(f"{convidado.telefone} - {convidado.email}"),
                                    trailing=ft.IconButton(
                                        icon=ft.icons.DELETE,
                                        on_click=lambda e, convidado_id=convidado.id: delete_cliente(convidado_id)
                                    )
                                ) for convidado in Convidado.select()
                            ],on_scroll=True
                        )
                    ]
                )
            )

        ]
    )

    # page.add(titulo, tabs)
    caregar_presente()
    return ft.Column(
            controls=[
                titulo,
                tabs
            ]
        )


#ft.app(Convidador)