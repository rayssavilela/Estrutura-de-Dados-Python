class ListadeTarefas:
    def __init__(self):
        self.equipe_a = set()
        self.equipe_b = set()

    def IniciandoLista(self):
        equipeA = input("Equipe A = ")
        equipeB = input("Equipe B = ")

        # Verifica se veio vazio
        if not equipeA.strip() or not equipeB.strip():
            print("ERRO: As equipes não podem estar vazias!")
            return self.IniciandoLista()
        
        self.equipe_a = set(
            p.strip().lower() for p in equipeA.split(',') #split(',') Divide a string usando a vírgula como separador.
        ) #strip() Remove espaços do começo e do final.
        #for p in principais.split(',') Percorre cada item da lista.
        #.lower() Transforma tudo em minúsculo.

        self.equipe_b = set(
            p.strip().lower() for p in equipeB.split(',')
        )

    def JuntandoListas(self):
        # retorna a união
        return self.equipe_a.union(self.equipe_b)

    def RetirandoElemento(self):

        uniao = self.JuntandoListas()

        print(f"Lista atual: {uniao}")

        retirar = input(
            "Digite qual elemento deseja tirar da lista: "
        ).strip().lower()

        if retirar in uniao:

            uniao.remove(retirar)

            print(f"\nElemento '{retirar}' removido!")

            print(f"Nova lista: {uniao}")

        else:
            print("\nEsse elemento não existe na lista.")
        
lista = ListadeTarefas()

lista.IniciandoLista()

lista.RetirandoElemento()