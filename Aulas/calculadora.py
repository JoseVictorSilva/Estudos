valor1 = 10
valor2 = 4
operacao = '+'
print('+*+*+* CALCULADORA +*+*+*')
print('QUAL É A OPERAÇÃO DESEJADA? (+/-/*/÷)')

if operacao == '+':
    resultado = valor1+valor2
    print(f'Resultado: {resultado}')
if operacao == '-':
    resultado = valor1-valor2
    print(f'Resultado: {resultado}')
if operacao == 'polinomio':
    resultado = valor1**2 + (2*(valor1*valor2)) + valor2**2
    print(f'Resultado: {resultado}')


# SE O NÚMERO FOR DIVISIVEL POR 3 IMPRIMA FIZZ
# SE FOR DIVISIVEL POR 5 IMPRIMA BUZZ if variavel % 5 == 0
# SE FOR DIVISIVEL POR 5 E POR 3 IMPRIMA FIZZBUZZ
# SE NÃO IMPRIMA NaN