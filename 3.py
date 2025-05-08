# Simulador de Eleições. Escrever um algoritmo que calcule o resultado final das
# eleições para a presidência de um clube “Os nerds”, sabendo-se que:
# a) existem três chapas concorrendo;
# b) os eleitores votaram fornecendo o número da chapa escolhida;
# c) votaram ao todo 8 membros do clube. 
# O programa deverá processar os votos recebidos e fornecer o total de votos de cada uma das
# chapas, o total de votos em branco e o total de votos nulos. Além disso, o programa deverá verificar
# se a chapa mais votada é vencedora no primeiro turno da eleição (mais de 50% dos votos) ou se
# deverá ocorrer um segundo turno. 



print("--------------VOTAÇÃO NERDS----------------------")
print("CHAPA A ")
print("CHAPA B ")
print("CHAPA C ")
print("BRANCO (1) ")
print("NULO (0)")

chapaA= 0
chapaB= 0
chapaC= 0
cont =0 
branco=0
nulo = 0
for cont in range(8):
    voto = input("Para qual chapa deseja votar? A, B ou C?")
    voto.lower()
    if voto == 'a' or voto =='b' or voto == 'c':
        if voto == 'a':
            chapaA +=1
        elif voto =='b':
            chapaB +=1
        elif voto =='c':
            chapaC += 1
    elif voto == 1:
        branco +=1
    elif voto != 'a' or voto !='b' or voto != 'c': 
        print("Chapa não identificada. Contabilizado como nulo.")
        nulo +=1
    elif voto == 0:
        nulo +=1
    cont+1


    

print("----------------RESULTADO DAS ELEIÇÕES-------------------------")

if chapaA > 4 :
    print(f"A chapa A ganhou com {chapaA} votos")
    print(f"A chapa B teve {chapaB} votos")
    print(f"A chapa C teve {chapaC} votos")
    print(f"Votos nulos: {nulo}")
    print(f"Voto branco {branco}")
elif chapaA == chapaB:
    print(f"A chapa A empatou com chapa B, tendo {chapaA} votos")
    print(f"A chapa C teve {chapaC} votos")
    print(f"Votos nulos: {nulo}")
    print(f"Voto branco {branco}")
    print("-------------Segundo Turno---------------------")
    voto = input("Para qual chapa deseja votar? A ou B?")

    for cont in range(8):
        voto.lower()
        if voto == 'a' or voto =='b' or voto == 'c' or voto == 'A' or voto == 'B' or voto == 'C' :
            if voto == 'a'or voto == 'A' :
                chapaA +=1
            elif voto =='b'or voto == 'B':
                chapaB +=1
            elif voto =='c' or voto == 'C' :
                print("inválido. informe outro.")
                voto = input("Para qual chapa deseja votar? A ou B?")
        elif voto == 1:
            branco +=1
        elif voto != 'a' or voto !='b' or voto != 'c' or voto == 'A' or voto == 'B' or voto == 'C' : 
            print("Chapa não identificada. Contabilizado como nulo.")
            nulo +=1
        elif voto == 0:
            nulo +=1
        voto = input("Para qual chapa deseja votar? A ou B?")

    if chapaA > 4:
        print(f"A chapa A ganhou com {chapaA} votos")
        print(f"A chapa B teve {chapaB} votos")
        print(f"Votos nulos: {nulo}")
        print(f"Voto branco {branco}")
    elif chapaB > 4:
        print(f"A chapa B ganhou com {chapaB} votos")
        print(f"A chapa A teve {chapaA} votos")
        print(f"Votos nulos: {nulo}")
        print(f"Voto branco {branco}")

    
elif chapaA == chapaC:
    print(f"A chapa A empatou com chapa C, tendo {chapaA} votos")
    print(f"A chapa B teve {chapaB} votos")
    print(f"Votos nulos: {nulo}")
    print(f"Voto branco {branco}")
    print("-------------Segundo Turno---------------------")
    voto = input("Para qual chapa deseja votar? A ou C?")

    for cont in range(8):
        voto.lower()
        if voto == 'a' or voto =='b' or voto == 'c' or voto == 'A' or voto == 'B' or voto == 'C' :
            if voto == 'a'or voto == 'A':
                chapaA +=1
            elif voto =='b'or voto == 'B' :
                print("inválido. informe outro.")
                voto = input("Para qual chapa deseja votar? A ou C?")
            elif voto =='c'or voto == 'C':
                chapaC += 1
        elif voto == 1:
            branco +=1
        elif voto != 'a' or voto !='b' or voto != 'c' or  voto == 'A' or voto == 'B' or voto == 'C' : 
            print("Chapa não identificada. Contabilizado como nulo.")
            nulo +=1
        elif voto == 0:
            nulo +=1
        voto = input("Para qual chapa deseja votar? A ou C?")
    if chapaC > 4:
        print(f"A chapa C ganhou com {chapaC} votos")
        print(f"A chapa A teve {chapaA} votos")
        print(f"Votos nulos: {nulo}")
        print(f"Voto branco {branco}")
    elif chapaA > 4:
        print(f"A chapa A ganhou com {chapaA} votos")
        print(f"A chapa C teve {chapaC} votos")
        print(f"Votos nulos: {nulo}")
        print(f"Voto branco {branco}")
elif chapaB == chapaC:
    print(f"A chapa B empatou com chapa C, tendo {chapaB} votos")
    print(f"Votos nulos: {nulo}")
    print(f"Voto branco {branco}")
    print("-------------Segundo Turno---------------------")
    voto = input("Para qual chapa deseja votar? B ou C?")
    for cont in range(8):
        voto.lower(voto)
        if voto =='b' or voto == 'c' or voto == 'B' or voto == 'C' :
            if voto =='b' or voto == 'B':
                chapaB +=1
            elif voto == 'a':
                print("inválido. informe outro.")
                voto = input("Para qual chapa deseja votar? B ou C?")
            elif voto =='c'or voto == 'C':
                chapaC += 1
        elif voto == 1:
            branco +=1
        elif voto !='b' or voto != 'c' or voto != 'C' or voto != 'B': 
            print("Chapa não identificada. Contabilizado como nulo.")
            nulo +=1
        elif voto == 0:
            nulo +=1
        voto = input("Para qual chapa deseja votar? B ou C?")
    if chapaC > 4:
        print(f"A chapa C ganhou com {chapaC} votos")
        print(f"A chapa B teve {chapaB} votos")
        print(f"Votos nulos: {nulo}")
        print(f"Voto branco {branco}")
    elif chapaB > 4:
        print(f"A chapa B ganhou com {chapaB} votos")
        print(f"A chapa C teve {chapaC} votos")
        print(f"Votos nulos: {nulo}")
        print(f"Voto branco {branco}")
    
elif chapaB > 4:
    print(f"A chapa B ganhou com {chapaB} votos")
    print(f"A chapa A teve {chapaA} votos")
    print(f"A chapa C teve {chapaC} votos")
    print(f"Votos nulos: {nulo}")
    print(f"Voto branco {branco}")
elif chapaC  > 4:
    print(f"A chapa C ganhou com {chapaC} votos")
    print(f"A chapa A teve {chapaA} votos")
    print(f"A chapa B teve {chapaB} votos")
    print(f"Votos nulos: {nulo}")
    print(f"Voto branco {branco}")
