'''
Crie um programa que recebe como entrada um número inteiro. Caso o
número digitado seja negativo, o programa deve imprimir ‘Retroceder’; se
o número for 0, imprimir ‘Pare’; e se for um número positivo, imprimir
‘Avançar’.
'''

def verificar_numero(numero):
    if numero < 0:
        print("Retroceder")
    elif numero == 0:
        print("Pare")
    else:
        print("Avançar")

numero = int(input("Digite um número inteiro: "))

verificar_numero(numero)
