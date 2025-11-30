"""
Autor: Alejandro
Fecha: 20/11/2025
Descripción: Analiza código erróneo, identifica errores, corrige y ejecuta

Unidad 2 - OPT2 - Tarea individual
RA2_d) Identificar y solucionar errores en algoritmos
"""

# Código corregido
try:
    num = int(input("Introduce un número: "))
    if num % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
except ValueError:
    print("Error: Debes introducir un número entero válido")
