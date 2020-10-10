"""
For / Else em Python

"""
variavel = ['Luiz Otávio', 'AJoãozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('j'):
        break
else:
    print('Nao existe uma palavra que começa com J')
