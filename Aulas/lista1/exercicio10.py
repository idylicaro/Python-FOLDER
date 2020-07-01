primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))
terceiraNota = float(input("Digite a terceira nota: "))

media = (primeiraNota + segundaNota + terceiraNota) / 3

if media >= 7 and media < 10:
    print('APROVADO, Media:%d'%(media))
elif media < 7:
    print('REPROVADO, Media:%d'%(media))
elif media == 10 :
    print('Aprovado com Distinção')