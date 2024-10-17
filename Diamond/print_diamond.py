def print_diamond(letter):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = alphabet.index(letter)
    diamond = []

    # Parte superior do diamante
    for i in range(index + 1):
        spaces_before = ' ' * (index - i)
        if i == 0:
            line = spaces_before + alphabet[i]
        else:
            spaces_between = ' ' * (2 * i - 1)
            line = spaces_before + alphabet[i] + spaces_between + alphabet[i]
        diamond.append(line)

    # Parte inferior do diamante (espelhada)
    for i in range(index - 1, -1, -1):
        diamond.append(diamond[i])

    # Imprimir o diamante
    for line in diamond:
        print(line)

# Exemplos de uso
print_diamond('E')
print()
print_diamond('C')
