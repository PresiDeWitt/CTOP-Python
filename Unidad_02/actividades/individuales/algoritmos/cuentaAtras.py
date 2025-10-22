import time

def cuentAtras(numero):
    for i in range(numero, 0, -1):
        print(i)
        time.sleep(1)
    print("Se acabo el tiempo jiji")
try:
    num = int(input("Ingrese un número para la cuenta atras: "))
except ValueError:
    print("El numero debe ser un numero entero")
    exit()
cuentAtras(num)