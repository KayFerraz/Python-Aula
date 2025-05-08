#Faça um programa que tenha como entrada 2 números, em seguida mostre um texto/menu para escolher a 
# operação desejada: + - * /
#
#       Adição +
#       Subtração -
#       Multiplicação *
#       Divisão /
#       Raiz quadrada 
#       Potência

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

soma = num1 + num2
div = num1 / num2
mult = num1 * num2
sub = num1 - num2
pot = num1 ** num2
raiz = num1 ** 0.5


print("OPERAÇÃO DESEJADA")
print("1 - ADIÇÃO")
print("2 - SUBTRAÇÃO")
print("3 - DIVISÃO")
print("4 - MULTIPLICAÇÃO")
print("5 - POTÊNCIA")
print("6 - RAIZ QUADRADA")

var = int(input("Digite a operação desejada"))


if var == 1:
    print("SOMA")
    print(f"O resultado da soma de {num1} + {num2} é: {soma}")
elif var == 2:
    print("SUBTRAÇÃO")
    print(f"O resultado da subtração de {num1} - {num2} é: {sub}")
elif var == 3:
    print("DIVISÃO")
    if num2 > 0:
        print(f"O resultado da divisão de {num1} / {num2} é: {div}")
    else: 
        print("Não é possível dividir número por zero")
elif var == 4:
    print("MULTIPLICAÇÃO") 
    print(f"O resultado da multplicação de {num1} * {num2} é: {mult}")
elif var == 5:
    print("POTÊNCIA")
    print(f"O resultado da potência de {num1} ** {num2} é: {pot}")
elif var == 6:
    print("RAIZ QUADRADA")
    print(f"O resultado da raiz quadrada de {num1} é: {raiz}")
else: 
    print("OPÇÃO INVÁLIDA!")
