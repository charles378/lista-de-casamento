import flet as ft
import sqlite3

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.window_resizable = False
    page.window_always_on_top = True
    page.title = 'Controle de lista do casal'
    task = ''
    view = 'all'
    db_execute('CREATE TABLE IF NOT EXISTS TASKS(name, status)')
    results = db_execute('SELECT * FROM tasks')

    def db_execute(query, params=[]):
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute(query, params)
            con.commit()
            return cur.fetchall()

    def checked(e, view, update_task_list):
        is_checked = e.control.value
        label = e.control.label

        if is_checked:
            db_execute('UPDATE tasks SET status = "complete" WHERE name = ?', params=[label])
        else:
            db_execute('UPDATE tasks SET status = "incomplete" WHERE name = ?', params=[label])

        if view == 'all':
            results = db_execute('SELECT * FROM tasks')
        else:
            results = db_execute('SELECT * from tasks WHERE status = ?', params=[view])

        update_task_list(results)

    def tasks_container(page, results):
        return ft.Container(
            height=page.height * 0.8,
            content=ft.Column(
                controls=[
                    ft.Checkbox(label=res[0], 
                                on_change=lambda e: checked(e, view, update_task_list),
                                value=True if res[1] == 'complete' else False)
                    for res in results if res
                ]
            )
        )

    def set_value(e):
        return e.control.value

    def add(e, input_task, task, update_task_list):
        nome = task
        status = 'incomplete'

        if nome:
            db_execute(query='INSERT INTO tasks VALUES(?,?)', params=[nome, status])
            input_task.value = ''
            results = db_execute('SELECT * FROM tasks')
            update_task_list(results)

    def update_task_list(page, results):
        tasks = tasks_container(page, results)
        page.controls.pop()
        page.add(tasks)
        page.update()

    def tabs_changed(e, update_task_list, view):
        if e.control.selected_index == 0:
            results = db_execute('SELECT * FROM tasks')
            view = 'all'
        elif e.control.selected_index == 1:
            results = db_execute('SELECT * FROM tasks WHERE status = "incomplete"')
            view = 'incomplete'
        update_task_list(results)

    def update_task_list(results):
            tasks = tasks_container(page, results)
            page.controls.pop()
            page.add(tasks)
            page.update()

            page.add(ft.TextField(on_change=lambda e: set_value(e)))
            page.add(ft.Button(text="Add", on_click=lambda e: add(e, input_task, task, update_task_list)))
            page.add(ft.Tabs(on_change=lambda e: tabs_changed(e, update_task_list)))

            update_task_list(results)

ft.app(target=main)
# import flet as ft
# from databaze import Convidado, Presente


# def Convidador(page: ft.Page):
    
#     def marcar_comprado(e, presente_id,id):
#         convidado = Convidado.get_by_id(id)
#         presente = Presente.get_by_id(presente_id)
#         presente.compra = not presente.compra
#         presente.convidado_id =  convidado.id # Aqui você pode definir o ID do convidado
#         presente.save()
#         caregar_presente()
    
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
#                 label_style=ft.TextStyle(color=ft.colors.AMBER)
#             )
            
#             todos_list.controls.append(ft.Row([checkbox],scroll=True))

#         for presente in concluidos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id),
#                 check_color=ft.colors.AMBER_200
#             )
            
#             concluidos_list.controls.append(ft.Row([checkbox],scroll=True))

#         for presente in incompletos_presentes:
#             checkbox = ft.Checkbox(
#                 label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id)
#             )
            
#             incompletos_list.controls.append(ft.Row([checkbox],scroll=True))

#         page.update()

#     titulo = ft.Text('Lista de Presentes',  size=30, color= ft.colors.AMBER)

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
#             ft.Tab(text='Lista de convidados', content=item_comprado )
#         ]
#     )

#     caregar_presente()
#     page.add( ft.Column(
#             controls=[
#                 titulo,
#                 tabs
#             ]
#         ))
# ft.app(Convidador)

# import flet as ft
# from databaze import Convidado, Presente

# def Convidador(page: ft.Page):
#     page.bgcolor = ft.colors.WHITE
    
#     def marcar_comprado(e, presente_id, id):
#         convidado = Convidado.get_by_id(id)
#         presente = Presente.get_by_id(presente_id)
#         presente.compra = not presente.compra
#         presente.convidado_id = convidado.id
#         presente.save()
#         caregar_presente()
    
#     def caregar_presente():
#         todos_presentes = Presente.select()
#         concluidos_presentes = Presente.select().where(Presente.compra == True)
#         incompletos_presentes = Presente.select().where(Presente.compra == False)

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
#             convidado = Convidado.get_by_id(presente.convidado_id)
#             item_comprado.controls.append(ft.Text(f"Presente: {presente.nome} - Comprado por: {convidado.nome}"))

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


# import flet as ft
# from databaze import Convidado, Presente

# def Convidador(page: ft.Page):
#     page.bgcolor = ft.colors.WHITE
    
#     def marcar_comprado(e, presente_id, id):
#         convidado = Convidado.get_by_id(id)
#         presente = Presente.get_by_id(presente_id)
#         presente.compra = not presente.compra
#         presente.convidado_id = convidado.id
#         presente.save()
#         caregar_presente()
    
#     def caregar_presente():
#         todos_presentes = Presente.select()
#         concluidos_presentes = Presente.select().where(Presente.compra == True)
#         incompletos_presentes = Presente.select().where(Presente.compra == False)

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
#             if presente.convidado_id is not None:
#                 try:
#                     convidado = Convidado.get_by_id(presente.convidado_id)
#                     item_comprado.controls.append(ft.Text(f"Presente: {presente.nome} - Comprado por: {convidado.nome}"))
#                 except Convidado.DoesNotExist:
#                     item_comprado.controls.append(ft.Text(f"Presente: {presente.nome} - Comprado por: Convidado desconhecido"))

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


# import flet as ft
# from databaze import Convidado, Presente

# def Convidador(page: ft.Page):
#     convidado_id = page.session.get("convidado_id")
#     print(convidado_id)
#     if not convidado_id:
#         page.go("/login")
#         return
    
#     def marcar_comprado(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         if presente.convidado_id and presente.convidado_id != convidado_id:
#             # Se o presente já está vinculado a outro convidado, não permitir a alteração
#             return
#         presente.compra = not presente.compra
#         presente.convidado_id = convidado_id if presente.compra else None
#         presente.save()
#         caregar_presente()

#     def deletar_presente(e, presente_id):
#         presente = Presente.get_by_id(presente_id)
#         presente.delete_instance()
#         caregar_presente()
    
#     def caregar_presente():
#         todos_presentes = Presente.select()
#         todos_presentes_convidado = Presente.select().where(Presente.convidado_id == convidado_id)
#         concluidos_presentes = Presente.select().where(Presente.compra == True)
#         incompletos_presentes = Presente.select().where(Presente.compra == False)

#         todos_list.controls.clear()
#         concluidos_list.controls.clear()
#         incompletos_list.controls.clear()

#         todos_presentes_convidado = Presente.select().where(Presente.convidado_id == convidado_id)
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

#         for presente in todos_presentes_convidado:
#             checkbox = ft.Checkbox(
#                 label=f"Nome: {presente.nome} Marca: {presente.marca} Cor: {presente.cor}",
#                 value=presente.compra,
#                 on_change=lambda e, id=presente.id: marcar_comprado(e, id)
#             )
            
#             item_comprado.controls.append(ft.Row([checkbox], scroll=True),)

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
#     return(ft.Column(
#         controls=[
#             titulo,
#             tabs
#         ]
#     ))
# # ft.app(Convidador)
