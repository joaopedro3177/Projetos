# Sistema de cadastro em Python

resp = 0
resp1 = 0
nome = ""
idade = 0
endereco = ""
dataNascimento = ""
cpf = ""

while resp != 5:
    resp = int(input("Digite um número correspondente para o procedimento:\n 1 - Cadastrar \n 2 - Alterar \n 3 - Visualizar \n 4 - Excluir \n 5 - Sair"))


    if resp == 1:
        nome = input("Digite seu nome")
        idade = input("Digite sua idade")
        endereco = input("Digite seu endereço")
        dataNascimento = input("Digite sua data de nascimento")
        cpf = input("Digite seu CPF")
        print("Dados Cadastrados!")


    elif resp == 2:
        resp1 = int(input("Digite um número correspondente para alterar o que você deseja:\n 1 - Nome \n 2 - Idade \n 3 - Endereço \n 4 - Data de Nascimento \n 5 - CPF"))

        if resp1 == 1:
            nome = input("Digite seu nome")
            print("Dado cadastrado!")

        elif resp1 == 2:
            idade = input("Digite sua idade")
            print("Dado cadastrado!")

        elif resp1 == 3:
            endereco = input("Digite seu endereço")
            print("Dado cadastrado!")

        elif resp1 == 4:
            dataNascimento = input("Digite sua data de nascimento")
            print("Dado cadastrado!")

        elif resp1 == 5:
            cpf = input("Digite seu CPF")
            print("Dado cadastrado!")
        
        else:
            print("Opção inválida!")


        


    elif resp == 3:
        print(nome)
        print(idade)
        print(endereco)
        print(dataNascimento)
        print(cpf)

    elif resp == 4:
        nome = ""
        idade = 0
        endereco = ""
        dataNascimento = ""
        cpf = ""
        print("Dados Excluídos!")

    elif resp == 5:
        print("Programa encerrado!")

    else:
        print("Opção inválida!")
