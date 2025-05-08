# O jogo sério da empresa Cara de Pau Ltda. resolveu fazer uma pesquisa de mercado, abrangendo o 
# maior número de pessoas possíveis, para saber se as pessoas estão gostando ou não de um novo 
# produto lançado no mercado. A informações coletadas eram: o sexo (M,F), a idade e uma resposta 
# (S=sim, N=não, I=indiferente) de cada entrevistado. Faça um algoritmo que calcule: 
# a) quantas pessoas foram entrevistadas; 
# b) quantas pessoas disseram sim e quantas disseram não; 
# c) o percentual de pessoas que disseram não; 
# d) quantas mulheres disseram sim e quantos homens disseram não. 
print("Foi lançado um novo computador, para auxiliar programadores. Gostaria de fazer uma breve pesquisa.")
print("AS RESPOSTAS SÃO:")
print("S = SIM")
print("N = NÃO")
print("I = INDIFERENTE")
print("PERGUNTAS SOBRE O SEXO SÃO:")
print("H = HOMEM")
print("M = MULHER")

resp = input("Deseja continuar?S/N  ")
cont = 0
contH = 0
contM = 0
contS = 0
contI = 0
contN = 0
mulherSim = 0
homemNao = 0

while resp == 's' or resp == 'S':
    resp = input("Qual o sexo? H/M  ")
    if resp == 'H' or resp == 'h':
        contH +=1
    elif resp == 'M' or resp == 'm':
        contM +=1
    like = input("Você está satisfeito(a) com o nosso produto? S/N  " )
    if like == 's' or like =='S':
        contS+=1
    elif like == 'n' or like =='N':
        contN +=1
    elif like == 'i' or like =='I':
        contI+=1
    if resp == 'M' or resp == 'm' and like == 's' or like =='S':
        mulherSim +=1
    if resp == 'H' or resp == 'h' and like == 'n' or like =='N':
        homemNao +=1
    idade = input("Qual a idade?  ")
    resp = input("Deseja continuar?S/N  ")
    cont += 1

print(f"OPERAÇÃO ENCERRADA")
percentual = cont / contN * 100
print(f"Total de entrevistados: {cont}")
print(f"Quantidade de pessoas que disseram sim: {contS}")
print(f"Quantidade de pessoas que disseram não: {contN}")
print(f"Mulheres que disseram sim: {mulherSim}")
print(f"Percentual de pessoas que disseram não: {percentual} %")