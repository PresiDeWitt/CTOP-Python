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

print("=" * 80)
print("EVALUACIÓN DE RENDIMIENTO: SUMA DE NÚMEROS DEL 1 AL 1.000.000")
print("=" * 80)
print()

# VERSIÓN 1: Usando un bucle for
print("=" * 80)
print("VERSIÓN 1: Usando bucle for")
print("=" * 80)
print()
print("Código:")
print("  suma_for = 0")
print("  for i in range(1, 1000001):")
print("      suma_for += i")
print()

inicio = time.time()

suma_for = 0
for i in range(1, 1000001):
    suma_for += i

fin = time.time()
tiempo_for = fin - inicio

print(f"Suma: {suma_for}")
print(f"Tiempo: {tiempo_for:.4f} segundos")
print()

# VERSIÓN 2: Usando la función sum(range())
print("=" * 80)
print("VERSIÓN 2: Usando sum(range())")
print("=" * 80)
print()
print("Código:")
print("  suma_range = sum(range(1, 1000001))")
print()

inicio = time.time()

suma_range = sum(range(1, 1000001))

fin = time.time()
tiempo_range = fin - inicio

print(f"Suma: {suma_range}")
print(f"Tiempo: {tiempo_range:.4f} segundos")
print()

# COMPARACIÓN DE RENDIMIENTO
print("=" * 80)
print("COMPARACIÓN DE RENDIMIENTO")
print("=" * 80)
print()

# Verificar que ambas versiones dan el mismo resultado
if suma_for == suma_range:
    print(f"[OK] Ambas versiones producen el mismo resultado: {suma_for}")
else:
    print(f"ERROR: Los resultados no coinciden")
    print(f"   Versión 1: {suma_for}")
    print(f"   Versión 2: {suma_range}")

print()
print("-" * 80)

# Comparar tiempos de ejecución
if tiempo_for < tiempo_range:
    porcentaje = ((tiempo_range / tiempo_for) - 1) * 100
    print(f"[GANADOR] El bucle for es más rápido")
    print(f"   Ventaja: {porcentaje:.2f}% más rápido que sum(range())")
else:
    porcentaje = ((tiempo_for / tiempo_range) - 1) * 100
    print(f"[GANADOR] La función sum(range()) es más rápida")
    print(f"   Ventaja: {porcentaje:.2f}% más rápido que el bucle for")

print()
print(f"Diferencia de tiempo: {abs(tiempo_for - tiempo_range):.4f} segundos")

print()
print("-" * 80)
print("ANÁLISIS:")
print("-" * 80)
print()
print("• El bucle for ejecuta iteraciones en Python puro, lo que es más lento")
print("  porque cada operación += y cada acceso a la variable suma_for tiene")
print("  overhead del intérprete de Python.")
print()
print("• La función sum(range()) está implementada en C a bajo nivel, lo que")
print("  permite optimizaciones y ejecución más rápida. Además, range() genera")
print("  los números de forma eficiente sin crear una lista completa en memoria.")
print()
print("CONCLUSIÓN:")
print("  Para operaciones matemáticas sobre rangos grandes, las funciones")
print("  integradas de Python (sum, max, min, etc.) son significativamente")
print("  más rápidas que los bucles manuales.")
print()
print("=" * 80)

# INFORMACIÓN ADICIONAL: Fórmula matemática
print()
print("NOTA ADICIONAL: Fórmula matemática de Gauss")
print("-" * 80)
print("La suma de los números del 1 al n se puede calcular con la fórmula:")
print("  Suma = n × (n + 1) / 2")
print()
print("Para n = 1.000.000:")

inicio = time.time()
n = 1000000
suma_formula = n * (n + 1) // 2
fin = time.time()
tiempo_formula = fin - inicio

print(f"  Suma = {suma_formula}")
print(f"  Tiempo: {tiempo_formula:.6f} segundos")
print()
print("Esta fórmula es instantánea (O(1)) comparada con iterar (O(n))")
print("=" * 80)

