custoSorveteBase = 250

tamanhoDesejado = int(input("Digite o tamanho da torre de sorvete desejado: "))
alturaBase = int(input("Digite a altura base do sorvete: "))
razãoAumento = int(input("Digite a razão do aumento da torre de sorvete: "))

custoSorvete = 0

for x in range (alturaBase, tamanhoDesejado, razãoAumento):
    custoSorveteBase += 100

    if x > tamanhoDesejado:
        break

print (custoSorveteBase)