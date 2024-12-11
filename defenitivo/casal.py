import flet as ft
from databaze import Convidado, Presente, Casal

def casall(page: ft.Page):

    if page.session.get("convidado_id"):
        convidado_id = page.session.get("convidado_id")
        if convidado_id == 0:
            page.go('/')
        return ft.SnackBar(content=ft.Text("Email ou senha incorretos!"), bgcolor=ft.colors.RED)

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
    
    def delete_cliente(e, convidado_id):
        cliente = Convidado.get(Convidado.id == convidado_id)
        cliente.delete_instance()
        atualizar_dados()
    
    def marcar_comprado(e, presente_id):
        presente = Presente.get_by_id(presente_id)
        presente.compra = not presente.compra
        presente.save()
        caregar_presente()
    
    def deletar_presente(e, presente_id):
        presente = Presente.get_by_id(presente_id)
        presente.delete_instance()
        caregar_presente()

    # Função para atualizar a lista de clientes e produtos
    def atualizar_dados():
        clientes_list.controls.clear()
        
        for cliente in Convidado.select():
            compras = Presente.select().where(Presente.convidado_id == cliente.id)
            compras_texto = ", ".join([f"{compra.nome} ({'Comprado' if compra.compra else 'Não comprado'})" for compra in compras])
            
            clientes_list.controls.append(
                ft.Column(controls=[
                    ft.ListTile(
                        title=ft.Text(f'{cliente.id}  {cliente.nome}'),
                        subtitle=ft.Text(f"     {cliente.telefone} - {cliente.email} -- {compras_texto}"),
                        trailing=ft.IconButton(
                            icon=ft.icons.DELETE,
                            on_click=lambda e, cliente_id=cliente.id: delete_cliente(e, cliente_id),
                        )
                    ),
                ])
            )
        page.update()



    def caregar_presente():
        todos_presentes = Presente.select()
        concluidos_presentes = Presente.select().where(Presente.compra == True)
        incompletos_presentes = Presente.select().where(Presente.compra == False)
        

        todos_list.controls.clear()
        concluidos_list.controls.clear()
        incompletos_list.controls.clear()
        

        for presente in todos_presentes:
            checkbox = ft.Checkbox(
                label=f"Nome:   {presente.nome}      Marca:   {presente.marca}      Cor:  {presente.cor}",
                value=presente.compra,
                on_change=lambda e, id=presente.id: marcar_comprado(e, id),
                label_style=ft.TextStyle(color=ft.colors.AMBER)
            )
            delete_button = ft.IconButton(
                icon=ft.icons.DELETE,
                on_click=lambda e, id=presente.id: deletar_presente(e, id)
            )
            todos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

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
            concluidos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

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
            incompletos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

        page.update()

    nome_presente = ft.TextField(label='Nome')
    marca_presente = ft.TextField(label='Marca', expand=True)
    cor_presente = ft.TextField(label='Cor')
    adicionar_button = ft.ElevatedButton(text="Adicionar", on_click=adicionar_presente)

    titulo = ft.Text('Cadastra Presentes', size=30, color=ft.colors.AMBER)

    todos_list = ft.Column(scroll=True)
    concluidos_list = ft.Column(scroll=True)
    incompletos_list = ft.Column(scroll=True)
    clientes_list = ft.Column()

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
            ft.Tab(text="Todos", content=todos_list),
            ft.Tab(text="Concluídos", content=concluidos_list),
            ft.Tab(text="Incompletos", content=incompletos_list),
            ft.Tab(text='Lista de convidados', content=clientes_list )
        ]
    )
    
    atualizar_dados()
    caregar_presente()
    return ft.Column(
            controls=[
                titulo,
                nome_presente,
                marca_presente,
                cor_presente,
                adicionar_button,
                tabs
            ]
        )


# Inicie o aplicativo Flet
# ft.app(target=casall)
# import flet as ft
# from databaze import Convidado, Presente

# def casall(page: ft.Page):

#     def adicionar_presente(e):
#         nome = nome_presente.value
#         marca = marca_presente.value
#         cor = cor_presente.value
#         if nome and marca and cor:
#             Presente.create(nome=nome, marca=marca, cor=cor)
#             nome_presente.value = ""
#             marca_presente.value = ""
#             cor_presente.value = ""
#             carregar_presente()
    
#     def delete_cliente(e, convidado_id):
#         cliente = Convidado.get(Convidado.id == convidado_id)
#         cliente.delete_instance()
#         atualizar_dados()
    
#     def marcar_comprado(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.compra = not presente.compra
#         presente.save()
#         carregar_presente()
    
#     def deletar_presente(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.delete_instance()
#         carregar_presente()

#     # Função para atualizar a lista de clientes e produtos
#     def atualizar_dados():
#         clientes_list.controls.clear()
        
#         for cliente in Convidado.select():
#             clientes_list.controls.append(
#                 ft.ListTile(
#                     title=ft.Text(cliente.nome),
#                     subtitle=ft.Text(f"{cliente.telefone} - {cliente.email}"),
#                     trailing=ft.IconButton(
#                         icon=ft.icons.DELETE,
#                         on_click=lambda e, cliente_id=cliente.id: delete_cliente(e, cliente_id)
#                     )
#                 )
#             )
#         page.update()  # Atualiza a página

#     def carregar_presente():
#         todos_presentes = Presente.select()
#         concluidos_presentes = Presente.select().where(Presente.compra == True)
#         incompletos_presentes = Presente.select().where(Presente.compra == False)
        
#         todos_list.controls.clear()
#         concluidos_list.controls.clear()
#         incompletos_list.controls.clear()
        
#         for presente in todos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome: {presente.nome}      Marca: {presente.marca}      Cor: {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id),
#                 label_style=ft.TextStyle(color=ft.colors.AMBER)
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             todos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

#         for presente in concluidos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id),
#                 check_color=ft.colors.AMBER_200
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             concluidos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

#         for presente in incompletos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id)
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             incompletos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

#         page.update()  # Atualiza a página

#     nome_presente = ft.TextField(label='Nome')
#     marca_presente = ft.TextField(label='Marca', expand=True)
#     cor_presente = ft.TextField(label='Cor')

#     adicionar_button = ft.ElevatedButton(text='Adicionar Presente', on_click=adicionar_presente)

#     todos_list = ft.Column()
#     concluidos_list = ft.Column()
#     incompletos_list = ft.Column()
#     clientes_list = ft.Column()

#     page.add(
#         ft.Tabs(
#             tabs=[
#                 ft.Tab(text='Todos', content=todos_list),
#                 ft.Tab(text='Concluídos', content=concluidos_list),
#                 ft.Tab(text='Incompletos', content=incompletos_list),
#                 ft.Tab(text='Convidados', content=clientes_list)
#             ]
#         ),
#         nome_presente,
#         marca_presente,
#         cor_presente,
#         adicionar_button
#     )

#     atualizar_dados()
#     carregar_presente()
# ft.app(casall)

# import flet as ft
# from databaze import Convidado, Presente

# def casall(page: ft.Page):
#     dono_id = page.session.get("dono_id")
#     if not dono_id:
#         page.go("/login")
#         return

#     def adicionar_presente(e):
#         nome = nome_presente.value
#         marca = marca_presente.value
#         cor = cor_presente.value
#         if nome and marca and cor:
#             Presente.create(nome=nome, marca=marca, cor=cor)
#             nome_presente.value = ""
#             marca_presente.value = ""
#             cor_presente.value = ""
#             caregar_presente()
    
#     def delete_cliente(e, convidado_id):
#         cliente = Convidado.get(Convidado.id == convidado_id)
#         cliente.delete_instance()
#         atualizar_dados()
    
#     def marcar_comprado(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.compra = not presente.compra
#         presente.save()
#         caregar_presente()
    
#     def deletar_presente(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.delete_instance()
#         caregar_presente()

#     def atualizar_dados():
#         clientes_list.controls.clear()
        
#         for cliente in Convidado.select():
#             clientes_list.controls.append(
#                 ft.ListTile(
#                     title=ft.Text(cliente.nome),
#                     subtitle=ft.Text(f"{cliente.id} {cliente.telefone} - {cliente.email}"),
#                     trailing=ft.IconButton(
#                         icon=ft.icons.DELETE,
#                         on_click=lambda e, cliente_id=cliente.id: delete_cliente(e, cliente_id)
#                     )
#                 )
#             )
#         page.update()

#     def caregar_presente():
#         todos_presentes = Presente.select()
#         concluidos_presentes = Presente.select().where(Presente.compra == True)
#         incompletos_presentes = Presente.select().where(Presente.compra == False)
        
#         todos_list.controls.clear()
#         concluidos_list.controls.clear()
#         incompletos_list.controls.clear()

#         for presente in todos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome: {presente.nome}      Marca: {presente.marca}      Cor: {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id),
#                 label_style=ft.TextStyle(color=ft.colors.AMBER),
#                 disabled=presente.convidado_id and presente.convidado_id 
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             todos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

#         for presente in concluidos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id),
#                 check_color=ft.colors.AMBER_200,
#                 disabled=presente.convidado_id and presente.convidado_id 
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             concluidos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

#         for presente in incompletos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id),
#                 disabled=presente.convidado_id and presente.convidado_id 
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             incompletos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

#         page.update()

#     nome_presente = ft.TextField(label="Nome do Presente")
#     marca_presente = ft.TextField(label="Marca do Presente")
#     cor_presente = ft.TextField(label="Cor do Presente")
#     adicionar_button = ft.ElevatedButton(text="Adicionar Presente", on_click=adicionar_presente)

#     todos_list = ft.Column(scroll=True)
#     concluidos_list = ft.Column(scroll=True)
#     incompletos_list = ft.Column(scroll=True)
#     clientes_list = ft.Column()

#     tabs = ft.Tabs(
#         selected_index=0,
#         scrollable=True,
#         tabs=[
#             ft.Tab(text="Todos", content=todos_list),
#             ft.Tab(text="Concluídos", content=concluidos_list),
#             ft.Tab(text="Incompletos", content=incompletos_list),
#             ft.Tab(text="Convidados", content=clientes_list)
#         ]
#     )

#     caregar_presente()
#     atualizar_dados()

#     return ft.Column(
#             controls=[
                
#                 nome_presente,
#                 marca_presente,
#                 cor_presente,
#                 adicionar_button,
#                 tabs
#             ]
#         )


# # Certifique-se de que o método casall seja chamado corretamente em seu aplicativo Flet


# import flet as ft
# from databaze import Convidado, Presente, Casal

# def casall(page: ft.Page):
    

#     def adicionar_presente(e):
#         nome = nome_presente.value
#         marca = marca_presente.value
#         cor = cor_presente.value
#         if nome and marca and cor:
#             Presente.create(nome=nome, marca=marca, cor=cor)
#             nome_presente.value = ""
#             marca_presente.value = ""
#             cor_presente.value = ""
#             caregar_presente()

#     def delete_cliente(e, convidado_id):
#         cliente = Convidado.get(Convidado.id == convidado_id)
#         cliente.delete_instance()
#         atualizar_dados()

#     def marcar_comprado(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.compra = not presente.compra
#         presente.save()
#         caregar_presente()

#     def deletar_presente(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.delete_instance()
#         caregar_presente()

#     # Função para atualizar a lista de clientes e produtos
#     def atualizar_dados():
#         clientes_list.controls.clear()
#         for cliente in Convidado.select():
#             compras = Presente.select().where(Presente.convidado_id == cliente.id)
#             compras_texto = ", ".join([f"{compra.nome} ({'Comprado' if compra.compra else 'Não comprado'})" for compra in compras])
#             clientes_list.controls.append(
#                 ft.Column(controls=[
#                     ft.ListTile(
#                         title=ft.Text(f'{cliente.id}  {cliente.nome}'),
#                         subtitle=ft.Text(f"     {cliente.telefone} - {cliente.email} -- {compras_texto}"),
#                         trailing=ft.IconButton(
#                             icon=ft.icons.DELETE,
#                             on_click=lambda e, cliente_id=cliente.id: delete_cliente(e, cliente_id),
#                         )
#                     ),
#                 ])
#             )
#         page.update()

#     def caregar_presente():
#         todos_presentes = Presente.select()
#         concluidos_presentes = Presente.select().where(Presente.compra == True)
#         incompletos_presentes = Presente.select().where(Presente.compra == False)

#         todos_list.controls.clear()
#         concluidos_list.controls.clear()
#         incompletos_list.controls.clear()

#         for presente in todos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome:   {presente.nome}      Marca:   {presente.marca}      Cor:  {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id),
#                 label_style=ft.TextStyle(color=ft.colors.AMBER)
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             todos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

#         for presente in concluidos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id),
#                 check_color=ft.colors.AMBER_200
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             concluidos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

#         for presente in incompletos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id)
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             incompletos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

#         page.update()

#     nome_presente = ft.TextField(label='Nome')
#     marca_presente = ft.TextField(label='Marca', expand=True)
#     cor_presente = ft.TextField(label='Cor')
#     adicionar_button = ft.ElevatedButton(text="Adicionar", on_click=adicionar_presente)
#     titulo = ft.Text('Cadastra Presentes', size=30, color=ft.colors.AMBER)
#     todos_list = ft.Column(scroll=True)
#     concluidos_list = ft.Column(scroll=True)
#     incompletos_list = ft.Column(scroll=True)
#     clientes_list = ft.Column()
#     butan = ft.Row(
#         controls=[
#             marca_presente,
#             ft.FloatingActionButton(
#                 icon=ft.icons.ADD,
#                 on_click=adicionar_presente
#             )
#         ]
#     )
#     tabs = ft.Tabs(
#         selected_index=0,
#         scrollable=True,
#         tabs=[
#             ft.Tab(text="Todos", content=todos_list),
#             ft.Tab(text="Concluídos", content=concluidos_list),
#             ft.Tab(text="Incompletos", content=incompletos_list),
#             ft.Tab(text='Lista de convidados', content=clientes_list)
#         ]
#     )

#     atualizar_dados()
#     caregar_presente()
#     return(ft.Column(
#         controls=[
#             titulo,
#             nome_presente,
#             marca_presente,
#             cor_presente,
#             adicionar_button,
#             tabs
#         ]
#     ))

# #ft.app(casall)

# import flet as ft
# from databaze import Convidado, Presente, Casal

# def casall(page: ft.Page):
#     # Verificar se o usuário logado é o dono
#     dono_id = page.session.get("dono")
#     print(dono_id)
#     if not dono_id:
#         page.go("/login")

    
#     def delete_casal(cliente_id):
#             cliente = Casal.get(Casal.id == cliente_id)
#             cliente.delete_instance()
#             page.update()

#     def adicionar_presente(e):
#         nome = nome_presente.value
#         marca = marca_presente.value
#         cor = cor_presente.value
#         if nome and marca and cor:
#             Presente.create(nome=nome, marca=marca, cor=cor)
#             nome_presente.value = ""
#             marca_presente.value = ""
#             cor_presente.value = ""
#             caregar_presente()

#     def delete_cliente(e, convidado_id):
#         cliente = Convidado.get(Convidado.id == convidado_id)
#         cliente.delete_instance()
#         atualizar_dados()

#     def marcar_comprado(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.compra = not presente.compra
#         presente.save()
#         caregar_presente()

#     def deletar_presente(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.delete_instance()
#         caregar_presente()

#     # Função para atualizar a lista de clientes e produtos
#     def atualizar_dados():
#         clientes_list.controls.clear()
#         for cliente in Convidado.select():
#             compras = Presente.select().where(Presente.convidado_id == cliente.id)
#             compras_texto = ", ".join([f"{compra.nome} Mrca:{compra.marca}da Cor {compra.cor}({''if compra.compra else 'Não comprado'})" for compra in compras])
#             clientes_list.controls.append(
#                 ft.Column(controls=[
#                     ft.ListTile(
#                         title=ft.Text(f'{cliente.id}  {cliente.nome}'),
#                         subtitle=ft.Text(f"     Telefone {cliente.telefone}  Email {cliente.email} O Presente {compras_texto}"),
#                         trailing=ft.IconButton(
#                             icon=ft.icons.DELETE,
#                             on_click=lambda e, cliente_id=cliente.id: delete_cliente(e, cliente_id),
#                         )
#                     ),ft.Text(f'       O Presente  {compras_texto}')
#                 ])
#             )
#         page.update()

#     def caregar_presente():
#         todos_presentes = Presente.select()
#         concluidos_presentes = Presente.select().where(Presente.compra == True)
#         incompletos_presentes = Presente.select().where(Presente.compra == False)

#         todos_list.controls.clear()
#         concluidos_list.controls.clear()
#         incompletos_list.controls.clear()

#         for presente in todos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome:   {presente.nome}      Marca:   {presente.marca}      Cor:  {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id),
#                 label_style=ft.TextStyle(color=ft.colors.AMBER)
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             todos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

#         for presente in concluidos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome:   {presente.nome}      Marca:   {presente.marca}      Cor:  {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id),
#                 check_color=ft.colors.AMBER_200
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             concluidos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

#         for presente in incompletos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome:   {presente.nome}      Marca:   {presente.marca}      Cor:  {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id)
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             incompletos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

#         page.update()

#     nome_presente = ft.TextField(label='Nome')
#     marca_presente = ft.TextField(label='Marca', expand=True)
#     cor_presente = ft.TextField(label='Cor')
#     adicionar_button = ft.ElevatedButton(text="Adicionar", on_click=adicionar_presente)
#     titulo = ft.Text('Cadastra Presentes', size=30, color=ft.colors.AMBER)
#     todos_list = ft.Column(scroll=True)
#     concluidos_list = ft.Column(scroll=True)
#     incompletos_list = ft.Column(scroll=True)
#     clientes_list = ft.Column()
#     butan = ft.Row(
#         controls=[
#             marca_presente,
#             ft.FloatingActionButton(
#                 icon=ft.icons.ADD,
#                 on_click=adicionar_presente
#             )
#         ]
#     )
#     tabs = ft.Tabs(
#         selected_index=0,
#         scrollable=True,
#         tabs=[
#             ft.Tab(text="Todos", content=todos_list),
#             ft.Tab(text="Concluídos", content=concluidos_list),
#             ft.Tab(text="Incompletos", content=incompletos_list),
#             ft.Tab(text='Lista de convidados', content=clientes_list)
#         ]
#     )

#     atualizar_dados()
#     caregar_presente()
#     return ft.Column(
#         controls=[
#             titulo,
#             nome_presente,
#             marca_presente,
#             cor_presente,
#             adicionar_button,
#             tabs,
#             delete_casal
#         ]
#     )

# Certifique-se de que o método casall seja chamado corretamente em seu aplicativo Flet
#ft.app(target=casall)

# import flet as ft
# from databaze import Convidado, Presente, Casal

# def casall(page: ft.Page):
#     # Verificar se o usuário logado é o dono
#     dono_id = page.session.get("dono")
#     if not dono_id:
#         page.go("/login")
#         return
#     dono = Casal.get_or_none(Casal.id == dono_id)
#     if not dono:
#         page.go("/login")
#         return

#     def adicionar_presente(e):
#         nome = nome_presente.value
#         marca = marca_presente.value
#         cor = cor_presente.value
#         if nome and marca and cor:
#             Presente.create(nome=nome, marca=marca, cor=cor)
#             nome_presente.value = ""
#             marca_presente.value = ""
#             cor_presente.value = ""
#             caregar_presente()

#     def delete_cliente(e, convidado_id):
#         cliente = Convidado.get(Convidado.id == convidado_id)
#         cliente.delete_instance()
#         atualizar_dados()

#     def marcar_comprado(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.compra = not presente.compra
#         presente.save()
#         caregar_presente()

#     def deletar_presente(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.delete_instance()
#         caregar_presente()

#     # Função para atualizar a lista de clientes e produtos
#     def atualizar_dados():
#         clientes_list.controls.clear()
#         for cliente in Convidado.select():
#             compras = Presente.select().where(Presente.convidado_id == cliente.id)
#             compras_texto = ", ".join([f"{compra.nome} ({'Comprado' if compra.compra else 'Não comprado'})" for compra in compras])
#             clientes_list.controls.append(
#                 ft.Column(controls=[
#                     ft.ListTile(
#                         title=ft.Text(f'{cliente.id}  {cliente.nome}'),
#                         subtitle=ft.Text(f"     {cliente.telefone} - {cliente.email} -- {compras_texto}"),
#                         trailing=ft.IconButton(
#                             icon=ft.icons.DELETE,
#                             on_click=lambda e, cliente_id=cliente.id: delete_cliente(e, cliente_id),
#                         )
#                     ),
#                 ])
#             )
#         page.update()

#     def caregar_presente():
#         todos_presentes = Presente.select()
#         concluidos_presentes = Presente.select().where(Presente.compra == True)
#         incompletos_presentes = Presente.select().where(Presente.compra == False)

#         todos_list.controls.clear()
#         concluidos_list.controls.clear()
#         incompletos_list.controls.clear()

#         for presente in todos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome:   {presente.nome}      Marca:   {presente.marca}      Cor:  {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id),
#                 label_style=ft.TextStyle(color=ft.colors.AMBER)
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             todos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

#         for presente in concluidos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id),
#                 check_color=ft.colors.AMBER_200
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             concluidos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

#         for presente in incompletos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id)
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             incompletos_list.controls.append(ft.Row([checkbox, delete_button], scroll=True))

#     # Componentes da página
#     nome_presente = ft.TextField(label="Nome do Presente")
#     marca_presente = ft.TextField(label="Marca do Presente")
#     cor_presente = ft.TextField(label="Cor do Presente")
#     adicionar_button = ft.ElevatedButton(text="Adicionar Presente", on_click=adicionar_presente)
#     todos_list = ft.Column()
#     concluidos_list = ft.Column()
#     incompletos_list = ft.Column()
#     clientes_list = ft.Column()
#     atualizar_dados()
#     caregar_presente()
#     return(
#         ft.Column([
#             ft.Text("Gerenciamento de Presentes", size=30, weight=ft.FontWeight.BOLD),
#             nome_presente,
#             marca_presente,
#             cor_presente,
#             adicionar_button,
#             ft.Text("Todos os Presentes"),
#             todos_list,
#             ft.Text("Presentes Concluídos"),
#             concluidos_list,
#             ft.Text("Presentes Incompletos"),
#             incompletos_list,
#             ft.Text("Lista de Clientes"),
#             clientes_list
#         ])
#     )

#     # Atualizar dados ao carregar a página
    

# # Certifique-se de que a função casall seja chamada corretamente

