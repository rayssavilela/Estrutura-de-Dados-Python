class Estoque:

    def __init__(self):
        self.sistema_estoque = {}

    def incluir_estoque(self):

        while True:
            item = input("Digite o nome do produto (Digite sair para encerrar): ")
            
            if item.lower() == 'sair':
                break

            quantidade = int(input("Digite a quantidade: "))

            self.sistema_estoque[item] = quantidade

    
    def saida(self):

        print(f'Estoque de produtos:\n{self.sistema_estoque}')

estoque = Estoque()

estoque.incluir_estoque()
estoque.saida()

