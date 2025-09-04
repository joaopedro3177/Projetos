#ex03
contVogais = 0
cont = 0
palavra = input("Digite uma palavra:")

palavra = palavra.lower()

while cont < len(palavra):
    letra = palavra[cont]

    if letra == "a":
        contVogais += 1

    elif letra == "e":
        contVogais += 1
        
    elif letra == "i":
        contVogais += 1

    elif letra == "o":
        contVogais += 1

    elif letra == "u":
        contVogais += 1

    cont += 1

print("A palavra tem ", contVogais, " Vogais!")

