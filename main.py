import random 

print('Olá, qual é o seu nome?')

usuario = input()

print(f'Bem-vindo, {usuario}!')

    

letra_maiuscula =  chr(random.randint(65, 90))
letra_minuscula = chr(random.randint(97, 122))
char_especial = chr(33)
lista_numeros = []


for i in range(5): #ele imprimirá 5 números (de 1 a 8)
    numeros = random.randrange(9)
    lista_numeros.append(numeros)




random.shuffle(lista_numeros)

lista_numeros = str(lista_numeros) [1:-1]
lista_numeros = lista_numeros.replace(',', '')

print('Vou gerar sua senha!')

print(letra_maiuscula, letra_minuscula, lista_numeros, char_especial)

