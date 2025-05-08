# No jogo “Descubra o Maior > e o Menor <”. Escreva um algoritmo que receba um conjunto de
# valores inteiros e positivos, calcule e exiba o maior e o menor valor do conjunto.
# Considere que:
# a. para encerrar a entrada de dados, deve ser digitado o valor zero;
# b. para valores negativos, deve ser exibida uma mensagem;
# c. esses valores (zero e negativos) não entrarão nos cálculos. 
num = int(input("Digite o número:  (0 para parar)"))
menor = num
maior = 0 
while num !=0:
    if num < 0: 
        print("O número precisa ser maior que 0.")
    if num > maior:
        maior = num
    elif num < menor:
        menor = num  
    num = int(input("Digite o número: "))
    

print(f"O menor é: {menor}")
print(f"O maior é: {maior}")
