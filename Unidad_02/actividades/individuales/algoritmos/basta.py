

palabras = []
peticiones = 0

while True:
    entrada = input("Introduce una palabra: ")
    peticiones += 1

    if entrada == "" or entrada.lower() == "basta":
      break
      palabras.append(entrada)
      print(" ".join(palabras))

    print(f"Has soportado estoicamente {peticiones} preguntas")

