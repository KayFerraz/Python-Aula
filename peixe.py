print("/-----------BEM VINDO AO CLUBE DE PESCA------------/")

peixe = float(input("Digite o peso do peixe: "))

calPeixe =  peixe - 50
multa = 4 * calPeixe

if peixe >0:
    if peixe <= 50:
        print("O Peso do peixe está dentro do limite")
    elif peixe >= 50:
        print("O peso do peixe excedeu o limite")
        print(f"Excedeu {calPeixe} do limite")
        print(f"Multa de {multa}" )
    else: 
        print("Valor inválido.")

        