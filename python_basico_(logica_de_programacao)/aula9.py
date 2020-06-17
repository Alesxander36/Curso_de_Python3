# Input: Entrada de dados do usuário

# Exemplos:

nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")
ano_nasc = 2020 - int(idade)  # fazendo um catch do str para int

print(f'{nome} tem {idade} anos.')
print(f'{nome} nasceu em {ano_nasc}')

# Exemplo de calculadora
num_1 = int(input('Digite um numero: '))
num_2 = int(input('Digite outro numero: '))

print(num_1 + num_2)
