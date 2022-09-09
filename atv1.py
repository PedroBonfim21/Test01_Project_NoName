'''
 Faça um algoritmo que contenha 3 vetores, o primeiro deve ser um vetor com 30 posições, onde irá conter números inteiros aleatórios. 
Após isso, separe esse vector em mais dois novos vetores onde no primeiro vector deve conter apenas os números pares e outro para números ímpares. Lembrando, você não deve alocar os valores manualmente, utilize um laço for ou while.
'''
import random

random_num = [random.randint(0, 100) for x in range(30)]
num_par=[]
num_impar=[]

for num in random_num:
    if (num%2)==0:
        num_par.append(num)

    else:
        num_impar.append(num)

print(f"vetor de numeros impar: {num_impar}")
print("\n")
print(f"vetor de numeros par: {num_par}")
