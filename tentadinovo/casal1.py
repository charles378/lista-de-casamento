import flet as ft

def casal(page: ft.Page):
    item = ft.TextField(label='O Item', expand=True)
    marca = ft.TextField(label='A marca do item', expand=True)

    def update_task_list(): # para atualiza a lista
        tasks = lista
        page.controls.pop() # para sobre escrever o utino tasks_container da pagena
        page.add(tasks) # adicionando a nova tasks_container na pagina
        page.update()# para altoalizar a pagina


    def tabs_changed(e):
        if e.control.selected_index == 0:
            page.add(ft.Text('ok'))
            page.update
        elif e.control.selected_index == 1:
            page.add(ft.Text('ok2'))
        elif e.control.selected_index == 2:
            page.add(ft.Text('ok3'))

        update_task_list()

    enpremi = ft.Row(controls=[item, marca, ft.FloatingActionButton(icon=ft.icons.ADD)])

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text='Todos'),
            ft.Tab(text='Em andamento'),
            ft.Tab(text='Finalizados')
        ]
    )

    lista = ft.Container(
        height=page.height * 0.8, # para defini o tamanho que vai 80% da pagina
            content= ft.Column(
                controls=[
                    ft.Checkbox(label='teste', value= True) # e a caixa de marcasao o value=True eo que deica a caixa marcada 
                ]
            )
    )
    page.add(enpremi, tabs, lista)

ft.app(casal)