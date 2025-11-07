senhaCorreta = "jotama21"
resp = ""
cont = 0

while cont < 3:
    resp = input("Digite a senha correta:")

    if resp == senhaCorreta:
        cont = 3
        print("Você está logado!")



    elif cont == 2:
        print("Você tentou demais!")

    cont +=1






    



