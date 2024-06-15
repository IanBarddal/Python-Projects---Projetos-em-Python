número = int(input("Digite um número: "))

contador = 0

while número != 1:
    if número % 2 == 0:
        número = número // 2
        contador += 1
        print (número)
    
    else:
        número = (número * 3) + 1
        contador += 1
        print (número)

print (número + contador)