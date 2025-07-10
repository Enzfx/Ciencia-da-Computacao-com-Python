numeroUm = int(input("Digite o primeiro número: "))
numeroDois = int(input("Digite o segundo número: "))
numeroTres = int(input("Digite o terceiro número: "))


def verificar_ordenacao(numeroUm, numeroDois, numeroTres):
    if numeroUm < numeroDois < numeroTres:
        return "crescente"
    elif numeroUm > numeroDois > numeroTres:
        return "não está em ordem crescente"
    else:
        return "não está em ordem crescente"
    
verificar_ordenacao = verificar_ordenacao(numeroUm, numeroDois, numeroTres)
print(verificar_ordenacao)
    
