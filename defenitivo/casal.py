import flet as ft
from databaze import Convidado, Presente


def casall(page: ft.Page):

    def adicionar_presente(e):
        nome = nome_presente.value
        marca = marca_presente.value
        cor = cor_presente.value
        if nome and marca and cor:
            Presente.create(nome=nome, marca=marca, cor=cor)
            nome_presente.value = ""
            marca_presente.value = ""
            cor_presente.value = ""
            caregar_presente()
    
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
            delete_button = ft.IconButton(
                icon=ft.icons.DELETE,
                on_click=lambda e, id=presente.id: deletar_presente(e, id)
            )
            todos_list.controls.append(ft.Row([checkbox, delete_button]))

        for presente in concluidos_presentes:
            checkbox = ft.Checkbox(
                label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
                value=presente.compra,
                on_change=lambda e, id=presente.id: marcar_comprado(e, id),
                check_color=ft.colors.AMBER_200
            )
            delete_button = ft.IconButton(
                icon=ft.icons.DELETE,
                on_click=lambda e, id=presente.id: deletar_presente(e, id)
            )
            concluidos_list.controls.append(ft.Row([checkbox, delete_button]))

        for presente in incompletos_presentes:
            checkbox = ft.Checkbox(
                label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
                value=presente.compra,
                on_change=lambda e, id=presente.id: marcar_comprado(e, id)
            )
            delete_button = ft.IconButton(
                icon=ft.icons.DELETE,
               on_click=lambda e, id=presente.id: deletar_presente(e, id)
            )
            incompletos_list.controls.append(ft.Row([checkbox, delete_button]))

        page.update()


    nome_presente = ft.TextField(label='Nome')
    marca_presente = ft.TextField(label='Marca', expand=True,)
    cor_presente = ft.TextField(label='cor')
    adicionar_button = ft.ElevatedButton(text="Adicionar", on_click=adicionar_presente)

    titulo = ft.Text('Cadastra Presentes',  size=30, color= ft.colors.AMBER)

    todos_list = ft.Column()
    concluidos_list = ft.Column()
    incompletos_list = ft.Column()

    butan = ft.Row(
        controls=[
            marca_presente,
            ft.FloatingActionButton(
                icon=ft.icons.ADD,
                on_click=adicionar_presente
            )
        ]
    )

    tabs = ft.Tabs(
        selected_index=0,
        scrollable=True,
        tabs=[
            ft.Tab(
                text='todos',
                content=ft.Column([
                        ft.Text("Todos os Presentes:"),
                        todos_list
                    ])
                   ),
            ft.Tab(
                text='Compreto',
                content=ft.Column([
                        ft.Text("Presentes Concluídos:"),
                        concluidos_list])
                ),
            ft.Tab(
                text='incompreto',
                content=ft.Column([
                        ft.Text("Presentes Incompletos:"),
                        incompletos_list
                    ])
                ),
            ft.Tab(
                text='Lista de convidados',
                content=ft.Column(
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
                            ]
                        )
                    ]
                )
            )

        ]
    )

    page.add(titulo,nome_presente, cor_presente, butan, tabs)
    caregar_presente()


ft.app(casall)