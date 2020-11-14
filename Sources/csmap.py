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
    aux = []
    #Considerando que todas as estações colidirão no segundo slot
    #é atribuido um delay pra cada estação
    for i in range (n):
        delay = randint(1,n)
        Tempo[i] += delay
    
    while (Ultimo == False):

        for i in range (n):
            #Passagem de tempo para estações que não sofreram colisões 
            # nem foram enviadas
            if (Tempo_Atual - Tempo[i]) == 1 and Enviados[i] == 0:
                Tempo[i] = Tempo_Atual

        for i in range (n):
            # Seleciona estações que tempo da estação (com ou sem delay)
            # for igual ao tempo atual
            if (Tempo[i] == Tempo_Atual):
                Pronto.append(i)

        Estacoes = len(Pronto)
            # Pra cada estação que puder enviar no momento atual seleciona 
            # aquelas com probabilidade = 0,01
        for i in range (Estacoes):
            if (randint(1,100)==42):
                aux.append(Pronto[i])

        Estacoes = len(aux)
        #Se houver colisão, as estações relacionadas esperam por um tempo aleatório
        if (Estacoes > 1):
            for i in range(Estacoes):
                delay = randint(1, n)
                Tempo[aux[i]] += delay
        #Se apenas 1 tentar enviar esse é enviado
        elif (Estacoes == 1):
            Enviados[aux[0]] = 1
            Restantes -= 1
            if (Primeiro == False):
                Primeiro = True
                Tempos_Finais[0] = Tempo[aux[0]]
            
            if (Restantes == 0):
                Tempos_Finais[1] = Tempo[aux[0]]
                Ultimo = True
            
        Pronto = []
        aux = []
        Tempo_Atual += 1
        
    return Tempos_Finais  