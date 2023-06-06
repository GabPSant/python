# >Listas

# Antes:
nota1 = 8.9
nota2 = 7.4
nota3 = 9.6

# Com Listas
notas = [8.9,7.4,9.6]

# Criando Listas
lista = [] # Lista vazia
lista = list() # Lista vazia
lista = [7, "raiz quadrada", 5.0, True]
lista_de_listas = [10, [1,2,3]]

#Indexação
lista = [10, "Wilson", 3.1415, True]

for i in range(4): print(lista[i])
print()
# Em python, se eu colocar um numero negativo como 'i' ele retorna os valores de forma inversa
for i in range(1,5): print(lista[-i])

# Slices(fatiamento) - pegar parte da lista
lista = [10,50,60,84,75,46,25]
# Muito parecido com range
print(lista[0:3])
print(lista[3:6])

print(lista[2:6:2])
print()
# Como percorrer todos os elementos de uma lista
# Interação com for:

# 1. Utilizando os próprios elementos da lista

for elementos in lista:
    print(elementos)

# 2. Utilizando os indices
print(f"Comprimento da lista: {len(lista)}") #len = length

for i in range(len(lista)):
    print(f"{i}: {lista[i]}")
    print()

# > Métodos de Listas

lista = [1,3,12,8,2]

# append -> Adiciona elementos no final da lista

print(f"Antes do append: {lista}")
lista.append(3)
print(f"Depois do append: {lista}")

# insert -> adiciona elementos em posições selecionadas
lista.insert(2,10) # Empurra o resto na frente
print(f"Depois do insert: {lista}")

# extend -> juntar duas listas
lista2 = [1,2,3]
lista.extend(lista2)
print(f"Depois do extend: {lista}")

# pop -> remove o ultimo elemento ou elemento no indíce escolhido

lista.pop
print(f"Lista após o pop (sem definir o indíce): {lista}")
lista.pop(0)
print(f"Lista após o pop (com o indíce definido): {lista}")

# remove -> elimina um elemento existente na lista
lista.remove(3) #Só remove um elemento
print(f"Lista apos o remove: {lista}")

#count -> conta quantas vezes tal elemento aparece na lista
print(f"Quantas vezes o elemento 3 aparece na lista?\nR: {lista.count(3)}")

# index -> diz o indíce (posição) de tal elemento na lista.
print(f"Qual o indice do elemento 12?\nR: {lista.index(12)}")

# sort -> ordena a lista
lista.sort() #ordena de forma crescente
print(f"Lista depois do sort (crescente): {lista}")
lista.sort(reverse=True) #ordena de forma decrescente
print(f"Lista depois do sort (decrescente): {lista}")
print()
# > Funções para Listas
# len -> tamanho da lista/ quantos elementos tem na lista
print(f"Tamanho da lista: {len(lista)}")

# sum -> soma todos os elementos da lista
print(f"Soma de todos os elementos da lista: {sum(lista)}")

# max -> retorna o maior valor da lista
print(f"Maior elemento da lista: {max(lista)}")

# min -> retorna o menor valor da lista
print(f"Menor elemento da lista: {min(lista)}")