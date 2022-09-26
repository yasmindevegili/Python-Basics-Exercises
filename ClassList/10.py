nome = str(input())
salario = float(input())
vendas = float(input())
salario_final = (0.15*vendas)+salario
print('TOTAL = R$ {:.2f}'.format(salario_final))
