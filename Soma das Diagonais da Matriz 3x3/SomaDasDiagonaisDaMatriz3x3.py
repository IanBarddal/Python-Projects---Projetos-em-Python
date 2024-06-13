matriz = []

for x in range (3):
    linhas = []
    for y in range (3):
        valores = int (input ("Digite os valores da matriz: "))
        linhas.append(valores)
    matriz.append(linhas)

diagonalPrincipal = matriz[0][0] + matriz[1][1] + matriz[2][2]
diagonalSecundária = matriz[0][2] + matriz[1][1] + matriz[2][0]

print (f"A diagonal principal vale {diagonalPrincipal}")
print (f"A diagonal secundária vale {diagonalSecundária}")