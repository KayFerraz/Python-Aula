#se categoria for A e a faixa de valor for entre 1 e 10
# entre 1 e 10: Classificação bronze
# entre 11 e 20: Classificação prata
# entre 21 e 30: Classificação ouro

#se categoria for B e a classificação Diamate
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


cat = 'A'
valor = 15

if cat == 'A':
    if valor >=1 and valor <=10:
        print('Categoria A: Classificação Bronze')
    elif valor >=11 and valor <=20:
        print('Categoria B: Classificação Prata')
    elif valor >=21 and valor <=30:
        print('Categoria C: Classificação Ouro')
    else: 
        print("Nçao foi possível classificar.")
elif cat == 'B':
    print ("Categoria B: Classificação Diamante")
else: 
    print("Não foi possível classificar")
    

