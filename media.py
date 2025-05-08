#Faça um programa que leia 2 notas, calcule a média e verifique se o aluno está Aprovado ou Reprovado.

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1 + nota2)/ 2
exame = 10 - media

print(f"A média é de: {media}")

if media < 6:
    print("O aluno está reprovado.")
else:
    print("O aluno está aprovado.")
    print(f"No exame precisa de: {exame}" )

