from models import *

teste = {'prdouto': 'PS5', 'vagaba': 'PS5', 'balela': 'PS5', 'carta': 'PS5'}

teste1 = {'prdouto': 'PS5', 'vagaba': 'PS5', 'balela': 'PS5', 'carta': 'PS5'}
print(teste.keys())
if __name__ == '__main__':
    carrinho = Carrinho()
    ps5 = Produto("PS4", 2500.99)
    ps1 = Produto("PS4", 2500.99)
    xbox = Produto("XBOX Series S", 3500.99)
    carrinho.cadastrar(ps5)
    carrinho.cadastrar(xbox)
    carrinho.cadastrar(ps1)
    carrinho.listar()

