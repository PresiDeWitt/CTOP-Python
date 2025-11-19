import sys

a = input('Introduce un numero entero: ')
try:
    a = int(a)
    print('Que buen numero es el:', a)
except ValueError as e:
    print('Debes introducir un numero entero')
finally:
    print('Fin del programa')
    sys.exit(0)