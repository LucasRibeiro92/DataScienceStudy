from collections import Counter


def gm(x):
    return f"Bom dia {x.upper()}!"

print(gm('luquinhas'))

def vogais(x):
    return len([letra for letra in x.lower() if letra in 'aeiou'])

print(vogais('luquinhas'))

