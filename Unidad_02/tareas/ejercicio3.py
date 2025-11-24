"""
Autor: Alejandro
Fecha: 19/11/2025
Descripción: Realiza tres pruebas del programa del ejercicio 2 (par/impar)
             y presenta los resultados en formato tabla

Unidad 2 - OPT2 - Tarea individual
RA2_c) Realizar pruebas para validar la funcionalidad de los algoritmos

Ejemplo de entrada: Ejecución directa del script
Ejemplo de salida: Tabla con pruebas y resultados
"""

print("=" * 80)
print("PRUEBAS DEL ALGORITMO: DETERMINAR SI UN NÚMERO ES PAR O IMPAR")
print("=" * 80)
print()

# Función del algoritmo a probar
def es_par_o_impar(num):
    """
    Determina si un número es par o impar
    Retorna: 'par' o 'impar'
    """
    if num % 2 == 0:
        return "par"
    else:
        return "impar"


# TABLA DE PRUEBAS
print("┌─────────────────────┬─────────────────────┬─────────────────────┬────────────┐")
print("│ Número introducido  │ Resultado esperado  │ Resultado obtenido  │ ¿Coincide? │")
print("├─────────────────────┼─────────────────────┼─────────────────────┼────────────┤")

# PRUEBA 1: Número par
numero_prueba_1 = 10
esperado_1 = "par"
obtenido_1 = es_par_o_impar(numero_prueba_1)
coincide_1 = "OK" if esperado_1 == obtenido_1 else "FAIL"

print(f"│ {numero_prueba_1:^19} │ {esperado_1:^19} │ {obtenido_1:^19} │ {coincide_1:^10} │")

# PRUEBA 2: Número impar
numero_prueba_2 = 7
esperado_2 = "impar"
obtenido_2 = es_par_o_impar(numero_prueba_2)
coincide_2 = "OK" if esperado_2 == obtenido_2 else "FAIL"

print(f"│ {numero_prueba_2:^19} │ {esperado_2:^19} │ {obtenido_2:^19} │ {coincide_2:^10} │")

# PRUEBA 3: Número negativo (0 también se puede probar)
numero_prueba_3 = -8
esperado_3 = "par"
obtenido_3 = es_par_o_impar(numero_prueba_3)
coincide_3 = "OK" if esperado_3 == obtenido_3 else "FAIL"

print(f"│ {numero_prueba_3:^19} │ {esperado_3:^19} │ {obtenido_3:^19} │ {coincide_3:^10} │")

# PRUEBA 4 (EXTRA): Número 0
numero_prueba_4 = 0
esperado_4 = "par"
obtenido_4 = es_par_o_impar(numero_prueba_4)
coincide_4 = "OK" if esperado_4 == obtenido_4 else "FAIL"

print(f"│ {numero_prueba_4:^19} │ {esperado_4:^19} │ {obtenido_4:^19} │ {coincide_4:^10} │")

print("└─────────────────────┴─────────────────────┴─────────────────────┴────────────┘")

# RESUMEN DE PRUEBAS
print()
print("=" * 80)
print("RESUMEN DE PRUEBAS:")
print("=" * 80)

pruebas_exitosas = [coincide_1, coincide_2, coincide_3, coincide_4].count("OK")
total_pruebas = 4

print(f"Total de pruebas realizadas: {total_pruebas}")
print(f"Pruebas exitosas: {pruebas_exitosas} [OK]")
print(f"Pruebas fallidas: {total_pruebas - pruebas_exitosas} [FAIL]")
print()

if pruebas_exitosas == total_pruebas:
    print("RESULTADO: Todas las pruebas han pasado correctamente")
    print("   El algoritmo funciona como se esperaba.")
else:
    print("RESULTADO: Algunas pruebas han fallado")
    print("   Es necesario revisar el algoritmo.")

print("=" * 80)

# ANÁLISIS DETALLADO
print()
print("ANÁLISIS DETALLADO DE LAS PRUEBAS:")
print("-" * 80)
print()
print(f"Prueba 1 (número par positivo: {numero_prueba_1})")
print(f"  - Esperado: {esperado_1}")
print(f"  - Obtenido: {obtenido_1}")
print(f"  - Resultado: {'PASS [OK]' if coincide_1 == 'OK' else 'FAIL [X]'}")
print(f"  - Explicación: {numero_prueba_1} % 2 = {numero_prueba_1 % 2}, por tanto es {obtenido_1}")
print()

print(f"Prueba 2 (número impar positivo: {numero_prueba_2})")
print(f"  - Esperado: {esperado_2}")
print(f"  - Obtenido: {obtenido_2}")
print(f"  - Resultado: {'PASS [OK]' if coincide_2 == 'OK' else 'FAIL [X]'}")
print(f"  - Explicación: {numero_prueba_2} % 2 = {numero_prueba_2 % 2}, por tanto es {obtenido_2}")
print()

print(f"Prueba 3 (número negativo: {numero_prueba_3})")
print(f"  - Esperado: {esperado_3}")
print(f"  - Obtenido: {obtenido_3}")
print(f"  - Resultado: {'PASS [OK]' if coincide_3 == 'OK' else 'FAIL [X]'}")
print(f"  - Explicación: {numero_prueba_3} % 2 = {numero_prueba_3 % 2}, por tanto es {obtenido_3}")
print(f"  - Nota: Los números negativos también pueden ser pares o impares")
print()

print(f"Prueba 4 (cero: {numero_prueba_4})")
print(f"  - Esperado: {esperado_4}")
print(f"  - Obtenido: {obtenido_4}")
print(f"  - Resultado: {'PASS [OK]' if coincide_4 == 'OK' else 'FAIL [X]'}")
print(f"  - Explicación: {numero_prueba_4} % 2 = {numero_prueba_4 % 2}, por tanto es {obtenido_4}")
print(f"  - Nota: El cero se considera par por definición matemática")

print()
print("=" * 80)
