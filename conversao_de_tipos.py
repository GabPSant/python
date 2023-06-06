# Conversão de Tipos
idade = '26'
numero1 = '10'
numero2 = '20'

#print(numero1 + numero2) #1020
print(idade, type(idade))
idade_inteira = int(idade)
print(idade_inteira,type(idade_inteira))

# Tipos de conversores
"""
    int() -> converter para Inteiro
    str() -> converter para String
    float() -> converter para Float
    bool() -> converter para Boolean
"""

altura = float(input("Qual a sua altura: "))
print(altura, type(altura)) #A não ser que eu defina o tipo antes do input, sempre saira str(String)