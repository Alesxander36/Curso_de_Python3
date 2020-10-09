"""
Listas em Python

Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = l1 + l2

# l1.extend('a')
# l2.append('b')
# l2.insert(#for valor in l4:
#  print(valor)

# print(l1)
# print(l2)
# print(l3)
# print(l4)

# Joguinho de forca

secreto = 'perfume'
digitadas = []
chances = 3

while True:

    if chances <= 0:
        print('VOCÊ PERDEU!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUUUlll, a letra "{letra}" existe na palavra secreto.')
    else:
        print(f'AFFFzzz, a letra "{letra}" NÃO EXISTE na palavra secreto.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta esta assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem: {chances} chances.')
    print()
