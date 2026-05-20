class Vendas:

    def __init__(self):
        
        self.vendas = { 

            "Eletrônicos": [ 

                {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000}, 

                {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500} 

            ], 

            "Eletrodomésticos": [ 

                {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000}, 

                {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800} 

            ], 

            "Livros": [ 

                {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50}, 

                {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100} 

            ] 

        } 

    def total_por_categoria(self):

        for categoria, vendas in self.vendas.items():

            total = 0

            total = sum(
                venda["quantidade"] * venda["valor_unitario"] 
                for venda in vendas
                )

            print(f"{categoria}: R$ {total:.2f}")


v = Vendas()
v.total_por_categoria()
