# > Criar funções
# Funções com parametros
def saudacao(nome):
    print(f"Seja bem vindo, {str(nome)}!\nUm prazer té-lo no curso")

saudacao("Gabriel")

# Funções com parametros default
def saudacao(nome, curso = "Python"):
    print(f"Saudações {nome}!\nBem vindo ao curso de {curso}")

saudacao("Gabriel")

#Funções com retornos
def soma(x, y):
    return x+y

print(soma(5,6))

def calculo(x,y, operacao = '+'):
    if(operacao == '+'): return x+y
    elif(operacao == '-'): return x-y
    elif(operacao == '/'): return x/y
    elif(operacao == '*'): return x*y

print(calculo(5,8,'*'))