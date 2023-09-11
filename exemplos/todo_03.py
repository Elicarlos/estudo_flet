import flet as ft

class TodoApp(ft.UserControl):
    def build(self):
        self.nova_tarefa = ft.TextField(hint_text='O que deseja fazer?')
        self.tarefa = ft.Column()

        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.nova_tarefa,
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_tarefa),
                    ],
                ),
                self.tarefa,
            ]
        )

    def add_tarefa(self,e):
        if not self.nova_tarefa.value:
            self.nova_tarefa.error_text = 'Campo Obrigatorio'

        else:
            self.tarefa.controls.append(ft.Checkbox(label=self.nova_tarefa.value))
            self.nova_tarefa.value = ''
            self.update()

def main(page: ft.Page):
    page.title = 'Todo List'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = TodoApp()
    todo1 = TodoApp()
    todo2 = TodoApp()
    page.add(todo, todo1, todo2)

ft.app(target=main)

