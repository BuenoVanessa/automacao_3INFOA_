'''
Cássia precisa de ajuda para calcular a quantidade de gotas de
medicamento para sua filha. Construa um programa que solicite a
concentração de princípio ativo do medicamento em mg/ml, o peso da
criança e a dose recomendada em mg por kg. O programa deve calcular a
dose total multiplicando o peso da criança pela dose por kg recomendada
e dividindo pelo conteúdo do medicamento em mg por ml. Para obter a
quantidade de gotas, multiplica-se o resultado por 20, já que 1 ml equivale
a aproximadamente 20 gotas.
'''

def calcular_quantidade_de_gotas(concentracao, peso_da_crianca, dose_por_kg):
  
    dose_total = peso_da_crianca * dose_por_kg
    
   
    ml_necessarios = dose_total / concentracao
    
    #(1 ml = 20 gotas)
    quantidade_de_gotas = ml_necessarios * 20
    
    return quantidade_de_gotas

concentracao = float(input("Digite a concentração do medicamento (mg/ml): "))
peso_da_crianca = float(input("Digite o peso da criança (kg): "))
dose_por_kg = float(input("Digite a dose recomendada por kg (mg/kg): "))


quantidade_de_gotas = calcular_quantidade_de_gotas(concentracao, peso_da_crianca, dose_por_kg)
print("A quantidade de gotas é igual a: ", quantidade_de_gotas)
