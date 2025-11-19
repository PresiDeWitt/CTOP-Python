import time

def cuentAtras(numero):
    for i in range(numero, 0, -1):
        print(i)
        time.sleep(0.5)
    print("Se acabo el tiempo jiji")
try:
    num = int(input("Ingrese un numero entre 5 y 50: "))
    if num < 5 or num > 50:
        print("El numero debe estar entre 5 y 50")
        exit()
except ValueError:
    print("El numero debe ser un numero entero")
    exit()
cuentAtras(num)