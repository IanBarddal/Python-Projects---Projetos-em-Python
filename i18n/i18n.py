palavra = input("Digite uma palavra: ")

contagem2 = 0

for letra1 in palavra[0:1]:
    contagem1 = letra1

for letra in palavra [1:-1]:
    contagem2 += 1

for letra2 in palavra [-1:len(palavra)]:
    contagem3 = letra2

print (letra1 + str(contagem2) + letra2)