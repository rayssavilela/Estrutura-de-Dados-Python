class Workshop:

    def __init__(self):

        self.participantes = { 

            "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

            "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

        }

    def solicitar_participante(self):

        while True:
            nome_participante = input("Nome do participante a ser removido: ").strip().title()
            encontrado = False

            for workshop, participantes in self.participantes.items():  #workshop é os keys do dicionario, ja participantes seria o valor 
                if nome_participante in participantes:
                    participantes.remove(nome_participante) #usa o remove de conjuntos para remover o objeto solicitada

                    print(
                        f"{nome_participante} removido do {workshop}!"
                    )
                    encontrado = True
                    break

            if encontrado:
                break
            else:
                print(
                    f'O participante "{nome_participante}" não foi encontrado.'
                )
              

    def mostrar_lista_atualizada(self):
        print(f'Lista atualizada de participantes:\n{self.participantes}')

participantes = Workshop()

participantes.solicitar_participante()
participantes.mostrar_lista_atualizada()