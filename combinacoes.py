'''
requisitos importar 'itertools'
'''

import itertools

mapa = { 0:" ", 1:", "}

entrada = 'inicio'

while entrada != '0':
    entrada = input("Forneça uma frase (Digite '0' para encerrar): ")
    if entrada != '0':
        listaPalavras = entrada.split()
        # print("listaPalavras=",listaPalavras)
        # print("len(listaPalavras)=",len(listaPalavras))

        # gerando o arranjo (com repetição) de possiblidades de um conjunto de elementos binários em função da quantidade de palavras da frase
        possibilidades = list(itertools.product([0,1], repeat=len(listaPalavras)-1))
        # print("possibilidades=",possibilidades)
        # print("len(possibilidades)=",len(possibilidades))

        # outra abordagem
        # bin = [0,1]
        # possibilidades = [ (x,y,z) for x in bin for y in bin for z in bin ]

        combinacoes = []
        for arranjo in possibilidades:
            # print("arranjo=",arranjo)
            frases = []
            i=0
            frase=""
            for palavra in listaPalavras:
                # print("\tpalavra=",palavra)
                if i < len(listaPalavras)-1:
                    frase += palavra + mapa[arranjo[i]]    
                else:
                    frase += palavra
                i=i+1
            # print("\tfrase= "+frase)
            frases.append(frase)
            combinacoes.append(frases)

        print("combinacoes =",combinacoes)


