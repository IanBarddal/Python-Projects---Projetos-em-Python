jogadores = int(input("Escreva o número de jogadores: "))

somaPontos = 0
somaFaltas = 0
estrela = 0

for x in range (jogadores):
    pontos = int(input("Escreva o número de pontos: "))
    pontos *= 5
    faltas = int(input("Escreva o número de faltas: "))    
    faltas *= 3

    pontuação = pontos - faltas

    print (pontuação)

    if pontuação > 40:
        estrela += 1

if estrela == jogadores:
    print (f"{estrela}+")
elif estrela < jogadores:
    print (estrela)