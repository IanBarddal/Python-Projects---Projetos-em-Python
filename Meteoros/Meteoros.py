testes = 1

while True:
    contaMeteoro = 0

    coordXSup = int(input("Digite a coordenada X do canto superior da propriedade: "))
    coordYSup = int(input("Digite a coordenada Y do canto superior da propriedade: "))
    coordXInf = int(input("Digite a coordenada X do canto inferior da propriedade: "))
    coordYInf = int(input("Digite a coordenada Y do canto inferior da propriedade: "))

    if coordXSup == coordYSup == coordXInf == coordYInf == 0:
        break

    qtdeMeteoros = int(input("Digite a quantidade de meteoros: "))

    x = 0
    while x < qtdeMeteoros:
        coordMeteoroX = int(input("Digite a coordenada X do meteoro: "))
        coordMeteoroY = int(input("Digite a coordenada Y do meteoro: "))

        if (coordMeteoroX >= coordXSup and coordMeteoroX <= coordXInf) and (coordMeteoroY >= coordYInf and coordMeteoroY <= coordYSup):
            contaMeteoro += 1
        
        x += 1
    
    print (f"Teste {testes}:")
    print (contaMeteoro, end="\n")

    testes += 1