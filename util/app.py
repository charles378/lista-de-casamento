# import flet as ft
# from database import Presente

# def main(page: ft.Page):
#     page.title = "Lista de Presentes"
    
#     def adicionar_presente(e):
#         nome = nome_input.value
#         if nome:
#             Presente.create(nome=nome)
#             nome_input.value = ""
#             carregar_presentes()

#     def marcar_comprado(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.comprado = not presente.comprado
#         presente.save()
#         carregar_presentes()

#     def deletar_presente(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.delete_instance()
#         carregar_presentes()

#     def carregar_presentes():
#         presentes = Presente.select()
#         presentes_list.controls.clear()
#         for presente in presentes:
#             checkbox = ft.Checkbox(
#                 label=presente.nome,
#                 value=presente.comprado,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id)
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             presentes_list.controls.append(ft.Row([checkbox, delete_button]))
#         page.update()

#     nome_input = ft.TextField(label="Nome do Presente")
#     adicionar_button = ft.ElevatedButton(text="Adicionar", on_click=adicionar_presente)
#     presentes_list = ft.Column()

#     page.add(
#         ft.Tabs(
#             tabs=[
#                 ft.Tab(
#                     text="Adicionar Presente",
#                     content=ft.Column([
#                         nome_input,
#                         adicionar_button,
#                     ])
#                 ),
#                 ft.Tab(
#                     text="Lista de Presentes",
#                     content=ft.Column([
#                         ft.Text("Presentes:"),
#                         presentes_list
#                     ])
#                 )
#             ]
#         )
#     )

#     carregar_presentes()

# ft.app(target=main)


# import flet as ft
# from database import Presente

# def main(page: ft.Page):
#     page.title = "Lista de Presentes"
    
#     def adicionar_presente(e):
#         nome = nome_input.value
#         marca = marca_input.value
#         cor = cor_input.value
#         link = link_input.value
#         if nome and marca and cor and link:
#             Presente.create(nome=nome, marca=marca, cor=cor, link=link)
#             nome_input.value = ""
#             marca_input.value = ""
#             cor_input.value = ""
#             link_input.value = ""
#             carregar_presentes()

#     def marcar_comprado(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.comprado = not presente.comprado
#         presente.save()
#         carregar_presentes()

#     def deletar_presente(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.delete_instance()
#         carregar_presentes()

#     def carregar_presentes():
#         todos_presentes = Presente.select()
#         concluidos_presentes = Presente.select().where(Presente.comprado == True)
#         incompletos_presentes = Presente.select().where(Presente.comprado == False)

#         todos_list.controls.clear()
#         concluidos_list.controls.clear()
#         incompletos_list.controls.clear()

#         for presente in todos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"{presente.nome} - {presente.marca} - {presente.cor} - {presente.link}",
#                 value=presente.comprado,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id)
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             todos_list.controls.append(ft.Row([checkbox, delete_button]))

#         for presente in concluidos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"{presente.nome} - {presente.marca} - {presente.cor} - {presente.link}",
#                 value=presente.comprado,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id)
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             concluidos_list.controls.append(ft.Row([checkbox, delete_button]))

#         for presente in incompletos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"{presente.nome} - {presente.marca} - {presente.cor} - {presente.link}",
#                 value=presente.comprado,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id)
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             incompletos_list.controls.append(ft.Row([checkbox, delete_button]))

#         page.update()

#     nome_input = ft.TextField(label="Nome do Presente")
#     marca_input = ft.TextField(label="Marca")
#     cor_input = ft.TextField(label="Cor")
#     link_input = ft.TextField(label="Link")
#     adicionar_button = ft.ElevatedButton(text="Adicionar", on_click=adicionar_presente)
#     todos_list = ft.Column()
#     concluidos_list = ft.Column()
#     incompletos_list = ft.Column()

#     page.add(
#         ft.Tabs(
#             tabs=[
#                 ft.Tab(
#                     text="Adicionar Presente",
#                     content=ft.Column([
#                         nome_input,
#                         marca_input,
#                         cor_input,
#                         link_input,
#                         adicionar_button,
#                     ])
#                 ),
#                 ft.Tab(
#                     text="Todos",
#                     content=ft.Column([
#                         ft.Text("Todos os Presentes:"),
#                         todos_list
#                     ])
#                 ),
#                 ft.Tab(
#                     text="Concluídos",
#                     content=ft.Column([
#                         ft.Text("Presentes Concluídos:"),
#                         concluidos_list
#                     ])
#                 ),
#                 ft.Tab(
#                     text="Incompletos",
#                     content=ft.Column([
#                         ft.Text("Presentes Incompletos:"),
#                         incompletos_list
#                     ])
#                 )
#             ]
#         )
#     )

#     carregar_presentes()

# ft.app(target=main)


# import flet as ft
# from database import Presente

# def main(page: ft.Page):
#     page.title = "Lista de Presentes"
    
#     def adicionar_presente(e):
#         nome = nome_input.value
#         marca = marca_input.value
#         cor = cor_input.value
#         link = link_input.value
#         if nome and marca and cor and link:
#             Presente.create(nome=nome, marca=marca, cor=cor, link=link)
#             nome_input.value = ""
#             marca_input.value = ""
#             cor_input.value = ""
#             link_input.value = ""
#             carregar_presentes()

#     def marcar_comprado(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.comprado = not presente.comprado
#         presente.convidado_id = 1  # Aqui você pode definir o ID do convidado
#         presente.save()
#         carregar_presentes()

#     def deletar_presente(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.delete_instance()
#         carregar_presentes()

#     def carregar_presentes():
#         todos_presentes = Presente.select()
#         concluidos_presentes = Presente.select().where(Presente.comprado == True)
#         incompletos_presentes = Presente.select().where(Presente.comprado == False)

#         todos_list.controls.clear()
#         concluidos_list.controls.clear()
#         incompletos_list.controls.clear()

#         for presente in todos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"{presente.id} - {presente.nome} - {presente.marca} - {presente.cor} - {presente.link}",
#                 value=presente.comprado,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id)
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             todos_list.controls.append(ft.Row([checkbox, delete_button]))

#         for presente in concluidos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"{presente.id} - {presente.nome} - {presente.marca} - {presente.cor} - {presente.link}",
#                 value=presente.comprado,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id)
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             concluidos_list.controls.append(ft.Row([checkbox, delete_button]))

#         for presente in incompletos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"{presente.id} - {presente.nome} - {presente.marca} - {presente.cor} - {presente.link}",
#                 value=presente.comprado,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id)
#             )
#             delete_button = ft.IconButton(
#                 icon=ft.icons.DELETE,
#                 on_click=lambda e, id=presente.id: deletar_presente(e, id)
#             )
#             incompletos_list.controls.append(ft.Row([checkbox, delete_button]))

#         page.update()

#     nome_input = ft.TextField(label="Nome do Presente")
#     marca_input = ft.TextField(label="Marca")
#     cor_input = ft.TextField(label="Cor")
#     link_input = ft.TextField(label="Link")
#     adicionar_button = ft.ElevatedButton(text="Adicionar", on_click=adicionar_presente)
#     todos_list = ft.Column()
#     concluidos_list = ft.Column()
#     incompletos_list = ft.Column()

#     page.add(
#         ft.Tabs(
#             tabs=[
#                 ft.Tab(
#                     text="Adicionar Presente",
#                     content=ft.Column([
#                         nome_input,
#                         marca_input,
#                         cor_input,
#                         link_input,
#                         adicionar_button,
#                     ])
#                 ),
#                 ft.Tab(
#                     text="Todos",
#                     content=ft.Column([
#                         ft.Text("Todos os Presentes:"),
#                         todos_list
#                     ])
#                 ),
#                 ft.Tab(
#                     text="Concluídos",
#                     content=ft.Column([
#                         ft.Text("Presentes Concluídos:"),
#                         concluidos_list
#                     ])
#                 ),
#                 ft.Tab(
#                     text="Incompletos",
#                     content=ft.Column([
#                         ft.Text("Presentes Incompletos:"),
#                         incompletos_list
#                     ])
#                 )
#             ]
#         )
#     )

#     carregar_presentes()

# ft.app(target=main)
