"""
Autor: Alejandro
Fecha: 19/11/2025
Descripción: Pide un número entero positivo y muestra todos los números desde 1 hasta ese número.

Unidad 3 - OPT3 - Tarea individual
RA3_a) Implementar estructuras de control en Python
"""

# Solicitar un número entero positivo
num = int(input("Introduce un número entero positivo: "))

# Validar que el número sea positivo
if num > 0:
    print("Números desde 1 hasta", num, ":")
    for i in range(1, num + 1):
        print(i)
else:
    print("El número debe ser positivo.")
