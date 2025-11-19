# Autor: Alejandro
# Fecha: 17/11/2025
# Descripción: Programa que calcula la suma de los números del 1 al 1.000.000
# de dos formas diferentes y mide el tiempo de ejecución para evaluar el rendimiento.
#
# Ejemplo de salida:
# === Versión 1: Usando bucle for ===
# Suma: 500000500000
# Tiempo: 0.0523 segundos
#
# === Versión 2: Usando sum(range()) ===
# Suma: 500000500000
# Tiempo: 0.0089 segundos

import time

# Versión 1: Usando un bucle for
print('=== Versión 1: Usando bucle for ===')
inicio = time.time()

suma_for = 0
for i in range(1, 1000001):
    suma_for += i

fin = time.time()
tiempo_for = fin - inicio

print(f'Suma: {suma_for}')
print(f'Tiempo: {tiempo_for:.4f} segundos')

print()  # Línea en blanco para separar las versiones

# Versión 2: Usando la función sum(range())
print('=== Versión 2: Usando sum(range()) ===')
inicio = time.time()

suma_range = sum(range(1, 1000001))

fin = time.time()
tiempo_range = fin - inicio

print(f'Suma: {suma_range}')
print(f'Tiempo: {tiempo_range:.4f} segundos')

print()  # Línea en blanco

# Comparación de rendimiento
print('=== Comparación de rendimiento ===')
if tiempo_for < tiempo_range:
    diferencia = ((tiempo_for / tiempo_range) - 1) * 100
    print(f'El bucle for es más rápido por {abs(diferencia):.2f}%')
else:
    diferencia = ((tiempo_range / tiempo_for) - 1) * 100
    print(f'La función sum(range()) es más rápida por {abs(diferencia):.2f}%')
print(f'Diferencia de tiempo: {abs(tiempo_for - tiempo_range):.4f} segundos')
# Autor: Alejandro
# Fecha: 17/11/2025
# Descripción: Solicita tres números enteros al usuario y muestra cuál es el mayor
# usando condicionales múltiples (if-elif-else)
#
# Ejemplo de entrada/salida:
# Introduce el primer número: 5
# Introduce el segundo número: 12
# Introduce el tercer número: 8
# El mayor número es: 12

# Solicitar tres números enteros al usuario
num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))
num3 = int(input('Introduce el tercer número: '))

# Determinar cuál es el mayor usando condicionales múltiples
if num1 >= num2 and num1 >= num3:
    print(f'El mayor número es: {num1}')
elif num2 >= num1 and num2 >= num3:
    print(f'El mayor número es: {num2}')
else:
    print(f'El mayor número es: {num3}')

