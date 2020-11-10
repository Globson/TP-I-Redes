from random import randint


def SlottedAloha():
    print("O tamanho do frame é de 51,2 microsegundos\n")
    n = int(input("Entre com a quantidade de estacoes:"))
    Tempo = [0 for i in range(n)]
    Pronto = [0 for i in range(n)]
    VetorAux = [0 for i in range(n)]
    Enviado = [0 for i in range(n)]

    for i in range(n):
        rand = randint(0, 60) * 512
        Tempo[i] = rand
        microssegundos = Tempo[i]/10
        print("A estação ", i+1, " ira enviar no tempo:  ", microssegundos, " microssegundos")
    Gatilho = 0
    TempoAtual = 0
    Aux = 0
    Index = 0
    Colisao = 0
    while(Gatilho == 0):
        for i in range(n):
            if(TempoAtual == Tempo[i] and Enviado[i] == 0):
                Pronto[i] = 1

        for i in range(n):
            if(Pronto[i] == 1 and Aux == 0):
                Aux = 1
                VetorAux[Index] = i
                Index += 1
            elif(Pronto[i] == 1 and Aux == 1):
                Colisao = 1
                VetorAux[Index] = i
                Index += 1
        if(Colisao == 1):
            print("\nColisao detectada nas estacoes:\n")
            for i in range(Index):
                rand = randint(1, 30) * 512
                Tempo[VetorAux[i]] = Tempo[VetorAux[i]]+rand
                print("\t( ", VetorAux[i]+1, " ", end=')')
            if(Index > 1):
                print("\n\nO novo tempo de envio de cada estacao sera: ")
            for i in range(Index):
                print("\tEstacao: ", VetorAux[i]+1, " -> ", (Tempo[VetorAux[i]]/10))
        if(Colisao != 1 and Aux == 1):
            Enviado[VetorAux[Index-1]] = 1
            microssegundo = TempoAtual/10
            print("A estacao ", VetorAux[Index-1]+1," enviou com sucesso! Tempo: ", microssegundo," microssegundos")
            Gatilho = 1
        for i in range(n):
            if(Enviado[i] == 0):
                Gatilho = 0
        TempoAtual += 512
        for i in range(n):
            Pronto[i] = 0
        Aux = 0
        Colisao = 0
        Index = 0


if __name__ == "__main__":
    SlottedAloha()
    pass
