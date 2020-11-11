from Sources.slottedAloha import SlottedAloha
from statistics import fmean,stdev

def CalculosEstatisticos(VetorTPrimeiro,VetorTTodos): #Vetor contendo 33 valores de tempo gastos pela primeira maquina para enviar e todas para enviar, respectivamente.
    print("\n\t->O tempo medio para a primeira maquina enviar foi de: %.5f microssegundos" % fmean(VetorTPrimeiro))
    print("\n\t->O desvio padrao do tempo para a primeira maquina enviar foi de: %.5f microssegundos" % stdev(VetorTPrimeiro))
    print("\n\t->O tempo medio para todas as maquinas enviarem foi de: %.5f microssegundos" % fmean(VetorTTodos))
    print("\n\t->O desvio padrao do tempo para todas as maquinas enviarem enviar foi de: %.5f microssegundos" % stdev(VetorTTodos))

if __name__ == "__main__":
    while(1):   
        n = int(input("Entre com a quantidade de maquinas:"))
        print("Escolha o algoritmo desejado:\n\t1 - Slotted Aloha\n\t2 - CSMA p-persistente\n\t3 - Algoritmo de recuo binario exponencial")
        a=0
        while(a != 1 and a != 2 and a!=3):
            a = int(input("Entre:"))
            if(a != 1 and a != 2 and a!=3):
                print("Opcao invalida!")
        if(a==1):
            VetorTEnviadoPrimeiro = []
            VetorTTotal = []
            for k in range (33):
                TemposAloha = SlottedAloha(n)
                #print("\nOs tempos para as maquinas enviarem com o algoritmo Slotted Aloha foram:\n",TemposAloha)
                MenorT=TemposAloha[0]
                for j in range(n):
                    if(MenorT>TemposAloha[j]):
                        MenorT = TemposAloha[j]
                VetorTEnviadoPrimeiro.append(MenorT)
                #print("O tempo necessario para a primeira maquina enviar foi de: ",MenorT," microssegundos")
                Total=TemposAloha[0]
                for i in range(n):
                    if(Total<TemposAloha[i]):
                        Total = TemposAloha[i]
                VetorTTotal.append(Total)
                #print("O tempo total foi: ",Total," microssegundos")
            CalculosEstatisticos(VetorTEnviadoPrimeiro,VetorTTotal)
        #if(a==2):
            #Entrar com parte do CSMA
        #if(a==3):
            #Entrar com parte do algoritmo de recuo
        print("\n\nDeseja voltar ao menu inicial?\n\t1 - Sim\n\t2 - Nao")
        b=0
        while(b!=1 and b!=2):
            b=int(input("Entre:"))
            if(b != 1 and b != 2):
                print("Opcao invalida!")
        if(b==2):
            break
    pass
