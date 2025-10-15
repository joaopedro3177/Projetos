nomes = []
resp = 0
nomeDigitado = ""


while resp != 3:
    resp = int(input("Armazenamento de nomes: \n 1 - Cadastrar um nome \n 2 - Vizualizar os nomes \n 3 - Sair"))

    if resp == 1:
        nomeDigitado = input("Digite um nome para armazenar: ")
        nomes += [nomeDigitado]

    elif resp == 2:
        print(nomes)

    elif resp == 3:
        print("Programa encerrado!")

    else:
        print("Digito inválido!")


