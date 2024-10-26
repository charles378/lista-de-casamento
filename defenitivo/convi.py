import flet as ft
from databaze import Convidado, Presente

# def Convidador(page: ft.Page):
#     convidado_id = page.session.get("convidado_id")
#     if not convidado_id:
#         page.go("/login")
#         return

#     page.bgcolor = ft.colors.WHITE
    
#     def marcar_comprado(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.compra = not presente.compra
#         presente.convidado_id = convidado_id
#         presente.save()
#         caregar_presente()
    
#     def caregar_presente():
#         todos_presentes = Presente.select().where(Presente.convidado_id == convidado_id)
#         concluidos_presentes = todos_presentes.where(Presente.compra == True)
#         incompletos_presentes = todos_presentes.where(Presente.compra == False)

#         todos_list.controls.clear()
#         concluidos_list.controls.clear()
#         incompletos_list.controls.clear()
#         item_comprado.controls.clear()

#         for presente in todos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome: {presente.nome}      Marca: {presente.marca}      Cor: {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id),
#                 label_style=ft.TextStyle(color=ft.colors.AMBER)
#             )
#             todos_list.controls.append(ft.Row([checkbox], scroll=True))

#         for presente in concluidos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id),
#                 check_color=ft.colors.AMBER_200
#             )
#             concluidos_list.controls.append(ft.Row([checkbox], scroll=True))

#         for presente in incompletos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id)
#             )
#             incompletos_list.controls.append(ft.Row([checkbox], scroll=True))

#         for presente in concluidos_presentes:
#             item_comprado.controls.append(ft.Text(f"Presente: {presente.nome} - Comprado por: {convidado_id}"))

#         page.update()

#     titulo = ft.Text('Lista de Presentes', size=30, color=ft.colors.AMBER)

#     todos_list = ft.Column(scroll=True)
#     concluidos_list = ft.Column(scroll=True)
#     incompletos_list = ft.Column(scroll=True)
#     item_comprado = ft.Column()

#     tabs = ft.Tabs(
#         selected_index=0,
#         scrollable=True,
#         tabs=[
#             ft.Tab(text="Todos", content=todos_list),
#             ft.Tab(text="Concluídos", content=concluidos_list),
#             ft.Tab(text="Incompletos", content=incompletos_list),
#             ft.Tab(text='Lista de convidados', content=item_comprado)
#         ]
#     )

#     caregar_presente()
#     return ft.Column(
#         controls=[
#             titulo,
#             tabs
#         ]
#     )

def Convidador(page: ft.Page):
    convidado_id = page.client_storage.get("convidado_id")
    if not convidado_id:
        page.go("/login")
        return

    page.bgcolor = ft.colors.WHITE
    
    def marcar_comprado(e, presente_id):
        presente = Presente.get_by_id(presente_id)
        presente.compra = not presente.compra
        presente.convidado_id = convidado_id
        presente.save()
        caregar_presente()
    
    def caregar_presente():
        todos_presentes = Presente.select().where(Presente.convidado_id == convidado_id)
        concluidos_presentes = todos_presentes.where(Presente.compra == True)
        incompletos_presentes = todos_presentes.where(Presente.compra == False)

        todos_list.controls.clear()
        concluidos_list.controls.clear()
        incompletos_list.controls.clear()
        item_comprado.controls.clear()

        for presente in todos_presentes:
            checkbox = ft.Checkbox(
                label=f"Nome: {presente.nome}      Marca: {presente.marca}      Cor: {presente.cor}",
                value=presente.compra,
                on_change=lambda e, id=presente.id: marcar_comprado(e, id),
                label_style=ft.TextStyle(color=ft.colors.AMBER)
            )
            todos_list.controls.append(ft.Row([checkbox], scroll=True))

        for presente in concluidos_presentes:
            checkbox = ft.Checkbox(
                label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
                value=presente.compra,
                on_change=lambda e, id=presente.id: marcar_comprado(e, id),
                check_color=ft.colors.AMBER_200
            )
            concluidos_list.controls.append(ft.Row([checkbox], scroll=True))

        for presente in incompletos_presentes:
            checkbox = ft.Checkbox(
                label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
                value=presente.compra,
                on_change=lambda e, id=presente.id: marcar_comprado(e, id)
            )
            incompletos_list.controls.append(ft.Row([checkbox], scroll=True))

        for presente in concluidos_presentes:
            item_comprado.controls.append(ft.Text(f"Presente: {presente.nome} - Comprado por: {convidado_id}"))

        page.update()

    titulo = ft.Text('Lista de Presentes', size=30, color=ft.colors.AMBER)

    todos_list = ft.Column(scroll=True)
    concluidos_list = ft.Column(scroll=True)
    incompletos_list = ft.Column(scroll=True)
    item_comprado = ft.Column()

    tabs = ft.Tabs(
        selected_index=0,
        scrollable=True,
        tabs=[
            ft.Tab(text="Todos", content=todos_list),
            ft.Tab(text="Concluídos", content=concluidos_list),
            ft.Tab(text="Incompletos", content=incompletos_list),
            ft.Tab(text='Lista de convidados', content=item_comprado)
        ]
    )

    caregar_presente()
    return ft.Column(
        controls=[
            titulo,
            tabs
        ]
    )