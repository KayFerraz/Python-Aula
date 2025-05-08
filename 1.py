# Neste jogo mostre que você domina par ou ímpar e vença seu adversário. Implemente um algoritmo
# que solicite ao usuário 10 números inteiros e, ao final, informe a quantidade de números ímpares e
# pares lidos. Calcule também a soma dos números pares e a média dos números ímpares. 


num = int(input("Digite o número: "))
impar = 0
par = 0
somaPar = 0
mediaImp = 0 
calcM = mediaImp

for cont in range(10):
    num = int(input("Digite o número: "))
    if num %2 ==0 :
        par +=1 
        somaPar += num
    else :
        impar +=1
        mediaImp += num 

calcM = mediaImp / impar


print(f"Há {impar} números ímpares") 
print(f"Há {par} números pares")  
print(f"Números pares somados:  {somaPar} ")   
print(f"Média dos números ímpares:  {calcM} ")  
