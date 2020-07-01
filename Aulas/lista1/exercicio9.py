numero = int(input('Digite um numero menor que 1000: '))

print('{} Centenas, {} Dezenas, {} Unidade'.format((numero)//100, (numero%100) // 10, ((numero%100)%10)))
