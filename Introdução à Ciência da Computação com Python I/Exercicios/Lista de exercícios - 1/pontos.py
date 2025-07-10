import math

def coordenadasDeUmPontoOrtogonal():
    x1 = float(input("Digite o valor de x1: "))
    y1 = float(input("Digite o valor de y1: "))
    x2 = float(input("Digite o valor de x2: "))
    y2 = float(input("Digite o valor de y2: "))
    return x1, y1, x2, y2

def calcularDistancia(x1, y1, x2, y2):
    distancia = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if distancia >= 10:
        return "longe"
    else:
        return "perto"

x1, y1, x2, y2 = coordenadasDeUmPontoOrtogonal()
resultado = calcularDistancia(x1, y1, x2, y2)
print(resultado)