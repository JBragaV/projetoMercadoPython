print("Modulo Produto")
from util.utils import arruma_preco


class Produto:

    contador: int = 0

    def __init__(self: object, nome: str, preco: float) -> None:
        self.__nome = nome
        self.__preco = preco
        self.__codigo = Produto.contador
        Produto.contador += 1

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def preco(self) -> str:
        return arruma_preco(self.__preco)

    def __str__(self) -> str:
        return f"{self.codigo}\nNome: {self.nome}\nPreço: {self.preco}"
