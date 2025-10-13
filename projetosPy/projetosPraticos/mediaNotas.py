notas = []
cont = 0
nota = 0
soma = 0
media = 0

while cont <= 10:
    nota = int(input("Digite uma nota: "))
    notas.append(nota)
    soma += notas[cont]
    cont += 1
    
media = soma / 10

print("A média das notas é de ", media)

