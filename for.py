# Lista todos os valores de 0 até 9
"""
for variavel in range(10):
    print(variavel)
print()
"""
# Lista todos os valores de 1 até 9
"""
for variavel in range(1,10):
    print(variavel)
print()
"""
#Começa em 1 e vai até 11, pulando de 3 em 3 numeros (1,4,7,10)
"""
for variavel in range(1,12,3):
    print(variavel)
"""
nota_total = 0
for i in range(3):
    nota = float(input(f"Informe a sua {i+1}º nota: "))
    nota_total += nota
print(f"\nSua media é: {nota_total/3}")
