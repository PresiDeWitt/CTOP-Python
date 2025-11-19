
palabra = input("Introduce una palabra: ")

if palabra == "":
    print("No has introducido ninguna palabra.")
else:
    contador = 0
    for ch in palabra:
        if ch.isalpha():
            contador += 1
    print(f"La palabra '{palabra}' tiene {contador} letras.")

