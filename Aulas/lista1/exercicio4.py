primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))
media = (primeiraNota + segundaNota) / 2

if media > 9:
    conceito = 'A'
elif media > 7.5 and media < 9:
    conceito = 'B'  
elif media > 6 and media < 7.5:
    conceito = 'C'  
elif media > 4 and media < 6:
    conceito = 'D'
else:
    conceito = 'E'

print('Nota 1: %.1f, Nota 2: %.1f, Média: %.1f e Conceito: %s'%(primeiraNota,segundaNota,media,conceito))  