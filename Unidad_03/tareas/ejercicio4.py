"""
Autor: Alejandro
Fecha: 30/11/2025
Descripción: Corrige errores en un programa que calcula el área de un rectángulo.

Unidad 3 - OPT3 - Tarea individual
RA2_c) Depurar errores en programas
"""


def area_rectangulo(base, altura):
    # Corrgimos el operador de potencia ** por el operador de multiplicación *
    return base * altura


try:
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))
    area = area_rectangulo(base, altura)
    # Y corregimos el eero de sintaxis de el print
    print("El área es:", area)
except ValueError:
    print("Error: Debes introducir valores numéricos.")
