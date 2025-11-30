"""
Autor: Alejandro
Fecha: 20/11/2025
Descripción: Programa que pide un número entero y determina si es par o impar
             (Implementación del algoritmo del ejercicio 1)

Unidad 2 - OPT2 - Tarea individual
RA2_b) Escribir código en Python que implemente algoritmos diseñados
"""

# INICIO del algoritmo
print("=" * 60)
print("DETERMINAR SI UN NÚMERO ES PAR O IMPAR")
print("=" * 60)
print()

# Pedir al usuario un número entero
try:
    num = int(input("Introduce un número entero: "))

    # Determinar si es par o impar
    if num % 2 == 0:
        print(f"El número {num} es par")
    else:
        print(f"El número {num} es impar")

except ValueError:
    print("Error: Debes introducir un número entero válido")
