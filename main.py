from Sources.slottedAloha import SlottedAloha
from Sources.csmap import CSMAp
from Sources.recuobinario import CSMAp_recuobinario
from statistics import fmean,stdev
def CalculosEstatisticos(VetorTPrimeiro,VetorTTodos): #Funcao para calcular medias e desvios padrao, recebe vetor contendo 33 valores de tempo gastos pela primeira maquina para enviar e todas para enviar, respectivamente.
    print("\n\t->O tempo medio para a primeira maquina enviar foi de: %.5f microssegundos" % fmean(VetorTPrimeiro))
    print("\n\t->O desvio padrao do tempo para a primeira maquina enviar foi de: %.5f microssegundos" % stdev(VetorTPrimeiro))
    print("\n\t->O tempo medio para todas as maquinas enviarem foi de: %.5f microssegundos" % fmean(VetorTTodos))
    print("\n\t->O desvio padrao do tempo para todas as maquinas enviarem enviar foi de: %.5f microssegundos" % stdev(VetorTTodos))

if __name__ == "__main__":
    while(1): 
        n = int(input("Entre com a quantidade de maquinas:"))  #Menu
        print("Escolha o algoritmo desejado:\n\t1 - Slotted Aloha\n\t2 - CSMA p-persistente\n\t3 - Algoritmo de recuo binario exponencial")
        a=0
        while(a != 1 and a != 2 and a!=3):
            a = int(input("Entre:"))
            if(a != 1 and a != 2 and a!=3):
                print("Opcao invalida!")
        if(a==1): #Slotted Aloha
            VetorTEnviadoPrimeiro = [] #Vetor para armazenar tempos da primeira maquina enviar em cada uma das 33 instancias
            VetorTTotal = [] #Vetor para armazenar tempos para todas as maquinas enviarem em cada uma das 33 instancias
            for k in range (33):
                TemposAloha = SlottedAloha(n) #Chamando SlottedAloha, funcao retorna um vetor com tempo necessario para enviar de cada uma das maquinas
                MenorT=TemposAloha[0]
                for j in range(n): #Pegando menor tempo, referente a primeira maquina que enviou
                    if(MenorT>TemposAloha[j]):
                        MenorT = TemposAloha[j]
                VetorTEnviadoPrimeiro.append(MenorT) #Adicionando menor tempo ao vetor de primeiras maquinas a enviar
                Total=TemposAloha[0]
                for i in range(n):  # Pegando maior tempo, referente a ultima maquina que enviou
                    if(Total<TemposAloha[i]):
                        Total = TemposAloha[i]
                VetorTTotal.append(Total) #Adicionando maior tempo ao vetor de tempo total para maquinas a enviar
            CalculosEstatisticos(VetorTEnviadoPrimeiro,VetorTTotal) #chamando funcao para calcular estatisticas e imprimir resultado
        if(a==2):
            VetorTEnviadoPrimeiro = []
            VetorTTotal = []
            for k in range (33):
                Tempos_CSMAp = CSMAp(n) #Chamando CSMAp, funcao retorna vetor com duas posicoes, referente ao tempo do primeiro enviar e todas maquinas enviarem
                VetorTEnviadoPrimeiro.append(Tempos_CSMAp[0]*51.2) #Adicionando ao vetor valor em tempo da primeira maquina a enviar
                VetorTTotal.append(Tempos_CSMAp[1]*51.2) #Adicionando ao vetor valor em tempo de todas maquinas enviarem
            CalculosEstatisticos(VetorTEnviadoPrimeiro,VetorTTotal) #chamando funcao para calcular estatisticas e imprimir resultado
        if(a==3):
            VetorTEnviadoPrimeiro = []
            VetorTTotal = []
            for k in range(33):
                Tempos_CSMApRecuoBinario = CSMAp_recuobinario(n) #Chamando CSMAp com recuo binario, funcao retorna vetor com duas posicoes, referente ao tempo do primeiro enviar e todas maquinas enviarem ou em caso de erro false.
                if(Tempos_CSMApRecuoBinario==False): #Caso aconteça um erro no tratamento de colisoes, algoritmo é interrompido e a mensagem False, referente a um erro é retornada
                    print("\n\tERRO! Houveram mais de 16 colisoes no algoritmo de recuo binario!")
                else: #Caso nao retorne False
                    VetorTEnviadoPrimeiro.append(Tempos_CSMApRecuoBinario[0]*51.2) #Adicionando ao vetor valor em tempo da primeira maquina a enviar
                    VetorTTotal.append(Tempos_CSMApRecuoBinario[1]*51.2) #Adicionando ao vetor valor em tempo de todas maquinas enviarem
            if(len(VetorTEnviadoPrimeiro) > 0 and len(VetorTTotal) > 0):
                CalculosEstatisticos(VetorTEnviadoPrimeiro, VetorTTotal) #chamando funcao para calcular estatisticas e imprimir resultado
        print("\n\nDeseja voltar ao menu inicial?\n\t1 - Sim\n\t2 - Nao")
        b=0
        while(b!=1 and b!=2): #Pequeno menu que pergunta se usuario deseja finalizar ou voltar ao menu inicial.
            b=int(input("Entre:"))
            if(b != 1 and b != 2):
                print("Opcao invalida!")
        if(b==2):
            break
    pass
