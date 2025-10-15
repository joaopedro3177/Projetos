numeros = []
numero = 0
resp = 0
numeroMaior = 0
numeroMenor = 0

while resp != 3:
    resp = int(input("Maior e Menor: \n 1 - Armazenar um número \n 2  - Mostrar o menor e o maior \n 3 - Sair"))
    if resp == 1:
        numero = int(input("Digite um número para armazenar:"))
        numeros += [numero]

    elif resp == 2:
        numeroMaior = numeros[0]
        numeroMenor = numeros[0]
        for cont in numeros:
            if numeroMaior < numeros[cont]:
                numeroMaior = numeros[cont]
                numeroMenor = numeroMaior

            else:
                numeroMenor = numeros[cont]

        print("O menor número é ",numeroMenor)
        print("O maior número é ",numeroMaior)


    elif resp == 3:
        print("Programa encerrado!")



    else:
        print("Opção inválida!")

        