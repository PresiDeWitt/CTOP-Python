"""
Autor: Alejandro
Fecha: 19/11/2025
Descripción: Diagrama de flujo que representa un algoritmo para determinar si un
             número es par o impar

Unidad 2 - OPT2 - Tarea individual
RA2_a) Crear diagramas de flujo que representen algoritmos de manera efectiva

DIAGRAMA DE FLUJO (representación textual):

    ┌─────────────────┐
    │     INICIO      │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────────────────┐
    │ Pedir número entero         │
    │ al usuario                  │
    │ num = input(...)            │
    └────────┬────────────────────┘
             │
             ▼
    ┌─────────────────────────────┐
    │ Convertir a entero          │
    │ num = int(num)              │
    └────────┬────────────────────┘
             │
             ▼
         ┌───────────┐
         │ ¿num % 2  │
         │  == 0?    │
         └─┬─────┬───┘
           │     │
        SÍ │     │ NO
           │     │
           ▼     ▼
    ┌──────────┐ ┌──────────┐
    │ Mostrar: │ │ Mostrar: │
    │ "Es par" │ │ "Es      │
    │          │ │  impar"  │
    └─────┬────┘ └────┬─────┘
          │           │
          └─────┬─────┘
                │
                ▼
         ┌─────────────┐
         │     FIN     │
         └─────────────┘

DESCRIPCIÓN DEL ALGORITMO:
1. INICIO
2. Solicitar al usuario que introduzca un número entero
3. Almacenar el número en una variable (num)
4. DECISIÓN: ¿El residuo de dividir num entre 2 es igual a 0?
   - SI → El número es par → Mostrar "Es par"
   - NO → El número es impar → Mostrar "Es impar"
5. FIN

SÍMBOLOS UTILIZADOS:
- Óvalo: Inicio y Fin del algoritmo
- Rectángulo: Proceso (asignación, cálculo)
- Rombo: Decisión (condición)
- Paralelogramo: Entrada/Salida de datos
- Flechas: Flujo de ejecución

Ejemplo de entrada: 10
Ejemplo de salida: El número 10 es par

Ejemplo de entrada: 7
Ejemplo de salida: El número 7 es impar
"""

# Este archivo contiene la REPRESENTACIÓN TEXTUAL del diagrama de flujo
# Para crear un diagrama visual, se pueden usar herramientas como:
# - draw.io (https://app.diagrams.net/)
# - Lucidchart (https://www.lucidchart.com/)
# - Microsoft Visio
# - Creately

print("=" * 70)
print("DIAGRAMA DE FLUJO: DETERMINAR SI UN NÚMERO ES PAR O IMPAR")
print("=" * 70)
print()
print("Este archivo contiene la representación textual del diagrama.")
print("Para visualizar el diagrama completo, consulta la sección de")
print("comentarios en el código fuente.")
print()
print("PASOS DEL ALGORITMO:")
print("-" * 70)
print("1. INICIO")
print("2. Pedir número entero al usuario")
print("3. Convertir entrada a tipo entero")
print("4. DECISIÓN: ¿num % 2 == 0?")
print("   └─ SI  → Mostrar 'Es par'")
print("   └─ NO  → Mostrar 'Es impar'")
print("5. FIN")
print()
print("=" * 70)
print("REPRESENTACIÓN ASCII DEL DIAGRAMA:")
print("=" * 70)
print()

# Imprimir el diagrama ASCII
diagrama = """
    ┌─────────────────┐
    │     INICIO      │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────────────────┐
    │ Pedir número entero         │
    │ al usuario                  │
    │ num = input(...)            │
    └────────┬────────────────────┘
             │
             ▼
    ┌─────────────────────────────┐
    │ Convertir a entero          │
    │ num = int(num)              │
    └────────┬────────────────────┘
             │
             ▼
         ┌───────────┐
         │ ¿num % 2  │
         │  == 0?    │
         └─┬─────┬───┘
           │     │
        SÍ │     │ NO
           │     │
           ▼     ▼
    ┌──────────┐ ┌──────────┐
    │ Mostrar: │ │ Mostrar: │
    │ "Es par" │ │ "Es      │
    │          │ │  impar"  │
    └─────┬────┘ └────┬─────┘
          │           │
          └─────┬─────┘
                │
                ▼
         ┌─────────────┐
         │     FIN     │
         └─────────────┘
"""

print(diagrama)
print()
print("=" * 70)
print("NOTA: Para el ejercicio 2, se implementará este algoritmo en Python.")
print("=" * 70)
