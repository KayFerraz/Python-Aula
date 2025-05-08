prod = int (input("Digite o valor do produto:"))
desc = int(input("Digite o valor de desconto: "))

calc = prod - desc

print(f"O Valor do produto é: R${prod}")
print(f"O Valor do desconto é: R${desc}")
print(f"Desconto de R${desc} na mercadoria de valor R${prod}")
print(f"O valor a pagar é R${calc}")