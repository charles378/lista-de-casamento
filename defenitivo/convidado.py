import flet as ft
from databaze import Convidado, Presente

def Convidador(page: ft.Page):
    convidado_id = page.session.get("convidado_id")
    print(convidado_id)
    if not convidado_id:
        page.go("/login")
        return
    
    def marcar_comprado(e, presente_id):
        presente = Presente.get_by_id(presente_id)
        if presente.convidado_id and presente.convidado_id != convidado_id:
            # Se o presente já está vinculado a outro convidado, não permitir a alteração
            return
        presente.compra = not presente.compra
        presente.convidado_id = convidado_id if presente.compra else None
        presente.save()
        caregar_presente()

    def deletar_presente(e, presente_id):
        presente = Presente.get_by_id(presente_id)
        presente.delete_instance()
        caregar_presente()
    
    def caregar_presente():
        todos_presentes = Presente.select()
        todos_presentes_convidado = Presente.select().where(Presente.convidado_id == convidado_id)
        concluidos_presentes = Presente.select().where(Presente.compra == True)
        incompletos_presentes = Presente.select().where(Presente.compra == False)

        todos_list.controls.clear()
        concluidos_list.controls.clear()
        incompletos_list.controls.clear()
        item_comprado.controls.clear()

        for presente in todos_presentes:
            checkbox = ft.Checkbox(
                label=f"Nome: {presente.nome}      Marca: {presente.marca}      Cor: {presente.cor}",
                value=presente.compra,
                on_change=lambda e, id=presente.id: marcar_comprado(e, id),
                label_style=ft.TextStyle(color=ft.colors.AMBER),
                disabled=presente.convidado_id and presente.convidado_id != convidado_id
            )
            todos_list.controls.append(ft.Row([checkbox], scroll=True))

        for presente in concluidos_presentes:
            checkbox = ft.Checkbox(
                label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
                value=presente.compra,
                on_change=lambda e, id=presente.id: marcar_comprado(e, id),
                check_color=ft.colors.AMBER_200,
                disabled=presente.convidado_id and presente.convidado_id != convidado_id
            )
            concluidos_list.controls.append(ft.Row([checkbox], scroll=True))

        for presente in incompletos_presentes:
            checkbox = ft.Checkbox(
                label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
                value=presente.compra,
                on_change=lambda e, id=presente.id: marcar_comprado(e, id),
                disabled=presente.convidado_id and presente.convidado_id != convidado_id
            )
            incompletos_list.controls.append(ft.Row([checkbox], scroll=True))

        for presente in todos_presentes_convidado:
            checkbox = ft.Checkbox(
                label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
                value=presente.compra,
                on_change=lambda e, id=presente.id: marcar_comprado(e, id),
                disabled=presente.convidado_id and presente.convidado_id != convidado_id
            )
            
            item_comprado.controls.append(ft.Row([checkbox], scroll=True))

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
    return ft.Column([titulo, tabs])

# Certifique-se de que o método Convidador seja chamado corretamente em seu aplicativo Flet
