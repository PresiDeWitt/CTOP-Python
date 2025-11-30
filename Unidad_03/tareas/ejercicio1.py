"""
Autor: Alejandro
Fecha: 25/11/2025
Descripción: Solicita tres números enteros al usuario y muestra cuál es el mayor.

Unidad 3 - OPT3 - Tarea individual
RA3_a) Implementar estructuras de control en Python
"""

# Solicitar tres números al usuario
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

# Determinar el mayor
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

# Mostrar el resultado
print(f"El número mayor es: {mayor}")
