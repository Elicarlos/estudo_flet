import flet as ft

def main(page: ft.Page):
    def add_tarefa(e):
        page.add(ft.Checkbox(label=nova_tarefa.value))
        nova_tarefa.value = ''
        page.update()

    
    nova_tarefa = ft.TextField(hint_text='O que voce deseja fazer? ')

    page.add(nova_tarefa, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_tarefa))

ft.app(target=main)

    
