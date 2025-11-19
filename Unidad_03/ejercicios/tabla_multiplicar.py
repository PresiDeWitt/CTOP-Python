print("Tabla de multiplicar")
n = input("Número entero: ")
if n == "":
    print("Saliendo.")
else:
    try:
        n = int(n)
    except ValueError:
        print("No es un entero.")
    else:
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
