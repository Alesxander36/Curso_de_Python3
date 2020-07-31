# Exercício 1
"""
Faça um programa que peça para o usuário para digitar um número inteiro
informe  se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num_inteiro = input('Digite um numero inteiro: ')

if num_inteiro.isdigit():
    num_inteiro = int(num_inteiro)

    if num_inteiro % 2 == 0:
        print(f'{num_inteiro} e par')
    else:
        print(f'{num_inteiro} e impar')
else:
    print('Isso nao e um numero inteiro.')


# Exercício 2
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

horario = input('Digite um horario de (0-23): ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print("Horario deve estar entre 0 e 23")
    else:
        if horario <= 11:
            print("Bom dia!")
        elif horario <= 17:
            print("Boa Tarde!")
        else:
            print("Boa noite!")
else:
    print("Por favor digite um horario entre 0 e 23 hs")


# Exercício 3
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu primero nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é curto')
elif tamanho <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
