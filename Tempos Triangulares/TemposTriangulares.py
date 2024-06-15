ângulo1 = int (input ("Digite o primeiro ângulo: "))
ângulo2 = int (input ("Digite o segundo ângulo: "))
ângulo3 = int (input ("Digite o terceiro ângulo: "))

somaÂngulos = ângulo1 + ângulo2 + ângulo3

if ângulo1 == 60 and ângulo2 == 60 and ângulo3 == 60:
    print ("Equilateral")
if somaÂngulos == 180 and ângulo1 == ângulo2 and ângulo2 != ângulo3:
    print ("Isosceles")
if somaÂngulos == 180 and ângulo1 != ângulo2 and ângulo2 != ângulo3:
    print ("Scalene")
if somaÂngulos != 180:
    print ("Error")