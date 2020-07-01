# Operadores Relacionais

"""
== Igualdade
> Maior que
>= Maior que ou igual a
< Menor que
<= Menor que ou igual a
!= Diferente
"""
nome = input('Qual e o seu nome? ')
idade = input('Qual e a sua idade? ')
idade_limite = 18

idade = int(idade)

# LIMITE PARA PEGAR EMPRESTIMO
idade_menor = 20  # Muito jovem
idade_maior = 30  # Passou da idade


if idade >= idade_menor and idade <= idade_maior:
    print(f'Emprestimo aprovado para {nome}')
else:
    print(f'{nome} não pode pegar o emprestimo')
