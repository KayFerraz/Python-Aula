print("--------------------DETETIVE-----------------------")
print("Respostas serão no formato: ")
print("SIM ")
print("NÃO ")

p1 = input("Telefonou para a vítima? ")
p2 = input("Esteve no local do crime? ")
p3 = input("Mora perto da vítima? ")
p4 = input("Devia para a vítima? ")
p5 = input("Já trabalhou com a vítima? ")

somap = 0

if p1 == 'SIM' or p1 == 'sim':
    somap += 1
if p2 == 'SIM' or p2 == 'sim':
    somap += 1
if p3 == 'SIM' or p3 == 'sim':
    somap += 1
if p4 == 'SIM' or p4 == 'sim':
    somap += 1
if p5 == 'SIM' or p5 == 'sim':
    somap += 1

if somap == 0 or somap == 1: 
    print("INOCENTE")
elif somap == 2:
    print("SUSPEITO")
elif somap == 3 or somap == 4: 
    print("CÚMPLICE")
elif somap == 5: 
    print("ASSASSINO")
   
