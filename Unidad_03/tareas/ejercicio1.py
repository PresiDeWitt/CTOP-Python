"""
Autor: Alejandro
Fecha: 19/11/2025
Descripción: Solicita tres números enteros al usuario y muestra cuál es el mayor
             usando condicionales múltiples (if-elif-else)

Unidad 3 - OPT3 - Tarea individual
RA3_a) Implementar correctamente estructuras de control en programas en Python

Ejemplo de entrada: 
    Introduce el primer número: 5
    Introduce el segundo número: 12
    Introduce el tercer número: 8
    
Ejemplo de salida:
    El mayor número es: 12
"""

print("=" * 60)
print("PROGRAMA: ENCONTRAR EL MAYOR DE TRES NÚMEROS")
print("=" * 60)
print()

# Solicitar tres números enteros al usuario
try:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))
    
    print()
    print("-" * 60)
    
    # Determinar cuál es el mayor usando condicionales múltiples (if-elif-else)
    if num1 >= num2 and num1 >= num3:
        # num1 es el mayor o igual a los otros dos
        print(f"El mayor número es: {num1}")
        if num1 == num2 == num3:
            print("(Los tres números son iguales)")
        elif num1 == num2 or num1 == num3:
            print("(Hay números iguales)")
    
    elif num2 >= num1 and num2 >= num3:
        # num2 es el mayor o igual a los otros dos
        print(f"El mayor número es: {num2}")
        if num2 == num3:
            print("(Hay números iguales)")
    
    else:
        # num3 es el mayor
        print(f"El mayor número es: {num3}")
    
    print("-" * 60)
    
    # Información adicional: mostrar los tres números ordenados
    numeros = [num1, num2, num3]
    numeros_ordenados = sorted(numeros, reverse=True)
    print(f"Números ordenados de mayor a menor: {numeros_ordenados}")
    print("=" * 60)

except ValueError:
    print()
    print("Error: Debes introducir números enteros válidos")
    print("=" * 60)
