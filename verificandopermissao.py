class Permissoes:
    def __init__(self):
        self.permissoes_principais = set()
        self.permissoes_solicitadas = set()

    def ler_permissoes(self):
        principais = input("Permissões principais: ")
        solicitadas = input("Permissões solicitadas: ")

        self.permissoes_principais = set(
            p.strip().lower() for p in principais.split(',')
        ) #Essa linha pega uma string com permissões separadas por vírgula e transforma em um conjunto (set) padronizado, 
        #removendo espaços extras e convertendo tudo para minúsculo.

        self.permissoes_solicitadas = set(
            p.strip().lower() for p in solicitadas.split(',')
        )

    def verificar_permissoes(self):

        eh_subconjunto = self.permissoes_solicitadas.issubset(
            self.permissoes_principais
        )

        if eh_subconjunto:
            return "As permissões solicitadas fazem parte das permissões principais."
        else:
            faltando = (
                self.permissoes_solicitadas -
                self.permissoes_principais
            )

            return (
                f"As permissões {faltando} "
                f"não fazem parte das permissões principais."
            )


permissao = Permissoes()

permissao.ler_permissoes()

print(permissao.verificar_permissoes())