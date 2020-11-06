from random import randint
def SlottedAloha():
    k=1
    print("O tamanho do frame é de 1 segundo\n")
    n = int(input("Entre com a quantiade de estacoes:"))
    Tempo = [0 for i in range(n)]
    Pronto = [0 for i in range(n)]
    VetorAux = [0 for i in range(n)]
    Enviado = [0 for i in range(n)]

    for i in range(n):
        Tempo[i]= randint(1,10)
        print("A estação ",i+1," ira enviar no tempo:  ",Tempo[i])
    Gatilho=0
    TempoAtual=1
    Aux=0
    Index=0
    Colisao=0
    k=1
    while(Gatilho==0):
        for i in range(n):
            if(TempoAtual==Tempo[i] and Enviado[i]==0):
                Pronto[i]=1

        for i in range(n):
            if(Pronto[i]==1 and Aux==0):
                Aux=1
                VetorAux[Index]=i
                Index+=1
            elif(Pronto[i]==1 and Aux==1):
                Colisao=1
                VetorAux[Index]=i
                Index+=1
        if(Colisao==1):
            print("\nColisao detectada nas estacoes:\n")
            for i in range(Index):
                Tempo[VetorAux[i]]=Tempo[VetorAux[i]]+k
                print("\t( ",VetorAux[i]+1," ",end=')')
                k=k*2
            if(Index>1):
                print("\nO novo tempo de envio de cada estacao sera: ")
            for i in range(Index):
                print("Estacao: ",VetorAux[i]+1," -> ",Tempo[VetorAux[i]])
        if(Colisao!=1 and Aux==1):
            Enviado[VetorAux[Index-1]]=1
            print("A estacao ",VetorAux[Index-1]+1, " enviou com sucesso! Tempo: ", TempoAtual)       
            Gatilho=1
        for i in range(n):
            if(Enviado[i]==0):
                Gatilho=0
        TempoAtual+=1
        for i in range(n):
            Pronto[i]=0
        Aux=0
        Colisao=0
        Index=0
if __name__ == "__main__":
    SlottedAloha()
    pass