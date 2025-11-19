# Autor: Alejandro
# Fecha: 17/11/2025
# Descripción: Crea un programa que pida dos números y una operación (+, -, *, /)
# y muestre el resultado. Usa condicionales y operadores aritméticos.
#
# Ejemplo de entrada/salida:
# Introduce el primer número: 10
# Introduce el segundo número: 5
# Introduce la operación (+, -, *, /): +
# Resultado: 10 + 5 = 15

# Solicitar dos números al usuario
num1 = float(input('Introduce el primer número: '))
num2 = float(input('Introduce el segundo número: '))

# Solicitar la operación
operacion = input('Introduce la operación (+, -, *, /): ')

# Realizar la operación según el operador introducido
if operacion == '+':
    resultado = num1 + num2
    print(f'Resultado: {num1} + {num2} = {resultado}')
elif operacion == '-':
    resultado = num1 - num2
    print(f'Resultado: {num1} - {num2} = {resultado}')
elif operacion == '*':
    resultado = num1 * num2
    print(f'Resultado: {num1} * {num2} = {resultado}')
elif operacion == '/':
    # Validar que no se divida por cero
    if num2 != 0:
        resultado = num1 / num2
        print(f'Resultado: {num1} / {num2} = {resultado}')
    else:
        print('Error: No se puede dividir por cero')
else:
    print('Error: Operación no válida. Usa +, -, * o /')

