"""
Autor: Alejandro
Fecha: 19/11/2025
Descripción: Explica el proceso de desarrollo del algoritmo par/impar y cómo adaptarlo

Unidad 2 - OPT2 - Tarea individual
RA2_e) Explicar el proceso de desarrollo de un algoritmo de forma clara

Ejemplo de entrada: Ejecución directa del script
Ejemplo de salida: Explicación del desarrollo del algoritmo
"""

print("=" * 80)
print("EXPLICACIÓN DEL PROCESO DE DESARROLLO DEL ALGORITMO")
print("=" * 80)
print()

print("PREGUNTA 1: ¿Cómo ideaste el algoritmo?")
print("-" * 80)
print()
print("Para desarrollar el algoritmo de determinar si un número es par o impar,")
print("primero identifiqué el concepto matemático clave: un número es par si es")
print("divisible entre 2, es decir, si el residuo de la división entre 2 es cero.")
print("Luego diseñé los pasos: solicitar entrada al usuario, aplicar el operador")
print("módulo (%) para obtener el residuo, usar una estructura condicional (if-else)")
print("para evaluar si ese residuo es 0, y finalmente mostrar el resultado apropiado.")
print("El diseño fue simple y directo porque el problema tiene una solución matemática")
print("clara y bien definida.")
print()

print("PREGUNTA 2: ¿Por qué funciona correctamente?")
print("-" * 80)
print()
print("El algoritmo funciona correctamente porque se basa en una propiedad matemática")
print("fundamental: el operador módulo (%) devuelve el residuo de una división entera.")
print("Si num % 2 == 0, significa que 2 divide exactamente a num sin dejar residuo,")
print("lo cual es la definición de número par. En caso contrario (residuo 1), el número")
print("es impar. Python garantiza que este operador funciona consistentemente para todos")
print("los enteros (positivos, negativos y cero), por lo que el algoritmo es fiable y")
print("produce resultados correctos en todos los casos de prueba.")
print()

print("PREGUNTA 3: ¿Qué pasos serían necesarios para adaptarlo a múltiplo de 3?")
print("-" * 80)
print()
print("Para adaptar el algoritmo y detectar si un número es múltiplo de 3, solo se")
print("necesitan dos modificaciones simples: cambiar el divisor en la operación módulo")
print("de 2 a 3 (num % 3), y ajustar los mensajes de salida para reflejar el nuevo")
print("concepto ('es múltiplo de 3' o 'no es múltiplo de 3'). La estructura del")
print("algoritmo permanece idéntica porque el principio es el mismo: un número es")
print("múltiplo de otro si el residuo de su división es cero. Esta adaptabilidad")
print("demuestra que el algoritmo está bien diseñado y puede generalizarse fácilmente.")
print()

print("=" * 80)
print("DEMOSTRACIÓN: ADAPTACIÓN DEL ALGORITMO PARA MÚLTIPLO DE 3")
print("=" * 80)
print()

print("CÓDIGO ORIGINAL (PAR/IMPAR):")
print("-" * 80)
print("num = int(input('Introduce un número: '))")
print("if num % 2 == 0:")
print("    print('Es par')")
print("else:")
print("    print('Es impar')")
print()

print("CÓDIGO ADAPTADO (MÚLTIPLO DE 3):")
print("-" * 80)
print("num = int(input('Introduce un número: '))")
print("if num % 3 == 0:  # ← Cambio: de 2 a 3")
print("    print('Es múltiplo de 3')  # ← Cambio: mensaje")
print("else:")
print("    print('No es múltiplo de 3')  # ← Cambio: mensaje")
print()

print("CAMBIOS REALIZADOS:")
print("-" * 80)
print("1. Operador módulo: num % 2 → num % 3")
print("2. Mensaje afirmativo: 'Es par' → 'Es múltiplo de 3'")
print("3. Mensaje negativo: 'Es impar' → 'No es múltiplo de 3'")
print()

print("=" * 80)
print("EJECUCIÓN DEL ALGORITMO ADAPTADO:")
print("=" * 80)
print()

# Implementación del algoritmo adaptado
try:
    num = int(input("Introduce un número: "))
    if num % 3 == 0:
        print(f"[OK] El número {num} es múltiplo de 3")
        print(f"   ({num} ÷ 3 = {num // 3}, residuo = {num % 3})")
    else:
        print(f"[X] El número {num} NO es múltiplo de 3")
        print(f"   ({num} ÷ 3 = {num // 3}, residuo = {num % 3})")
    
except ValueError:
    print("Error: Debes introducir un número entero válido")

print()
print("=" * 80)
print("CONCLUSIÓN:")
print("=" * 80)
print("El algoritmo es flexible y fácil de adaptar porque se basa en un patrón")
print("general: 'determinar si un número es divisible por otro'. Cambiando el")
print("divisor (2, 3, 4, 5...) podemos detectar múltiplos de cualquier número.")
print("=" * 80)
