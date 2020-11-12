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
    
    
    while (Ultimo == False):

        for i in range (n):
            #Passagem de tempo para estações que não sofreram colisões 
            # nem foram enviadas
            if Tempo[i] < Tempo_Atual and Enviados[i] == 0:
                Tempo[i] = Tempo_Atual

        for i in range (n):
            #Se cair no 1% de chance e a estação não estiver esperando 
            # devido a uma colisão ou já foi enviada ela está pronta
            if (randint(1, 100) == 1) and Tempo[i] == Tempo_Atual:
                Pronto.append(i)

        Estacoes = len(Pronto)
        #Se houver colisão, as estações relacionadas esperam por um tempo aleatório
        if (Estacoes > 1):
            for i in range(Estacoes):
                Tempo[Pronto[i]] += randint(1, (n*2))
        #Se apenas 1 tentar enviar esse é enviado
        elif (Estacoes == 1):
            Enviados[Pronto[0]] = 1
            Restantes -= 1
            
            if (Primeiro == False):
                Primeiro = True
                Tempos_Finais[0] = Tempo[Pronto[0]]
            
            if (Restantes == 0):
                Tempos_Finais[1] = Tempo[Pronto[0]]
                Ultimo = True

        Pronto = []
        Tempo_Atual += 1
        
    return Tempos_Finais
            
    