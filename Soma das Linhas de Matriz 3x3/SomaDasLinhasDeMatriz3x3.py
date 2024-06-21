matriz = []

for x in range (3):
    linhas = []
    for y in range (3):
        elementos = int(input("Digite os elementos da matriz: "))
        linhas.append(elementos)
    matriz.append(linhas)

for linhas in range (3):
    somaLinhas = [sum(linhas) for linhas in matriz]

    print (f"A soma da linha {linhas} é {somaLinhas}")