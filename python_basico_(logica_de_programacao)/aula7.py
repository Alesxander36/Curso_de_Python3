# Introdução à formatação de Strings

nome = 'Alesxander Santos'
idade = 39
altura = 1.88
e_maior = idade > 18
data_1 = True
data_atual = 2020
peso = 95
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu umc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc e {:.2f}'.format(nome, idade, imc))
