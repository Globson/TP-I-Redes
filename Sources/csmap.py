from random import randint

def CSMAp (n):
    
    Tempo = [1 for i in range(n)]
    Pronto = []
    Enviados = [0 for i in range(n)]
    Estacoes = 0
    Tempos_Finais = [0,0]
    Primeiro = False
    Ultimo = False
    Tempo_Atual = 2
    Restantes = n
    contador = 1
    aux = []
    for i in range (n):
        delay = randint(1,n)
        Tempo[i] += delay
        print(delay)
    
    while (Ultimo == False):

        for i in range (n):
            #Passagem de tempo para estações que não sofreram colisões 
            # nem foram enviadas
            if (Tempo_Atual - Tempo[i]) == 1 and Enviados[i] == 0:
                Tempo[i] = Tempo_Atual

        for i in range (n):
            #Se cair no 1% de chance e a estação não estiver esperando 
            # devido a uma colisão ou já foi enviada ela está pronta
            if (Tempo[i] == Tempo_Atual):
                Pronto.append(i)

        Estacoes = len(Pronto)

        for i in range (Estacoes):
            if (randint(1,100)!=42):
                aux.append(Pronto[i])

        Estacoes = len(aux)
        #Se houver colisão, as estações relacionadas esperam por um tempo aleatório
        if (Estacoes > 1):
            for i in range(Estacoes):
                delay = randint(1, n)
                Tempo[aux[i]] += delay
            #print(Tempo)
        #Se apenas 1 tentar enviar esse é enviado
        elif (Estacoes == 1):
            Enviados[aux[0]] = 1
            Restantes -= 1
            print(Tempo, contador, Tempo[aux[0]])
            #contador+=1
            if (Primeiro == False):
                Primeiro = True
                Tempos_Finais[0] = Tempo[aux[0]]
            
            if (Restantes == 0):
                Tempos_Finais[1] = Tempo[aux[0]]
                Ultimo = True
            #del Tempo[Pronto[0]]
            
        Pronto = []
        aux = []
        Tempo_Atual += 1
        
    return Tempos_Finais
            
    