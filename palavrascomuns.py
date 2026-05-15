from collections import Counter

class PalavrasComuns:
    def __init__(self):
        self.tx1 = []
        self.tx2 = []

    def __str__(self):
        return f'{self.tx1} \n {self.tx2}'
    
    def InserirTexto(self):
        
            texto1 = input("Texto 1: ").strip()
            texto2 = input("Texto 2: ").strip()
            

            self.tx1.extend(texto1.title().split()) #Extend adiciona cada palavra na lista separadamente e se for feito com append nesse caso, eu vou criar lista sobre lista
            self.tx2.extend(texto2.title().split()) #Aqui quero fazer que a lista considere o texto em "Partes" para conseguir contar as palavras iguais


    def CombinarPalavras(self):
        contador1 = Counter(self.tx1)
        contador2 = Counter(self.tx2)

        duplicadas = {}

        for palavra in contador1: #Percorre na lista
            if palavra in contador2: #Pergunta se existe na lista
                duplicadas[palavra] = contador1[palavra] + contador2[palavra]

        return duplicadas
        
Combinar = PalavrasComuns()

Combinar.InserirTexto()

print(Combinar.CombinarPalavras())

        

"""
Outro método usando CONJUNTOS:
texto1 = set(input("Texto 1: ").lower().split()) 

texto2 = set(input("Texto 2: ").lower().split()) 

comuns = texto1.intersection(texto2) 

print(f"Palavras em comum: {comuns}") 

Insersection verifica palavras comuns
"""
