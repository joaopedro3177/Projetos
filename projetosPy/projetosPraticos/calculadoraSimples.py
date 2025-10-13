num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = 0
resp = 0

while resp != 5:
    resp = int(input("Digite uma opção para calcular:\n 1 - Somar \n 2 - subtrair\n 3 - Multiplicar\n 4  - dividir\n 5 - Sair "))
    if resp == 1:
        resultado = num1 + num2
        print(resultado)

    elif resp == 2:
        resultado = num1 - num2
        print(resultado)

    elif resp == 3:
        resultado = num1 * num2
        print(resultado)

    elif resp == 4:
        resultado = num1 / num2
        print(resultado)

    elif resp == 5:
        print("Programa encerrado!")

    else:
        print("Opção inválida")


