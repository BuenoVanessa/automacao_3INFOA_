'''
Exercício 3 - Semana 3
Crie um programa que lê do teclado
sucessivos números de matricula (int).
O programa deve parar de ler os números 
quando a matricula 0 for digitada.
Ao final deve apresentar os números de 
matriculas separados em 3 grupos.
'''

matriculas = [] #cria uma lista vazia (sem nomes)
while True: #repete para sempre
    matricula = input("Digite sua matricula: ")
    matriculas.append(matricula) #adiciona o nome na lista
    if matricula == "0": #se o nome for igual a fim
        print(matriculas)
        break        #para o laço de repetição

   