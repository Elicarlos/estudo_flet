from models import Produto
from views import ViewProduto

class Controller():
    def __init__(self):
        self.produto = Produto()
        self.view_produto = ViewProduto()