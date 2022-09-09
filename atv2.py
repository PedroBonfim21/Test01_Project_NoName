'''
2°) Crie um algoritmo que será responsável por calcular o índice de gordura corporal. 
Na situação do sexo masculino deverá conter os seguintes fluxos: 
menor do que 11% = Atleta,
entre 11% e 13% = bom,
entre 14% e 20% = normal,
entre 21% a 23% = elevado,
acima de 23% = alto

Na situação do sexo feminino:
menor do que 16%= Atleta,
entre 16% e 19% = bom,
entre 20% e 28% = normal,
entre 29% a 31% = elevado,
acima de 31% = alto
'''

indice=int(input("Digite o seu indice de gordura corporal: "))
sexo=str.upper(input("Digite seu sexo 'M' para masculino e 'F' para feminino: "))

if sexo == 'M':
    print("Sexo: MASCULINO")
    
    if indice < 11:
        print("indice de gordura de um ATLETA")

    elif  11<= indice <=14:
        print("indice de gordura BOM")

    elif 14<= indice <=21:
        print("indice de gordura NORMAL")
    
    elif 21<= indice <=23:
        print("indice de gordura ELEVADO")
        
    elif indice > 23:
        print("indice de gordura ALTO")

elif sexo == 'F':
    print("Sexo: FEMININO")
    if indice < 16:
        print("indice de gordura de um ATLETA")

    elif  16<= indice <=19:
        print("indice de gordura BOM")

    elif 20<= indice <=28:
        print("indice de gordura NORMAL")
    
    elif 29<= indice <=31:
        print("indice de gordura ELEVADO")

    elif indice > 31:
        print("indice de gordura ALTO")

