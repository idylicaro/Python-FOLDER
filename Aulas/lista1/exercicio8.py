data = input('Digite uma data no formato (dd / mm / aaaa): ')

dataVector  = data.split('/')
if(len(dataVector) != 3):
    print('Formato errado')
else:
    dia = int(dataVector[0])
    mes = int(dataVector[1])
    ano = int(dataVector[2])

    result = True

    if dia < 1 and dia > 31:
        result = False

    if mes <1 and mes > 12:
        result = False

    if ano < 0:
        result = False 

    if result:
        print('Formato Aceito')
    else:
        print('Formato Errado')