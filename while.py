numero_sorteado = 15
chances = 5

while chances != 0:
    print(f"Você tem {chances} chances") #Adicionar um f depois do print cria um printf
    numero_escolhido = int(input("informe numero entre 1 e 20: "))
    if(numero_escolhido != numero_sorteado):
        print("Essa não é a resposta correta")
        if(numero_escolhido > numero_sorteado): print("O número que você procura é menor")
        else: print("O número que você procura é maior")
        print()
        chances -= 1
    elif(chances == 0):
        print("Você perdeu!")
    if(numero_escolhido == numero_sorteado):
        print("Voce acertou!")
        break
    