"""
Autor: Alejandro
Fecha: 19/11/2025
Descripción: Programa que pide el nombre del usuario, saluda y muestra la longitud

Unidad 1 - OPT1 - Tarea individual
RA1_c) Aplicar la sintaxis básica en ejemplos prácticos en Python

"""

print("=" * 60)
print("PROGRAMA DE SALUDO PERSONALIZADO")
print("=" * 60)
print()

nombre = input("Introduce tu nombre: ")

print()
print(f"¡Hola, {nombre}! Bienvenido/a al programa.")

longitud_nombre = len(nombre)
print(f"Tu nombre tiene {longitud_nombre} caracteres.")

