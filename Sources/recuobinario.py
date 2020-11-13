from random import randint


def CSMAp_recuobinario(n):

    Tempo = [1 for i in range(n)]
    Pronto = []
    Enviados = [0 for i in range(n)]
    Estacoes = 0
    Tempos_Finais = [0, 0]
    Primeiro = False
    Ultimo = False
    Tempo_Atual = 2
    Restantes = n

    while (Ultimo == False):

        for i in range(n):
            #Passagem de tempo para estações que não sofreram colisões
            # nem foram enviadas
            if Tempo[i] < Tempo_Atual and Enviados[i] == 0:
                Tempo[i] = Tempo_Atual

        for i in range(n):
            #Se cair no 1% de chance e a estação não estiver esperando
            # devido a uma colisão ou já foi enviada ela está pronta
            if (randint(1, 100) == 1) and Tempo[i] == Tempo_Atual:
                Pronto.append(i)

        Estacoes = len(Pronto)
        #Se houver colisão, as estações relacionadas esperam por um tempo aleatório
        if (Estacoes > 1):  #Mexi dentro desse escopo @Saulim! Tentando estabelecer uma forma de sortear os novos tempos com o uso de rand(0,(2^quantidade de colisoes)-1)
            ColidiuDnv=[]
            QuantColisoes=0
            for i in range(Estacoes):
                QuantColisoes+=1
                Tempo[Pronto[i]] += randint(0,(2**QuantColisoes)-1)
            while True:
                for j in range(Estacoes-1):
                    for k in range(1,Estacoes):
                      if(Tempo[Pronto[j]] == Tempo[Pronto[k]]):
                            ColidiuDnv.append(j)
                            ColidiuDnv.append(k)
                if(len(ColidiuDnv)>0):
                    QuantColisoes+=1
                    IndexColidiu=0
                    for i in ColidiuDnv:
                        if(QuantColisoes>0 and QuantColisoes<=10):
                            Tempo[Pronto[i]] += randint(0, (2**QuantColisoes)-1)
                        elif (QuantColisoes>0 and QuantColisoes <= 16):
                            Tempo[Pronto[i]] += randint(0, (2**10)-1)
                        else:
                            return False #ERRO!
                        del(ColidiuDnv[IndexColidiu])
                        IndexColidiu+=1
                    IndexColidiu=0
            if (len(ColidiuDnv>0)):
                break

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
