# Operadores lógicos
"""
and, or, not
in e not in


# (verdadeiro E False) = Falso
comparacao1 and comparacao2

# Verdadeiro OU Verdadeiro
comp1 or comp2

a = 2
b = 3

if not b > a:
    print('B e maior do que A')
else:
    print('A e maior do que B')
"""

usuario = input('Nome de usuario: ')
senha = input('Senha do usuario: ')

usuario_bd = 'Alesxander'
senha_bd = '12345'

if usuario_bd == usuario and senha_bd == senha:
    print('Voce estar logado no sistema')
else:
    print('usuario e senha invalidos!')
