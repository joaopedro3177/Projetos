import random

resp = 0
num = random.randint(1, 20)
cont = 0

resp = int(input("Digite um número de 1 até 10 para acertar o sorteado: "))
while resp != num:
    
    if resp < num:
        resp = int(input("Digite um número maior: "))
        cont+= 1

    else:
        resp = int(input("Digite um número menor: "))
        cont+= 1

    
print("Parabéns você acertou o número sorteado, com ", cont, " Tentativas!")
        
    


