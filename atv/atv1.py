jogadores = ['Baiano', 'Pipi', 'Bernardo', 'Luquinhas', 'Caliel']
gols= [37, 12, 25, 2, 0]
indices= []

def calcTGol(gols):
    total_gols = 0
    for gol in gols:
        total_gols += gol
    return total_gols

def mediaGols(gols, jogadores):
    total_gols = 0
    for gol in gols:
        total_gols += gol
    return total_gols / len(jogadores)


media = mediaGols(gols, jogadores)
print(media)
total = calcTGol(gols)
print(total)

