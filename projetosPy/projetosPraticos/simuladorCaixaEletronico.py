notas = [200,100,50,20,10,5,2]
valor = 0
cont = 0
sobra = 0

valorSaque = int(input("Digite o valor que você quer sacar: "))

for cont in notas:
    caber =  valorSaque // cont
    valorSaque %= cont
    print("Em nota de ", cont)
    print("Vai precisar de ", caber)