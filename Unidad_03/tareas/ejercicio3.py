"""
Autor: Alejandro
Fecha: 19/11/2025
Descripción: Programa que pide dos números y una operación (+, -, *, /)
             y muestra el resultado usando condicionales y operadores aritméticos

Unidad 3 - OPT3 - Tarea individual
RA2_b) Realizar entradas y salidas de datos de forma adecuada

Ejemplo de entrada: 
    Introduce el primer número: 10
    Introduce el segundo número: 5
    Introduce la operación (+, -, *, /): +
    
Ejemplo de salida:
    10.0 + 5.0 = 15.0
"""

print("=" * 30)
print("CALCULADORA")
print("=" * 30)
print()

# Solicitar los dos números al usuario
try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    
    # Solicitar la operación
    operacion = input("Introduce la operación (+, -, *, /): ").strip()
    
    print()
    print("-" * 30)
    
    # Realizar la operación según el operador introducido usando condicionales
    if operacion == "+":
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    
    elif operacion == "-":
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    
    elif operacion == "*":
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    
    elif operacion == "/":
        # Validar que no se divida por cero
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Error: No se puede dividir por cero")
    
    else:
        print(f"Error: Operación '{operacion}' no válida")
        print("Operaciones válidas: +, -, *, /")
    
    print("-" * 30)
    print("=" * 30)

except ValueError:
    print()
    print("Error: Debes introducir números válidos")
    print("=" * 30)
except ZeroDivisionError:
    print()
    print("Error: División por cero")
    print("=" * 30)

