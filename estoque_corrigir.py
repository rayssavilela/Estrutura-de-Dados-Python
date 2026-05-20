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

    def corrigir_estoque(self):
        nome_item = input("Nome do produto a ser atualizado: ")

        if nome_item in self.sistema_estoque:
            nova_quantidade = int(input("Nova quantidade: "))
            self.sistema_estoque[nome_item] = nova_quantidade
            print("Quantidade atualizada com sucesso!")
            print(f'Estoque atualizado:\n{self.sistema_estoque}')
        else:
            print("Produto não encontrado no estoque.")

estoque = Estoque()

estoque.incluir_estoque()
estoque.saida()
estoque.corrigir_estoque()
