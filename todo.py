import flet as ft

def main(page: ft.Page):
   
    def add_taks(e):
        # page.add(ft.Checkbox(label=nova_tarefa.value))
        tarefa_view.controls.append(ft.Checkbox(label=nova_tarefa.value))
        # limpa a tela 
        nova_tarefa.value = ''
        page.update()

    nova_tarefa = ft.TextField(hint_text='O que voce precisa fazer?', expand=True)
    tarefa_view = ft.Column()
    view=ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    nova_tarefa,
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_taks),
                ],
            ),
            tarefa_view,
        ],
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)
ft.app(target=main)