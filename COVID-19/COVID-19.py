casosNovos = int(input("Digite a quantidade de casos por milhão de habitantes: "))
hospitalizações = int(input("Digite a quantidade de hospitalizações por milhão de habitantes: "))

if casosNovos <= 50 and hospitalizações <= 10:
    print("A cidade é considerada zona BRANCA!")

if hospitalizações > 10 and hospitalizações <= 30:
    print ("A cidade é considerada zona AMARELA!")

if hospitalizações > 30:
    print ("A cidade é considerada zona VERMELHA!")