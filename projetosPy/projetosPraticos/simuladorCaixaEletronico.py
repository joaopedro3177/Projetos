notas = [2,5,10,20,50,100,200]
valor = 0
cont = 0

valorSaque = int(input("Digite o valor que você quer sacar: "))

for cont in notas:
    N6 = valorSaque / notas[6]
    N5 = valorSaque / notas[5]
    N4 = valorSaque / notas[4]
    N3 = valorSaque / notas[3]
    N2 = valorSaque / notas[2]
    N1 = valorSaque / notas[1]
    N0 = valorSaque / notas[0]

print("Nota de 2: Vai precisar  ", N6)
print("Nota de 5: Vai precisar de ",N5)
print("Nota de 10: Vai precisar de ",N4)
print("Nota de 20: Vai precisar de ",N3)
print("Nota de 50: Vai precisar de ",N2)
print("Nota de 100: Vai precisar de ",N1)
print("Nota de 200: Vai precisar de ",N0)
    




