
print("----------------------------------------------------")
a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))
c = int(input("Digite o terceiro número:"))
print("----------------------------------------------------")

if a < b + c and  b < a + c  and c < a + b:
    if a == b and b == c and c == a:
        print("Triângulo equilátero.")
        print(f"Lado 1: {a}")
        print(f"Lado 2: {b}")
        print(f"Lado 3: {c}")
        print("----------------------------------------------------")
    elif  a == b or b == c or c == a:
        print("Triângulo isósceles.")
        print(f"Lado 1: {a}")
        print(f"Lado 2: {b}")
        print(f"Lado 3: {c}")
        print("----------------------------------------------------")
    elif a != b and b != c and c != a:
        print("Triângulo escaleno.")
        print(f"Lado 1: {a}")
        print(f"Lado 2: {b}")
        print(f"Lado 3: {c}")
        print("----------------------------------------------------")
else: 
    print("Não é um triângulo.")
    print("----------------------------------------------------")


