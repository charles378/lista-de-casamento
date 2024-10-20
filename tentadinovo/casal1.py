
import flet as ft
from database3 import Casal, Convidado, Presente

def main(page: ft.Page):
    page.title = "Lista de Presentes"

    # Campos de entrada para casal
    nome_casal = ft.TextField(label="Nome")
    telefone_casal = ft.TextField(label="Telefone")
    email_casal = ft.TextField(label="Email")
    senha_casal = ft.TextField(label="Senha")
    add_cliente_button = ft.ElevatedButton(text="Adicionar Cliente", on_click=add_casal)

    # Campos de entrada para convidado
    nome_convidado = ft.TextField(label="Nome")
    telefone_convidado = ft.TextField(label="Telefone")
    email_convidado = ft.TextField(label="Email")
    senha_convidado = ft.TextField(label="Senha")
    add_cliente_button = ft.ElevatedButton(text="Adicionar Cliente", on_click=add_convidado)

    # Campos de entrada para presente
    nome_presente = ft.TextField(label="Nome")
    marca_presente = ft.TextField(label="Marca")
    cor_presente = ft.TextField(label="Descrição")
    add_produto_button = ft.ElevatedButton(text="Adicionar Produto", on_click=add_presente)


    def add_casal(e):
        Casal.create(
            nome=nome_casal.value,
            telefone=telefone_casal.value,
            email=email_casal.value,
            senha=senha_casal.value
        )
        nome_casal.value = ""
        telefone_casal.value = ""
        email_casal.value = ""
        senha_casal.value = ""
    
        page.update()

    def add_convidado(e):
        Convidado.create(
            nome=nome_convidado.value,
            telefone=telefone_convidado.value,
            email=email_convidado.value,
            senha=senha_convidado.value 
        )
        nome_convidado.value = ""
        telefone_convidado.value = ""
        email_convidado.value = ""
        senha_convidado.value = ""
        
        page.update()

    def add_presente(e):
        Presente.create(
            nome=nome_presente.value,
            marca=marca_presente.value,
            cor=cor_presente.value
        )
        nome_presente.value = ""
        marca_presente.value = ""
        cor_presente.value = ""
        carregar_presentes()
        page.update()

    
    def adicionar_presente(e):
        nome = nome_input.value
        marca = marca_input.value
        cor = cor_input.value
        link = link_input.value
        if nome and marca and cor and link:
            Presente.create(nome=nome, marca=marca, cor=cor, link=link)
            nome_input.value = ""
            marca_input.value = ""
            cor_input.value = ""
            link_input.value = ""
            carregar_presentes()

    
    def marcar_comprado(e, presente_id, id):
        convidado = Convidado.get_by_id(id)
        presente = Presente.get_by_id(presente_id)
        presente.comprado = not presente.comprado
        presente.convidado_id =  convidado.id # Aqui você pode definir o ID do convidado
        presente.save()
        carregar_presentes()

    def deletar_presente(e, presente_id):
        presente = Presente.get_by_id(presente_id)
        presente.delete_instance()
        carregar_presentes()

    def carregar_presentes():
        todos_presentes = Presente.select()
        concluidos_presentes = Presente.select().where(Presente.comprado == True)
        incompletos_presentes = Presente.select().where(Presente.comprado == False)

        todos_list.controls.clear()
        concluidos_list.controls.clear()
        incompletos_list.controls.clear()

        for presente in todos_presentes:
            checkbox = ft.Checkbox(
                label=f"{presente.nome} - {presente.marca} - {presente.cor} - {presente.link}",
                value=presente.comprado,
                on_change=lambda e, id=presente.id: marcar_comprado(e, id)
            )
            delete_button = ft.IconButton(
                icon=ft.icons.DELETE,
                on_click=lambda e, id=presente.id: deletar_presente(e, id)
            )
            todos_list.controls.append(ft.Row([checkbox, delete_button]))

        for presente in concluidos_presentes:
            checkbox = ft.Checkbox(
                label=f"{presente.nome} - {presente.marca} - {presente.cor} - {presente.link}",
                value=presente.comprado,
                on_change=lambda e, id=presente.id: marcar_comprado(e, id)
            )
            delete_button = ft.IconButton(
                icon=ft.icons.DELETE,
                on_click=lambda e, id=presente.id: deletar_presente(e, id)
            )
            concluidos_list.controls.append(ft.Row([checkbox, delete_button]))

        for presente in incompletos_presentes:
            checkbox = ft.Checkbox(
                label=f"{presente.nome} - {presente.marca} - {presente.cor} - {presente.link}",
                value=presente.comprado,
                on_change=lambda e, id=presente.id: marcar_comprado(e, id)
            )
            delete_button = ft.IconButton(
                icon=ft.icons.DELETE,
                on_click=lambda e, id=presente.id: deletar_presente(e, id)
            )
            incompletos_list.controls.append(ft.Row([checkbox, delete_button]))

        page.update()

    nome_input = ft.TextField(label="Nome do Presente")
    marca_input = ft.TextField(label="Marca")
    cor_input = ft.TextField(label="Cor")
    link_input = ft.TextField(label="Link")
    adicionar_button = ft.ElevatedButton(text="Adicionar", on_click=adicionar_presente)
    todos_list = ft.Column()
    concluidos_list = ft.Column()
    incompletos_list = ft.Column()

    page.add(
        ft.Tabs(
            tabs=[
                ft.Tab(
                    text="Adicionar Presente",
                    content=ft.Column([
                        nome_input,
                        marca_input,
                        cor_input,
                        link_input,
                        adicionar_button,
                        ft.ListView(
                                controls=[
                                    ft.ListTile(
                                        title=ft.Text(cliente.nome),
                                        subtitle=ft.Text(f"{cliente.telefone} - {cliente.email}"),
                                        trailing=ft.IconButton(
                                            icon=ft.icons.DELETE,
                                           # on_click=lambda e, cliente_id=cliente.id: delete_pr(cliente_id)
                                        )
                                    ) for cliente in Casal.select()
                                ]
                            )
                    ])
                ),
                ft.Tab(
                    text="Todos",
                    content=ft.Column([
                        ft.Text("Todos os Presentes:"),
                        ft.ListView(
                                controls=[
                                    ft.ListTile(
                                        title=ft.Text(cliente.nome),
                                        subtitle=ft.Text(f"{cliente.telefone} - {cliente.email}"),
                                        trailing=ft.IconButton(
                                            icon=ft.icons.DELETE,
                                           # on_click=lambda e, cliente_id=cliente.id: delete_cliente(cliente_id)
                                        )
                                    ) for cliente in Convidado.select()
                                ]
                            )
                    ])
                ),
                ft.Tab(
                    text="Concluídos",
                    content=ft.Column([
                        ft.Text("Presentes Concluídos:"),
                        concluidos_list
                    ])
                ),
                ft.Tab(
                    text="Incompletos",
                    content=ft.Column([
                        ft.Text("Presentes Incompletos:"),
                        incompletos_list
                    ])
                )
            ]
        )
    )

    carregar_presentes()

ft.app(target=main)
