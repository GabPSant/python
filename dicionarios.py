# > Dicionarios
# Criando dicionarios
dicionario = {}
dicionario = dict()

dicionario = { 'nome': 'Gabriel', 'idade': 20, 'altura': 1.82}

print(dicionario)
print(dicionario['idade'])# Diga a chave e retorna o valor

# Adicionar elemento em dicionario
dicionario['programador'] = True
print(dicionario)

#Sobrescrever conteudo
dicionario['altura'] = 2
print(dicionario)

# Iterando um dicionário
for chave in dicionario:
    print(chave) #Retorna a chave do dicionario

for chave in dicionario:
    print(chave, dicionario[chave]) # Retorna a chave do dicionario e seu valor

# Testando a existência de uma chave
print('peso' in dicionario)
print('altura' in dicionario)