matriz = []

for x in range (3):
    linhas = []
    for y in range (3):
        elementos = int(input("Digite os elementos da matriz: "))
        linhas.append(elementos)
    matriz.append(linhas)

for colunas in range (3):
    somaColunas = [sum(colunas) for colunas in zip(*matriz)]
    
print (f"Somas: {somaColunas}")