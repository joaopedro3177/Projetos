cont = 0
contVogais = 0



palavra = input("Digite uma palavra para poder contar quantas vogais tem nela: ")

palavra = palavra.lower()

while cont < len(palavra):
    vogal = palavra[cont]

    if vogal == "a":
        contVogais += 1

    elif vogal == "e":
        contVogais += 1

    elif vogal == "i":
        contVogais += 1

    elif vogal == "o":
        contVogais += 1

    elif vogal == "u":
        contVogais += 1

    cont += 1

print("A palavra tem ", contVogais, "Vogais!")
        


