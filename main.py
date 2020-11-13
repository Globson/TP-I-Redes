from Sources.slottedAloha import SlottedAloha
from Sources.csmap import CSMAp
from Sources.recuobinario import CSMAp_recuobinario
from Sources.recuobinarioAloha import SlottedAlohaRecuo
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
        if(a==2):
            VetorTEnviadoPrimeiro = []
            VetorTTotal = []
            for k in range (33):
                Tempos_CSMAp = CSMAp(n)
                
                
                VetorTEnviadoPrimeiro.append(Tempos_CSMAp[0]*51.2)
                #print("O tempo necessario para a primeira maquina enviar foi de: ",MenorT," microssegundos")
                
                VetorTTotal.append(Tempos_CSMAp[1]*51.2)
                #print("O tempo total foi: ",Total," microssegundos")
            CalculosEstatisticos(VetorTEnviadoPrimeiro,VetorTTotal)
        if(a==3):
            VetorTEnviadoPrimeiro = []
            VetorTTotal = []
            for k in range(33):
                Tempos_CSMApRecuoBinario = CSMAp_recuobinario(n)
                if(Tempos_CSMApRecuoBinario==False):
                    print("\n\tERRO! Houveram mais de 16 colisoes no algoritmo de recuo binario!")
                else:
                    VetorTEnviadoPrimeiro.append(Tempos_CSMApRecuoBinario[0]*51.2)
                    #print("O tempo necessario para a primeira maquina enviar foi de: ",MenorT," microssegundos")

                    VetorTTotal.append(Tempos_CSMApRecuoBinario[1]*51.2)
                    #print("O tempo total foi: ",Total," microssegundos")
            CalculosEstatisticos(VetorTEnviadoPrimeiro, VetorTTotal)
        # if(a == 4):
            # VetorTEnviadoPrimeiro = []
            # VetorTTotal = []
            # for k in range(33):
                # Tempos_CSMApRecuoBinario = SlottedAlohaRecuo(n)
                # if(Tempos_CSMApRecuoBinario == False):
                    # print(
                        # "\n\tERRO! Houveram mais de 16 colisoes no algoritmo de recuo binario!")
                # else:
                    # MenorT = Tempos_CSMApRecuoBinario[0]
                    # for j in range(n):
                        # if(MenorT > Tempos_CSMApRecuoBinario[j]):
                            # MenorT = Tempos_CSMApRecuoBinario[j]
                    # VetorTEnviadoPrimeiro.append(MenorT)
                    # Total = Tempos_CSMApRecuoBinario[0]
                    # for i in range(n):
                        # if(Total < Tempos_CSMApRecuoBinario[i]):
                            # Total = Tempos_CSMApRecuoBinario[i]
                    # VetorTTotal.append(Total)
                # print(VetorTEnviadoPrimeiro)
                # print(VetorTTotal)
            # CalculosEstatisticos(VetorTEnviadoPrimeiro, VetorTTotal)
        print("\n\nDeseja voltar ao menu inicial?\n\t1 - Sim\n\t2 - Nao")
        b=0
        while(b!=1 and b!=2):
            b=int(input("Entre:"))
            if(b != 1 and b != 2):
                print("Opcao invalida!")
        if(b==2):
            break
    pass
