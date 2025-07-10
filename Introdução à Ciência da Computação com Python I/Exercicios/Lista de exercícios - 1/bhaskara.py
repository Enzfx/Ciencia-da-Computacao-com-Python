import math
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        # Garantir ordem crescente
        if raiz1 > raiz2:
            raiz1, raiz2 = raiz2, raiz1
        return f"as raízes da equação são {raiz1} e {raiz2}"
    elif delta == 0:
        raiz = -b / (2 * a)
        return f"a raiz dupla desta equação é {raiz}"
    else:
        return "esta equação não possui raízes reais"
    
raizes = calcular_raizes(a, b, c)
print(raizes)


