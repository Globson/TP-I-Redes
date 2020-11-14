from random import randint

def SlottedAloha(n):
    Tempo = [0 for i in range(n)]   #Vetor armazena tempo para cada maquina
    Pronto = [0 for i in range(n)]  #Vetor indica intencao de maquina enviar
    VetorAux = [0 for i in range(n)] #Vetor armazena index de maquinas que colidiram
    Enviado = [0 for i in range(n)] #Vetor indica maquinas que ja enviaram
    TemposFinais = [0 for i in range(n)] #Vetor usado para armazenar tempo que cada maquina necessitou para enviar com sucesso
    for i in range(n):
        Tempo[i] = 512  #inicialmente todas as maquinas tentam enviar no slot 2
    Gatilho = 0 #usado como condicao do while abaixo
    TempoAtual = 0 #Tempo atual do slot
    Aux = 0  #Variavel usada para controle
    Index = 0 #Variavel contadora de index
    Colisao = 0 #Variavel que detecta colisoes
    while(Gatilho == 0):
        for i in range(n):
            if(TempoAtual == Tempo[i] and Enviado[i] == 0): #Caso a maquina ainda nao tenha enviado e esteja no seu tempo de enviar ela é marcada como pronta para enviar.
                Pronto[i] = 1
        for i in range(n):
            if(Pronto[i] == 1 and Aux == 0): #Detectando maquinas que querem enviar no tempo atual
                Aux = 1
                VetorAux[Index] = i
                Index += 1
            elif(Pronto[i] == 1 and Aux == 1): #Caso Aux seja 1, uma ou mais maquinas tambem querem enviar, logo houve uma colisao
                Colisao = 1
                VetorAux[Index] = i
                Index += 1
        if(Colisao == 1): #Caso haja colisao, os novos tempos das respectivas maquinas serao sorteados e somados ao atual.
            for i in range(Index):
                rand = randint(1,n) * 512    # intervalo do rand de 1 ate n para realizar sorteio
                Tempo[VetorAux[i]] = Tempo[VetorAux[i]]+rand
        if(Colisao != 1 and Aux == 1): #Caso nao houve colisao e pelo menos uma maquina deseja enviar, a maquina é marcada como enviada com sucesso.
            Enviado[VetorAux[Index-1]] = 1
            microssegundo = TempoAtual/10 #Tempo é salvo em microssegundos
            TemposFinais[VetorAux[Index-1]] = microssegundo  #Tempo necessario para a maquina enviar é salvo no vetor e no final o vetor é retornado pela funcao.
            Gatilho = 1
        for i in range(n):
            if(Enviado[i] == 0):  #Se pelo menos uma maquina ainda nao enviou, gatilho continua 0 e nova iteracao acontece
                Gatilho = 0
        TempoAtual += 512 #Tempo atual do slot é incrementado
        for i in range(n):
            Pronto[i] = 0 #Variaveis sendo zeradas para proxima iteracao
        Aux = 0
        Colisao = 0
        Index = 0
    return TemposFinais #Vetor de tempos é retornado

