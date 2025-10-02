import random
resp = 0
cont = 0 
vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
vetorD = []




while resp != 5:
    resp = int(input("Digite um número correspondente para cada ação: \n 1 - Quina \n 2 - Sena \n 3 - Dupla sena \n 4 - Lotomainia \n 5 - Sair"))

    if resp == 1:

        for cont in range(5):
            num = random.randint(1, 80)
            vetor1.append(num)

        print(vetor1)




    elif resp == 2:

        for cont in range(6):
            num = random.randint(1, 60)
            vetor2.append(num)
        print(vetor2)



    elif resp == 3:

        for cont in range(6):
            num = random.randint(1, 50)
            vetor3.append(num)

        for cont in range(6):
            num = random.randint(1, 50)
            vetorD.append(num)

        print(vetor3)
        print(vetorD)



    elif resp == 4:
        for cont in range(50):
            num = random.randint(1, 99)
            vetor4.append(num)

        print(vetor4)


    elif resp == 5:
        print("Programa encerrado!")

