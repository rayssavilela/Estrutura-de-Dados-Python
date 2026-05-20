class Participantes:

    def __init__(self):

        self.participantes = {

            "Mariana": 25,
            "Carlos": 32,
            "Beatriz": 28,
            "Rafael": 35

        }

    def mostrar_nomes(self):

        print(f"Nomes dos participantes: {', '.join(self.participantes.keys())}") #Retorna as chaves do dicionário

    def mostrar_idades(self):

        print(
            f"Idades dos participantes: "
            f"{', '.join(str(idade) for idade in self.participantes.values())}" #Retorna os valores do dicionário
        )

    def mostrar_participantes(self):

        print("Participantes e suas idades:")

        for nome, idade in self.participantes.items(): #Retorna pares (chave, valor) como tuplas

            print(f"- {nome}: {idade} anos")



lista = Participantes()

lista.mostrar_nomes()
lista.mostrar_idades()
lista.mostrar_participantes()