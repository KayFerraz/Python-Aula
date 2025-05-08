# 4. Desenvolva um algoritmo que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto 
# de Renda, 8% para o INSS e 2% para o Sindicato, faça um programa que imprima:
# a) salário bruto.
# b) quanto pagou ao INSS. • c)
# quanto pagou à Receita Federal.
# d) quanto pagou ao Sindicato.
# e) o valor do salário líquido.
# Resumo do cálculo dos descontos:
# Descontos:
# - IR (11%)
# - INSS (8%)
# - Sindicato ( 2%)
# Obs.: salário líquido = salário bruto - descontos.


salarioTrab = float(input("Quanto você ganha por hora trabalhada? "))
horaTrab = float(input("Quantas horas você trabalha no mês?  "))
print("--------------------------------------------")

salBruto = salarioTrab * horaTrab
IR = salBruto * 0.11
INSS = salBruto * 0.08
sindicato = salBruto * 0.02

desconto = IR + INSS + sindicato
salLiquido = salBruto - desconto

print(f"Salario bruto: R${salBruto}")
print(f"Desconto do IR: R${IR}")
print(f"Desconto do INSS: R${INSS}")
print(f"Desconto do sindicato: R${sindicato}")
print(f"Salário líquido: R${salLiquido}")