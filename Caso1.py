numero = float(input('Digite um número: '))
if numero > 0:
    print('O numero', numero, 'é positivo')
elif numero < 0:
    print('O número', numero, 'é negativo')
else:
    print('O número', numero, 'é zero')

###

numero = float(input('Digite um número: '))
if numero > 0:
    print('O numero %.2f é positivo' % numero)
elif numero < 0:
    print('O número', numero, 'é negativo')
else:
    print('O número', numero, 'é zero')