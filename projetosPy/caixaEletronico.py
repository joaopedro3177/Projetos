saldo = 0
resp = 0
saldo = 0
valorSaque = 0
valorDeposito = 0



saldo = int(input("Digite seu saldo:"))
resp = int(input("O que você gostaria de fazer? Digite: (1) para saque, (2) para deposito, (3) para vizualizar o saldo e (4) para sair"))



if resp == 1 :
    valorSaque = int(input("Qual valor você gostaria de sacar?"))
    while valorSaque <= 0:
        print("Não é posível sacar esse valor!")
        valorSaque = int(input("Qual valor você gostaria de sacar?"))
             
    if valorSaque <= saldo:
        saldo -= valorSaque
        print("Valor sacado: ", valorSaque)
        print("Seu saldo atual ficou com um valor de: ", saldo)

    else:
        print("Saldo insuficiente!")

elif resp == 2:
    valorDeposito = int(input("Digite o valor a ser depositado:"))
    while valorDeposito <= 0:
        print("Não é possível depositar ", valorDeposito, "Reais!")
        valorDeposito = int(input("Digite o valor a ser depositado:"))

   
        
    saldo += valorDeposito
    print("Valor de ", valorDeposito, "Reais depositado!")
    print("Seu saldo atual ficou com um valor de: ", saldo)


       
elif resp == 3:
    print("O seu saldo é ", saldo)


elif resp == 4:
    print("Prorama encerrado!")

else:
    print("Numero inválido, Digite novamente")
        

    





    