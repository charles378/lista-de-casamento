import flet as ft
from database import db, Item

db.connect()  # para fazer a chamada da ação

db.create_tables([Item])  # para criar a tablela caso ela nao exista e criar uma lista [Usuario, Anuncio]


def casal(page: ft.Page):
    global task 
    
    def update_task_list(): # para atualiza a lista
        #tasks = tasks_container()
        tasks = Item.select()
        for u in tasks:
            page.controls.pop() # para sobre escrever o utino tasks_container da pagena
            page.add(u) # adicionando a nova tasks_container na pagina
        page.update()# para altoalizar a pagina

    def set_value(e):
        global task
        task = e.control.value # para pegar o valor do input so que preciso criar essa variavel na minha crass

    def add(e, input_task):
        nome = task # pegando o valor e salvando na variavel
        status = 'incomplete' # senpre sera salve o estatus como inconpreto

        if nome:
            Item.create(nome=nome, status=status) # para inserio o valori no banco de dados
            input_task.value = '' # para linpar o canpo de texto toda ves que salvar \
            results = Item.select()# para selecionar tudo que esta no bonco de dados
            update_task_list() # para atualiza a lista

    def tabs_changed(e):
        pass
        # if e.control.selected_index == 0:
        #     self.results = self.db_execute('SELECT * FROM tasks')
        #     self.view = 'all'
        # elif e.control.selected_index == 1:
        #     self.results = self.db_execute('SELECT * FROM tasks WHERE status = "incomplete"')
        #     self.view = 'incomplete'
        # elif e.control.selected_index == 2:
        #     self.results = self.db_execute('SELECT * FROM tasks WHERE status = "complete"')
        #     self.view = 'complete'

        # self.update_task_list()

    input_task = ft.TextField(
            hint_text='Digite um Item', # o hint_text serve para sumir o testo de ajuda
            expand=True, # o expand e para dimesiomar
            on_change=set_value # para chama a funcao set_value que capitura os dados digitado
        ) 
    
    input_bar = ft.Row(
            controls=[
                input_task,
                ft.FloatingActionButton(
                    icon=ft.icons.ADD,
                    on_click=lambda e: add(e, input_task) # para chamar a funcao add e passa um evento e o input_task
                )
            ]
        )
    tabs = ft.Tabs(
                selected_index=0, # para fixa no primeiro texto
                on_change=tabs_changed,
                tabs=[
                    ft.Tab(text='Todos'),
                    ft.Tab(text='Em andamento'),
                    ft.Tab(text='Finalizados')
                ]
        )
    page.add(input_bar, tabs)
    

ft.app(casal)