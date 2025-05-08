
print("/----------- SEJA BEM VINDO À CALCULADORA DE IMC------------/")
peso = int(input("Digite o peso para calcular o IMC: "))
altura = float(input("Digite a altura para calcular o IMC: "))
print("/-----------/")


alt = altura * altura
imc = peso / alt



if peso>0 :
    if imc < 16 :
        print('MAGREZA GRAVE')
    elif imc >= 16  and imc <=16.9:
        print('MAGREZA MODERADA')
    elif imc >=17 and imc <=18.5:
        print('MAGREZA LEVE')
    elif imc >=18.6 and imc <=24.9:
        print('PESO IDEAL')
    elif imc >=25 and imc <=29.9:
        print('SOBREPESO')
    elif imc >=30 and imc <=34.9:
        print('OBESIDADE GRAU I')
    elif imc >=35 and imc <=39.9:
        print('OBESIDADE GRAU II')
    elif imc >=40:
        print('OBESIDADE GRAU III') 
else: 
    print("Não foi possível classificar")
    

