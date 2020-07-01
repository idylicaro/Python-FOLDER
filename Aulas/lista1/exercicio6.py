import math

a = float(input("Digite o valor de A: "))
if a == 0:
    print('Não é uma Equação de segundo grau')
else:
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

delta = b**2 - 4 * a * c
if delta < 0:
    print('a equação não possui raízes reais')
elif delta == 0:
    print('A raiz unica é : {}'.format(-b/2*a))
else:
    print('A raiz 1 é : {}'.format( (-b+math.sqrt(delta)) / 2*a) )
    print('A raiz 2 é : {}'.format( (-b-math.sqrt(delta)) / 2*a) )