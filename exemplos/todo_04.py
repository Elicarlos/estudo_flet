import flet as ft

class Tarefa(ft.UserControl):
    def __init__(self, nome_tarefa, tarefa_delete):
        super().__init__()
        self.nome_tarefa = nome_tarefa
        self.tarefa_delete = tarefa_delete

    def build(self):
        self.display_tarefa = ft.Checkbox(value=False, label=self.nome_tarefa)
        self.edit_nome = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment="spaceBetween",
            vertical_alignment="center",    
            controls=[
                self.display_tarefa,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip='Edite a tarefa',
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip='Delete a tarefa',
                            on_click=self.delete_clicked,
                        ),

                    ],

                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_nome,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip='Atualiza tarefa',
                    on_click=self.save_clicked,
                )
                
            ],
        )
        return ft.Column(controls=[self.display_view, self.edit_view])
    

    def edit_clicked(self, e):
        self.edit_nome.value = self.display_tarefa.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_tarefa.label = self.edit_nome.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.tarefa_delete(self)


class TodoApp(ft.UserControl):
    def build(self):
        self.nova_tarefa = ft.TextField(hint_text='O que deseja fazer? ', expand=True)
        self.tarefas = ft.Column()

        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.nova_tarefa,
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.tarefas,
            ],
        )
    
    def add_clicked(self, e):
        tarefa = Tarefa(self.nova_tarefa.value, self.tarefa_delete)
        self.tarefas.controls.append(tarefa)
        self.nova_tarefa.value = ""
        self.update()

    def tarefa_delete(self, tarefa):
        self.tarefas.controls.remove(tarefa)
        self.update()

    
def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = "center"
    page.update()

    # create application instance
    app = TodoApp()

    # add application's root control to the page
    page.add(app)

ft.app(target=main)



    


