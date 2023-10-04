import random

palavra = random.choice(["python", "java", "javascript"])

palavra_oculta = ["_" for i in range(len(palavra))]

while True:
    letra = input("Digite uma letra: ")
    for i in range(len(palavra)):
        if palavra[i] == letra:
            palavra_oculta[i] = letra

print("Palavra oculta: " + " ".join(palavra_oculta))