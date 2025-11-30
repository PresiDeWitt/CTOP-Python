"""
Autor: Alejandro
Fecha: 30/11/2025
Descripción: Pide dos números y una operación (+, -, *, /) y muestra el resultado.

Unidad 3 - OPT3 - Tarea individual
RA2_b) Realizar entradas y salidas de datos adecuadas
"""

# Solicitar dos números y una operación
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

# Realizar la operación
if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: División entre cero"
else:
    resultado = "Operación no válida"

# Mostrar el resultado
print("Resultado:", resultado)
