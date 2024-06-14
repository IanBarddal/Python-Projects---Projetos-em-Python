número = int(input("Digite um número de três dígitos: "))

dígitoCentena = número // 100

if número < 100 or número > 999:
    print ("Valor inválido")

elif dígitoCentena % 2 == 0:
    print (dígitoCentena)
    print ("O dígito é par!")

else:
    print (dígitoCentena)
    print ("O dígito é ímpar!")