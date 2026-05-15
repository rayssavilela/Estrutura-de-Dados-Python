class ListaConvidados:

    def __init__(self):
        self.convidados = set()


    def __str__(self):
        return f'{self.convidados}'
    
    def Criar_lista(self):

        while True:
            nome = input("Digite o nome do convidado: ").strip()

            if nome.lower() == "sair":
                break

            self.convidados.add(nome.title())
            

        
            
lista = ListaConvidados()

lista.Criar_lista()

print(lista.convidados)