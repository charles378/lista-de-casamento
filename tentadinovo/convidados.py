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