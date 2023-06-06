# Exemplo: Idade de um indíviduo
idade = 17

if(idade >=18): print("A pessoa é maior de idade")
else: print("A pessoa não é maior de idade")

# Exemplo: media da pessoa e presença do individuo

media = float(input("A media da pessoa: "))
presenca = int(input("Qual foi a sua presença: "))

if(media>=7 and presenca>=75): 
    print("A pessoa está aprovada")
elif(media>3 and not(presenca<75)):
    print("A pessoa vai para a recuperação")
else:
    print("A pessoa está reprovada")