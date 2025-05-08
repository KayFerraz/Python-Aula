print("-------VERIFICAR SE O ANO É BISSEXTO--------")
print("Caso 1: é divisível por 4, mas não por 100.")
print("Caso 2: é divisível por 4,por 100 e por 400.")
print("--------------------------------------------")
ano = int(input("Informe o ano para verificar se é bissexto:  "))

calc1 = ano % 4 
calc2 = ano % 4
calc3 = ano % 100
calc4 = ano % 400

if ano > 0:
    if calc1 == 0 :
        print(f"O ano {ano} é bissexto, pois se encaixa no caso 1.")
    elif calc2 == 0 or calc3 == 0 or calc4 == 0:
        print(f"O ano {ano} é bissexto, pois se encaixa no caso 2.")
    else: 
        print(f"O ano {ano} não é bissexto")
    