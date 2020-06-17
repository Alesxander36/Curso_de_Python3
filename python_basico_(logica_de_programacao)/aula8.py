# Desafio

"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando f-strins (com chaves)
"""

nome = 'Alesxander'
idade = 40
altura = 1.88
peso = 100
ano = 2020 - idade
imc = peso / (altura ** 2)

print('{} tem {} anos, {} de altura e pesa {}kg.'.format(nome, idade, altura, peso))
print('O IMC de {} e {:.2f}'.format(nome, imc))
print('{} nasceu em {}'.format(nome, ano))
