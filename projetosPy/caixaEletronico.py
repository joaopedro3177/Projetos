saldo = int(input("Digite seu saldo:"))
resp = int(input("O que você gostaria de fazer? Digite: (1) para saque, (2) para deposito e (3) para vizualizar o saldo"))

if resp == 1 :
    valorSaque = int(input("Qual valor você gostaria de sacar?"))
    if valorSaque <= saldo:
        saldo -= valorSaque
        print("Valor sacado: ", valorSaque)
        print("Seu saldo atual ficou com um valor de: ", saldo)
    else:
        print("Saldo insuficiente!")

elif resp == 2:
    valorDeposito = int(input("Digite o valor a ser depositado:"))
    if valorDeposito > 0:
        


