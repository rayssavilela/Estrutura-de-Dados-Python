class CompararListas:

    def __init__(self):
        self.laura = set()
        self.ana = set()

    def InserirItens(self):

        self.laura = set(
            input("Lista da Laura: ").title().split(", ")
        )

        self.ana = set(
            input("Lista da Ana: ").title().split(", ")
        )

    def ItensComuns(self):

        return self.laura.intersection(self.ana)

    def ExclusivosLaura(self):

        return self.laura.difference(self.ana)

    def ExclusivosAna(self):

        return self.ana.difference(self.laura)

    def MostrarResultados(self):

        print(
            f"Itens em ambas as listas: "
            f"{', '.join(self.ItensComuns())}"
        )

        print(
            f"Itens exclusivos de Laura: "
            f"{', '.join(self.ExclusivosLaura())}"
        )

        print(
            f"Itens exclusivos de Ana: "
            f"{', '.join(self.ExclusivosAna())}"
        )
"""
O .join() serve para juntar elementos de uma lista, tupla ou conjunto em uma única string.

Exemplo simples:

nomes = ["Ana", "Laura", "Maria"]

resultado = ", ".join(nomes)

print(resultado)

Saída:

Ana, Laura, Maria
"""


comparar = CompararListas()

comparar.InserirItens()

comparar.MostrarResultados()