from random import randint

def SlottedAloha(n):
    print("O tamanho do frame é de 51,2 microsegundos\n")
    Tempo = [0 for i in range(n)]
    Pronto = [0 for i in range(n)]
    VetorAux = [0 for i in range(n)]
    Enviado = [0 for i in range(n)]
    TemposFinais = [0 for i in range(n)]
    print("Inicialmente todas as maquinas transmitirao no tempo 51,2 microssegundos!")
    for i in range(n):
        Tempo[i] = 512
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
            print("\nColisao detectada nas maquinas:\n")
            for i in range(Index):
                rand = randint(1, (n*2)) * 512    # intervalo do rand de 1 ate n*2 para ter uma margem de possibilidades de tempos razoavel
                Tempo[VetorAux[i]] = Tempo[VetorAux[i]]+rand
                print(" ( ",VetorAux[i]+1," ", end=')')
            if(Index > 1):
                print("\n\nO novo tempo de envio de cada maquina sera: ")
            for i in range(Index):
                print("\tmaquina: ", VetorAux[i]+1, " -> ", (Tempo[VetorAux[i]]/10))
        if(Colisao != 1 and Aux == 1):
            Enviado[VetorAux[Index-1]] = 1
            microssegundo = TempoAtual/10
            print("A maquina ", VetorAux[Index-1]+1," enviou com sucesso! Tempo: ", microssegundo," microssegundos")
            TemposFinais[VetorAux[Index-1]] = microssegundo
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
    return TemposFinais

