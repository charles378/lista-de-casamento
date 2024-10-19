import flet as ft
from models import Cliente, Produto

def main(page: ft.Page):
    page.title = "Cadastro de Clientes e Produtos"
    
    # Funções para adicionar, modificar e deletar clientes e produtos
    def add_cliente(e):
        Cliente.create(
            nome=nome_cliente.value,
            telefone=telefone_cliente.value,
            email=email_cliente.value
        )
        nome_cliente.value = ""
        telefone_cliente.value = ""
        email_cliente.value = ""
        page.update()

    def add_produto(e):
        Produto.create(
            nome=nome_produto.value,
            marca=marca_produto.value,
            descricao=descricao_produto.value,
            estoque=int(estoque_produto.value)
        )
        nome_produto.value = ""
        marca_produto.value = ""
        descricao_produto.value = ""
        estoque_produto.value = ""
        page.update()

    def delete_cliente(cliente_id):
        cliente = Cliente.get(Cliente.id == cliente_id)
        cliente.delete_instance()
        page.update()

    def delete_produto(produto_id):
        produto = Produto.get(Produto.id == produto_id)
        produto.delete_instance()
        page.update()

    def comprar_produto(produto_id):
        produto = Produto.get(Produto.id == produto_id)
        produto.estoque -= 1
        produto.save()
        page.update()

    # Campos de entrada para clientes
    nome_cliente = ft.TextField(label="Nome")
    telefone_cliente = ft.TextField(label="Telefone")
    email_cliente = ft.TextField(label="Email")
    add_cliente_button = ft.ElevatedButton(text="Adicionar Cliente", on_click=add_cliente)

    # Campos de entrada para produtos
    nome_produto = ft.TextField(label="Nome")
    marca_produto = ft.TextField(label="Marca")
    descricao_produto = ft.TextField(label="Descrição")
    estoque_produto = ft.TextField(label="Estoque")
    add_produto_button = ft.ElevatedButton(text="Adicionar Produto", on_click=add_produto)

    # Layout da página
    page.add(
        ft.Tabs(
            tabs=[
                ft.Tab(
                    text="Todos os Clientes",
                    content=ft.Column(
                        controls=[
                            nome_cliente,
                            telefone_cliente,
                            email_cliente,
                            add_cliente_button,
                            ft.ListView(
                                controls=[
                                    ft.ListTile(
                                        title=ft.Text(cliente.nome),
                                        subtitle=ft.Text(f"{cliente.telefone} - {cliente.email}"),
                                        trailing=ft.IconButton(
                                            icon=ft.icons.DELETE,
                                            on_click=lambda e, cliente_id=cliente.id: delete_cliente(cliente_id)
                                        )
                                    ) for cliente in Cliente.select()
                                ]
                            )
                        ]
                    )
                ),
                ft.Tab(
                    text="Todos os Produtos",
                    content=ft.Column(
                        controls=[
                            nome_produto,
                            marca_produto,
                            descricao_produto,
                            estoque_produto,
                            add_produto_button,
                            ft.ListView(
                                controls=[
                                    ft.ListTile(
                                        title=ft.Text(produto.nome),
                                        subtitle=ft.Text(f"{produto.marca} - {produto.descricao} - Estoque: {produto.estoque}", expand=True),
                                        trailing=ft.Row(
                                            controls=[
                                                ft.IconButton(
                                                    icon=ft.icons.SHOPPING_CART,
                                                    on_click=lambda e, produto_id=produto.id: comprar_produto(produto_id), 
                                                ),
                                                ft.IconButton(
                                                    icon=ft.icons.DELETE,
                                                    on_click=lambda e, produto_id=produto.id: delete_produto(produto_id)
                                                )
                                            ], scroll=True
                                        )
                                    ) for produto in Produto.select()
                                ]
                            )
                        ]
                    )
                )
            ]
        )
    )

ft.app(target=main)
