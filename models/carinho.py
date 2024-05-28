from models.produto import Produto


class Carrinho:

    def __init__(self) -> None:
        self.__carrinho: list[dict[Produto, int]] = []

    def cadastrar(self, produto: Produto) -> None:
        qtd: int = self.__buscar_produto_no_carrinho(produto)
        self.__carrinho.append({produto: qtd})

    def __buscar_produto_no_carrinho(self, produto: Produto) -> int:
        for prod in self.__carrinho:
            if prod.get(produto):
                return prod.get(produto) + 1
        return 1

    def listar(self) -> None:
        for prod in self.__carrinho:
            for produto, qtd in prod.items():
                print(f"{produto}")
                print(f"Quantidade: {qtd}")

    def comprar(self):
        pass

