# import flet as ft
# from database1 import Cliente

# def main(page: ft.Page):
#     page.title = "Cadastro de Clientes"
    
#     def adicionar_cliente(e):
#         nome = nome_input.value
#         email = email_input.value
#         if nome and email:
#             Cliente.create(nome=nome, email=email)
#             nome_input.value = ""
#             email_input.value = ""
#             page.update()
#             carregar_clientes()

#     def carregar_clientes():
#         clientes = Cliente.select()
#         clientes_list.controls.clear()
#         for cliente in clientes:
#             clientes_list.controls.append(ft.Text(f"{cliente.nome} - {cliente.email}"))
#         page.update()

#     nome_input = ft.TextField(label="Nome")
#     email_input = ft.TextField(label="Email")
#     adicionar_button = ft.ElevatedButton(text="Adicionar", on_click=adicionar_cliente)
#     clientes_list = ft.Column()

#     page.add(
#         ft.Column([
#             nome_input,
#             email_input,
#             adicionar_button,
#             ft.Text("Clientes:"),
#             clientes_list
#         ])
#     )

#     carregar_clientes()

# ft.app(target=main)


# import flet as ft
# from database1 import Cliente

# def main(page: ft.Page):
#     page.title = "Cadastro de Clientes"
    
#     def adicionar_cliente(e):
#         nome = nome_input.value
#         email = email_input.value
#         if nome and email:
#             Cliente.create(nome=nome, email=email)
#             nome_input.value = ""
#             email_input.value = ""
#             carregar_clientes()

#     def modificar_cliente(e):
#         cliente_id = int(cliente_id_input.value)
#         cliente = Cliente.get_by_id(cliente_id)
#         cliente.nome = nome_input.value
#         cliente.email = email_input.value
#         cliente.save()
#         carregar_clientes()

#     def deletar_cliente(e):
#         cliente_id = int(cliente_id_input.value)
#         cliente = Cliente.get_by_id(cliente_id)
#         cliente.delete_instance()
#         carregar_clientes()

#     def imprimir_clientes(e):
#         clientes = Cliente.select()
#         for cliente in clientes:
#             print(f"ID: {cliente.id}, Nome: {cliente.nome}, Email: {cliente.email}")

#     def carregar_clientes():
#         clientes = Cliente.select()
#         clientes_list.controls.clear()
#         for cliente in clientes:
#             clientes_list.controls.append(ft.Text(f"{cliente.id} - {cliente.nome} - {cliente.email}"))
#         page.update()

#     cliente_id_input = ft.TextField(label="ID do Cliente")
#     nome_input = ft.TextField(label="Nome")
#     email_input = ft.TextField(label="Email")
#     adicionar_button = ft.ElevatedButton(text="Adicionar", on_click=adicionar_cliente)
#     modificar_button = ft.ElevatedButton(text="Modificar", on_click=modificar_cliente)
#     deletar_button = ft.ElevatedButton(text="Deletar", on_click=deletar_cliente)
#     imprimir_button = ft.ElevatedButton(text="Imprimir", on_click=imprimir_clientes)
#     clientes_list = ft.Column()

#     page.add(
#         ft.Column([
#             cliente_id_input,
#             nome_input,
#             email_input,
#             adicionar_button,
#             modificar_button,
#             deletar_button,
#             imprimir_button,
#             ft.Text("Clientes:"),
#             clientes_list
#         ])
#     )

#     carregar_clientes()

# ft.app(target=main)


import flet as ft
from database1 import Cliente

def main(page: ft.Page):
    page.title = "Cadastro de Clientes"
    
    def adicionar_cliente(e):
        nome = nome_input.value
        email = email_input.value
        if nome and email:
            Cliente.create(nome=nome, email=email)
            nome_input.value = ""
            email_input.value = ""
            carregar_clientes()

    def modificar_cliente(e):
        cliente_id = int(cliente_id_input.value)
        cliente = Cliente.get_by_id(cliente_id)
        cliente.nome = nome_input.value
        cliente.email = email_input.value
        cliente.save()
        carregar_clientes()

    def deletar_cliente(e):
        cliente_id = int(cliente_id_input.value)
        cliente = Cliente.get_by_id(cliente_id)
        cliente.delete_instance()
        carregar_clientes()

    def carregar_clientes():
        clientes = Cliente.select()
        clientes_list.controls.clear()
        for cliente in clientes:
            clientes_list.controls.append(ft.Text(f"{cliente.id} - {cliente.nome} - {cliente.email}"))
        page.update()

    cliente_id_input = ft.TextField(label="ID do Cliente")
    nome_input = ft.TextField(label="Nome")
    email_input = ft.TextField(label="Email")
    adicionar_button = ft.ElevatedButton(text="Adicionar", on_click=adicionar_cliente)
    modificar_button = ft.ElevatedButton(text="Modificar", on_click=modificar_cliente)
    deletar_button = ft.ElevatedButton(text="Deletar", on_click=deletar_cliente)
    clientes_list = ft.Column()

    page.add(
        ft.Tabs(
            tabs=[
                ft.Tab(
                    text="Cadastro",
                    content=ft.Column([
                        nome_input,
                        email_input,
                        adicionar_button,
                        modificar_button,
                        deletar_button,
                    ])
                ),
                ft.Tab(
                    text="Clientes",
                    content=ft.Column([
                        ft.Text("Clientes:"),
                        clientes_list
                    ])
                )
            ]
        )
    )

    carregar_clientes()

ft.app(target=main)
