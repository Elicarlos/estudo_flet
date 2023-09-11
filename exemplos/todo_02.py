import flet as ft

def main(page: ft.Page):
    def add_task(e):
        if not nova_tarefa.value:
            nova_tarefa.error_text = 'Campo Obrigatorio'
            page.update()
        
        else:
            tarefas.controls.append(ft.Checkbox(label=nova_tarefa.value))
            nova_tarefa.value = ''
            view.update()
    
    nova_tarefa = ft.TextField(hint_text='O que voce deseja fazer',  expand=True)
    
    tarefas = ft.Column()
    view = ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    nova_tarefa,
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task),
                ],
            ),
            tarefas,
        ],
    )
   
    page.horizontal_alignment = 'center'
    page.add(view)

ft.app(target=main)