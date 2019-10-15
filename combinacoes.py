import itertools

def gerador(n, lista, i):
    result=[[]] 
    temp=[]
    if i==n:
        temp.append(lista)
        result.append(temp)
        return
    
    lista.insert(i,0)
    gerador(n, lista, i+1)

    lista.insert(i,1)
    gerador(n, lista, i+1)

n=2
array=[None]*n
print(gerador(2,array, 0))
print(array)

############################# above is trash

mapa = { 0:" ", 1:", "}
combinacoes = [[]]

frase = "eu gosto de café"
listaPalavras = frase.split()
# print("listaPalavras=",listaPalavras)
# print("len(listaPalavras)=",len(listaPalavras))

# gerando o arranjo de possiblidades (com repetição) 
possibilidades = list(itertools.product([0,1], repeat=len(listaPalavras)-1))
# print("possibilidades=",possibilidades)
# print("len(possibilidades)=",len(possibilidades))

# e = possibilidades[1]
# print(type(e[1]))
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

combinacoes.pop(0)
print("combinacoes=",combinacoes)

