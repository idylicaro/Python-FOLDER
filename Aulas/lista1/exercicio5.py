a = float(input('Digite o valor do lado A: '))
b = float(input('Digite o valor do lado B: '))
c = float(input('Digite o valor do lado C: '))

if a + b > c or a + c > b or c + b > a:
    if a == b and b == c:
        print('É um Triângulo Equilátero')
    elif a == b or a == c or b == c :
       print('É um Triângulo Isósceles')
    elif a != b and a != c and b != c :
       print('É um Triângulo Isósceles')
        
else:
    print('Não é um triângulo')