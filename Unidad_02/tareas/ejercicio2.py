"""
Autor: Alejandro
Fecha: 19/11/2025
Descripción: Programa que pide un número entero y determina si es par o impar
             (Implementación del algoritmo del ejercicio 1)

Unidad 2 - OPT2 - Tarea individual
RA2_b) Escribir código en Python que implemente algoritmos diseñados

Ejemplo de entrada: 
    Introduce un número entero: 10
    
Ejemplo de salida:
    El número 10 es par

Ejemplo de entrada: 
    Introduce un número entero: 7
    
Ejemplo de salida:
    El número 7 es impar
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
    # Un número es par si el residuo de dividirlo entre 2 es 0
    if num % 2 == 0:
        # Mostrar resultado: es par
        print(f"El número {num} es par")
    else:
        # Mostrar resultado: es impar
        print(f"El número {num} es impar")
    
    print()
    print("=" * 60)
    
except ValueError:
    # Manejo de error si el usuario no introduce un número válido
    print("Error: Debes introducir un número entero válido")
    print("=" * 60)


