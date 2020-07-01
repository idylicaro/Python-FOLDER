#josecarlos2001@gmail.com
salario = float(input("Digite o salario: "))

if salario <= 280:
    percent = 20
elif salario > 280 and salario < 700:
    percent = 15
elif salario > 1500:
    percent = 5

salarioFinal = salario + (salario/100) * percent

print('Salário antes do reajuste: {}'.format(salario))
print('Percentual de aumento aplicado: {}%'.format(percent))
print('Valor do aumento:',  salarioFinal)
print('Novo salário, após o aumento: {}'.format(salarioFinal))
