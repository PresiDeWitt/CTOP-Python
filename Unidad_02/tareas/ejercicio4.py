"""
Autor: Alejandro
Fecha: 19/11/2025
Descripción: Analiza código erróneo, identifica errores, corrige y ejecuta

Unidad 2 - OPT2 - Tarea individual
RA2_d) Identificar y solucionar errores en algoritmos

Ejemplo de entrada: Ejecución directa del script
Ejemplo de salida: Identificación de errores y código corregido funcionando
"""

print("=" * 80)
print("EJERCICIO DE DEPURACIÓN: IDENTIFICAR Y CORREGIR ERRORES")
print("=" * 80)
print()

# CÓDIGO ORIGINAL CON ERRORES
print("CÓDIGO ORIGINAL (CON ERRORES):")
print("-" * 80)
codigo_erroneo = '''
num = input("Introduce un número: ")
if num % 2 = 0:
    print("Es par")
else
    print("Es impar")
'''
print(codigo_erroneo)

# IDENTIFICACIÓN DE ERRORES
print("=" * 80)
print("IDENTIFICACIÓN DE ERRORES:")
print("=" * 80)
print()

print("ERROR 1: Tipo de dato incorrecto")
print("-" * 80)
print("Ubicación: Línea 1")
print("Problema:")
print("  input() devuelve una cadena (str), no se puede usar directamente")
print("  con el operador módulo (%) que requiere números enteros.")
print()
print("Solución:")
print("  Convertir la entrada a entero con int():")
print("  num = int(input('Introduce un número: '))")
print()

print("ERROR 2: Operador de asignación en vez de comparación")
print("-" * 80)
print("Ubicación: Línea 2")
print("Problema:")
print("  Se usa '=' (asignación) en lugar de '==' (comparación)")
print("  if num % 2 = 0:  ← INCORRECTO")
print()
print("Solución:")
print("  Usar el operador de comparación '==':")
print("  if num % 2 == 0:")
print()

print("ERROR 3: Falta de dos puntos (:) después del else")
print("-" * 80)
print("Ubicación: Línea 4")
print("Problema:")
print("  else  ← INCORRECTO (falta :)")
print("  Python requiere dos puntos después de else")
print()
print("Solución:")
print("  Añadir los dos puntos:")
print("  else:")
print()

# CÓDIGO CORREGIDO
print("=" * 80)
print("CÓDIGO CORREGIDO:")
print("=" * 80)
print()

codigo_corregido = '''
num = int(input("Introduce un número: "))
if num % 2 == 0:
    print("Es par")
else:
    print("Es impar")
'''
print(codigo_corregido)

# RESUMEN DE CORRECCIONES
print("=" * 80)
print("RESUMEN DE CORRECCIONES REALIZADAS:")
print("=" * 80)
print()
print("1. Línea 1: Añadido int() para convertir la entrada a entero")
print("2. Línea 2: Cambiado '=' por '==' en la condición")
print("3. Línea 4: Añadidos ':' después de else")
print()

# EJECUCIÓN DEL PROGRAMA CORREGIDO
print("=" * 80)
print("EJECUCIÓN DEL PROGRAMA CORREGIDO:")
print("=" * 80)
print()

# Implementación real del código corregido
try:
    num = int(input("Introduce un número: "))
    if num % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
    
    print()
    print("[OK] El programa se ha ejecutado correctamente")
    
except ValueError:
    print("Error: Debes introducir un número entero válido")

print()
print("=" * 80)
print("PRUEBAS DEL DEPURADOR DE VS CODE:")
print("=" * 80)
print()
print("Para probar este programa usando el depurador de VS Code:")
print()
print("1. Colocar un breakpoint en la línea: if num % 2 == 0:")
print("   (Clic en el margen izquierdo de la línea o presionar F9)")
print()
print("2. Presionar F5 o ir a Run → Start Debugging")
print()
print("3. Introducir un número cuando se solicite")
print()
print("4. El programa se detendrá en el breakpoint")
print()
print("5. Inspeccionar la variable 'num' en el panel de variables")
print()
print("6. Usar Step Over (F10) para ejecutar línea por línea")
print()
print("7. Observar cómo cambia el flujo según el valor de num % 2")
print()
print("=" * 80)
