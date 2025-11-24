"""
Autor: Alejandro
Fecha: 19/11/2025
Descripción: Pide un número entero positivo y muestra todos los números desde 1
             hasta ese número usando un bucle

Unidad 3 - OPT3 - Tarea individual
RA3_a) Implementar correctamente estructuras de control en programas en Python

Ejemplo de entrada: 
    Introduce un número entero positivo: 10
    
Ejemplo de salida:
    Números del 1 al 10:
    1 2 3 4 5 6 7 8 9 10
"""

print("=" * 60)
print("PROGRAMA: MOSTRAR NÚMEROS DEL 1 HASTA N")
print("=" * 60)
print()

# Solicitar un número entero positivo al usuario
try:
    numero = int(input("Introduce un número entero positivo: "))
    
    # Validar que el número sea positivo
    if numero <= 0:
        print()
        print("Error: El número debe ser positivo (mayor que 0)")
        print("=" * 60)
    else:
        print()
        print(f"Números del 1 al {numero}:")
        print("-" * 60)
        
        # Mostrar todos los números desde 1 hasta el número introducido
        # usando un bucle for
        for i in range(1, numero + 1):
            print(i, end=" ")
        
        print()  # Salto de línea
        
        # Información adicional
        print()
        print("-" * 60)
        print(f"Total de números mostrados: {numero}")
        print(f"Suma de todos los números: {sum(range(1, numero + 1))}")
        print("=" * 60)

except ValueError:
    print()
    print("Error: Debes introducir un número entero válido")
    print("=" * 60)

