try:
    a = int(input("Introduzca el primer número para comparar: "))
    b = int(input("Introduzca el segundo número para comparar: "))

    if a > b:
        print(f"{a} es mayor que {b}")
    elif b > a:
        print(f"{b} es mayor que {a}")
    else:
        print(f"{a} y {b} son iguales")

except ValueError:
    print("Error: Debe introducir números enteros válidos")