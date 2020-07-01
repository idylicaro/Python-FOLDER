horasTotais = int(input('Quantas horas trabalhadas por mes?'))
valorHora = float(input('Qual o valor da hora trabalhada?'))

salarioBruto = valorHora * horasTotais
if salarioBruto <= 900:
    irPercent = 0
elif salarioBruto > 900 and salarioBruto <= 1500:
    irPercent = 5
elif salarioBruto > 1500 and salarioBruto <= 2500:
    irPercent = 10
elif salarioBruto > 2500:
    irPercent = 20

descontoIr = (salarioBruto / 100) * irPercent
descontoINSS = (salarioBruto / 100) * 10
descontoFGTS = (salarioBruto / 100) * 11
totalDescontos = descontoIr+descontoINSS

print('Salário Bruto: ({} * {})......: R$%.2f'.format(valorHora,horasTotais)%(salarioBruto))
print('(-) IR ({}%%)..................: R$%.2f'.format(irPercent)%(descontoIr))
print('(-) INSS (10%%)................: R$%.2f' %(descontoINSS))
print('FGTS (11%%)....................: R$%.2f' %(descontoFGTS))
print('Total de descontos............: R$%.2f' %(totalDescontos))
print('Salario Liquido...............: R$%.2f' %(salarioBruto - totalDescontos))