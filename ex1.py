def calcMedia(notas):
    soma = 0
    for nota in notas:
        soma+=nota #soma = soma + nota
    return soma / len(notas)


notas = [2 , 9 , 7]
media = calcMedia(notas)

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("reprovado")
