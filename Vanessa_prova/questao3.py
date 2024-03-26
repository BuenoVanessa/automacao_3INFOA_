'''
Crie um programa que calcule o valor total das compras de um cliente. O
programa deve solicitar indefinidamente que o usuário digite o preço de
cada produto adquirido. Quando o usuário digitar a tecla 'igual' no lugar
do preço do produto, o programa deve exibir a soma dos preços de todos
os produtos digitados.
'''

def calcular_total_compras():
    total = 0.0
    
    while True:
        preco_produto = input("Digite o preço do produto (ou '=' para finalizar): ")
        
        if preco_produto.lower() == '=':
            break
        
        try:
            preco_produto = float(preco_produto)
            total += preco_produto

        except ValueError:
            print("Por favor, insira um preço válido.")

    return total

total_compras = calcular_total_compras() 
print("O total das compras é: ", total_compras)

