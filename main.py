from Sources.slottedAloha import SlottedAloha

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
            TemposAloha = SlottedAloha(n)
            print("\nOs tempos para as maquinas enviarem com o algoritmo Slotted Aloha foram:\n",TemposAloha)
            MenorT=TemposAloha[0]
            for j in range(n):
                if(MenorT>TemposAloha[j]):
                    MenorT = TemposAloha[j]
            print("O tempo necessario para a primeira maquina enviar foi de: ",MenorT," microssegundos")
            Total=TemposAloha[0]
            for i in range(n):
                if(Total<TemposAloha[i]):
                    Total = TemposAloha[i]
            print("O tempo total foi: ",Total," microssegundos")
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
