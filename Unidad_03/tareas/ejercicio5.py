"""
Autor: Alejandro
Fecha: 19/11/2025
Descripción: Programa que calcula la suma de los números del 1 al 1.000.000
             de dos formas diferentes y mide el tiempo de ejecución para evaluar
             el rendimiento

Unidad 3 - OPT3 - Tarea individual
RA2_d) Evaluar el rendimiento de los programas desarrollados

Ejemplo de salida:
    === Versión 1: Usando bucle for ===
    Suma: 500000500000
    Tiempo: 0.0523 segundos

    === Versión 2: Usando sum(range()) ===
    Suma: 500000500000
    Tiempo: 0.0089 segundos

    === Comparación de rendimiento ===
    La función sum(range()) es más rápida por 487.64%

"""

import time

# Suma con bucle for
inicio = time.time()
suma = 0
for i in range(1, 1000001):
    suma += i
print("Suma con for:", suma, "Tiempo:", time.time() - inicio, "segundos")

# Suma con sum(range)
inicio = time.time()
suma = sum(range(1, 1000001))
print("Suma con sum:", suma, "Tiempo:", time.time() - inicio, "segundos")
