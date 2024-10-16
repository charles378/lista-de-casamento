import flet as ft
import sqlite3


class ToDo:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor =ft.colors.BLACK
        #self.page.window_width = 350
        #self.page.window_height=450
        self.page.window_resizable=False
        self.page.window_always_on_top=True
        self.page.title='Controle de lista do casal'
        self.task = '' # criando a variavel para capitura o valor do input
        self.view = 'all'
        self.db_execute('CREATE TABLE IF NOT EXISTS TASKS(name, status)') # esta linha cria o banco de dado 
        self.results = self.db_execute('SELECT * FROM tasks') # para selecionar tudo que esta no bonco de dados
        self.main_page()

    # criar uma funcao para manipular o banco de dado
    def db_execute(self, query, params = []):
        with sqlite3.connect('datbase.db') as con: # abrindo a conmequicao do banco de dado com o nome de < con >
            cur = con.cursor() # criando um curso 
            cur.execute(query, params)
            con.commit() # para salva oque tiver digitado 
            return cur.fetchall() # para retornar toda as linha do banco de dado

    def checked(self, e):
        is_checked = e.control.value # pegar o valor do ft.Checkbox
        label = e.control.label # pegar o label do ft.Checkbox

        if is_checked:
            self.db_execute('UPDATE tasks SET status = "complete" WHERE name = ?', params=[label]) # para verifica o stato esta conpleto e nudar
        else:
            self.db_execute('UPDATE tasks SET status = "incomplete" WHERE name = ?', params=[label]) # para verifica o stato esta incompleto e nudar

        if self.view == 'all':
            self.results = self.db_execute('SELECT * FROM tasks')
        else:
            self.results = self.db_execute('SELECT * from tasks WHERE status = ?', params=[self.view])

        self.update_task_list() # para atualiza a lista

    # criando o caixa de marcasao 
    def tasks_container(self):
        return ft.Container(
            height=self.page.height * 0.8, # para defini o tamanho que vai 80% da pagina
            content= ft.Column(
                controls=[
                    ft.Checkbox(label=res[0], 
                                on_change = self.checked,
                                value= True if res[1] == 'complete' else False) # e a caixa de marcasao o value=True eo que deica a caixa marcada 
                    for res in self.results if res
                ]
            )
        )
    # funcao para pegar o valor do input
    def set_value(self, e):
        self.task = e.control.value # para pegar o valor do input so que preciso criar essa variavel na minha crass
    
    # criar funcao para dicionar os items no banco de dado
    def add(self, e, input_task):
        nome = self.task # pegando o valor e salvando na variavel
        status = 'incomplete' # senpre sera salve o estatus como inconpreto

        if nome:
            self.db_execute(query='INSERT INTO tasks VALUES(?,?)', params=[nome, status]) # para inserio o valori no banco de dados
            input_task.value = '' # para linpar o canpo de texto toda ves que salvar \
            self.results = self.db_execute('SELECT * FROM tasks') # para selecionar tudo que esta no bonco de dados
            self.update_task_list() # para atualiza a lista

    def update_task_list(self): # para atualiza a lista
        tasks = self.tasks_container()
        self.page.controls.pop() # para sobre escrever o utino tasks_container da pagena
        self.page.add(tasks) # adicionando a nova tasks_container na pagina
        self.page.update()# para altoalizar a pagina

    def tabs_changed(self, e):
        if e.control.selected_index == 0:
            self.results = self.db_execute('SELECT * FROM tasks')
            self.view = 'all'
        elif e.control.selected_index == 1:
            self.results = self.db_execute('SELECT * FROM tasks WHERE status = "incomplete"')
            self.view = 'incomplete'
        elif e.control.selected_index == 2:
            self.results = self.db_execute('SELECT * FROM tasks WHERE status = "complete"')
            self.view = 'complete'

        self.update_task_list()

    def main_page(self):
        input_task = ft.TextField(
            hint_text='Digite um Item', # o hint_text serve para sumir o testo de ajuda
            expand=True, # o expand e para dimesiomar
            on_change=self.set_value # para chama a funcao set_value que capitura os dados digitado
        )  

        # criendo local de adicionar as lista
        input_bar = ft.Row(
            controls=[
                input_task,
                ft.FloatingActionButton(
                    icon=ft.icons.ADD,
                    on_click=lambda e: self.add(e, input_task) # para chamar a funcao add e passa um evento e o input_task
                )
            ]
        )
        # criando as teques Todos Em andamento e Finalizados
        tabs = ft.Tabs(
                selected_index=0, # para fixa no primeiro texto
                on_change=self.tabs_changed,
                tabs=[
                    ft.Tab(text='Todos'),
                    ft.Tab(text='Em andamento'),
                    ft.Tab(text='Finalizados')
                ]
        )

        tasks = self.tasks_container() # aqui e para atribuir a funcao a uma variavel
        retu = input_bar, tabs, tasks
        return retu
       # self.page.add(input_bar, tabs, tasks)
        
    

#ft.app(ToDo)