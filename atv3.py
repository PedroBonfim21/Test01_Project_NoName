'''
3°) Faça um algoritmo para calcular o estoque médio de uma peça. Sendo assim o estoque-médio = (Quantidade mínima + quantidade máxima / 2)
'''

qnt_min=int(input("Digite a quantidade da minima da peça: "))
qnt_max=int(input("Digite a quantidade da maxima da peça: "))

estoque_medio = (qnt_min+qnt_max)/2

print(f"o estoque medio eh igual a: {estoque_medio}")