# Autor: Alejandro
# Fecha: 17/11/2025
# Descripción: Pide un número entero positivo y muestra todos los números desde
# 1 hasta ese número utilizando un bucle for
#
# Ejemplo de entrada/salida:
# Introduce un número entero positivo: 5
# 1
# 2
# 3
# 4
# 5

# Solicitar un número entero positivo al usuario
numero = int(input('Introduce un número entero positivo: '))

# Validar que el número sea positivo
if numero > 0:
    # Mostrar todos los números desde 1 hasta el número introducido
    for i in range(1, numero + 1):
        print(i)
else:
    print('Error: Debes introducir un número positivo')

