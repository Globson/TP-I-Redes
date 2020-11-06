import random

def envio():
    n = 0
    menor = 0
    estacoes = []
    print('Quantas estações deseja usar?')
    n = int(input())
    
    for i in range(n):
        estacoes.append(0)    

    while 1:
        if(estacoes[1] > estacoes[0]):
            estacoes.pop(0)
            print(estacoes[0])
            break
        else:
            menor = estacoes[0]
            for i in range(n):
                if estacoes[i] == menor:
                    estacoes[i] += random.randint(1,5)
        
        estacoes.sort()
       # print(estacoes)
    
    return 0
            
    
cero = envio()

