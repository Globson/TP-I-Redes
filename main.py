from slottedAloha512 import SlottedAloha

if __name__ == "__main__":
    n = int(input("Entre com a quantidade de estacoes:"))
    TemposAloha = SlottedAloha(n)
    print("\nOs tempos do algoritmo Slotted Aloha foram:\n",TemposAloha)
    pass
