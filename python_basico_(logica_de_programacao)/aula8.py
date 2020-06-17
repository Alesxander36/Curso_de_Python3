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
peso = 100.5
ano_atual = 2020
nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura} de altura')
print(f'{nome} pesa {peso} e seu imc e {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')
