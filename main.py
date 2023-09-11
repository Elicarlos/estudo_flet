import os
import flet as ft
from models import Produto as pd


def main(page: ft.Page):
    page.title = 'Etiquetario'
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER

    

    def salvar(e):
    
        if not nome_produto.value:
            nome_produto.error_text = 'Insira um nome para o produto'
            page.update()
        
        elif not preco_produto.value:
            preco_produto.error_text = 'Campo obrigatorio'
            page.update()
        else:
            name = nome_produto.value
            # page.clean()
            produto = pd.create(descricao=name)
            produto.save()
            nome_produto.value = ''
            

    nome_produto  = ft.TextField(label="Nome do produto", width=400)
    preco_produto  = ft.TextField(label="Preco", width=100)
    page.add( ft.Row(
            [
                nome_produto,
                preco_produto,
                ft.ElevatedButton(text='Salvar',on_click=salvar),
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        )
    
   

ft.app(target=main)