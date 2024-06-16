número = int(input("Digite um número: "))

vezes = int(input("Digite a quantidade de vezes que ele será deslocado: "))

soma = número

for x in range (vezes):
    número *= 10
    
    soma += número

somaFinal = soma

print (somaFinal)