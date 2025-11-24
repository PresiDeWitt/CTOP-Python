"""
Autor: Alejandro
Fecha: 19/11/2025
Descripción: Depuración de código con errores para calcular el área de un rectángulo.
             Se identifican y corrigen los errores del código proporcionado.

Unidad 3 - OPT3 - Tarea individual
RA2_c) Depurar errores en programas de manera eficiente

Ejemplo de entrada: 
    Introduce la base: 5
    Introduce la altura: 3
    
Ejemplo de salida:
    El area es: 15.0
"""

print("=" * 80)
print("EJERCICIO DE DEPURACIÓN: CÁLCULO DEL ÁREA DE UN RECTÁNGULO")
print("=" * 80)
print()

# CÓDIGO ORIGINAL CON ERRORES
print("CÓDIGO ORIGINAL (CON ERRORES):")
print("-" * 80)
codigo_erroneo = """
def area_rectangulo(base, altura):
    area = base ** altura
    return area

base = input('Introduce la base: ')
altura = input('Introduce la altura: ')
area = area_rectangulo(base, altura)
print('El area es: ' area)
"""
print(codigo_erroneo)

# IDENTIFICACIÓN DE ERRORES
print("=" * 80)
print("IDENTIFICACIÓN Y CORRECCIÓN DE ERRORES:")
print("=" * 80)
print()

print("1. ERROR DE SINTAXIS en la línea print")
print("-" * 80)
print("Ubicación: Línea 8")
print("Código erróneo:")
print("  print('El area es: ' area)")
print()
print("Problema:")
print("  Falta una coma (,) o el operador + entre el string y la variable")
print()
print("Corrección:")
print("  print('El area es:', area)  # Opción 1: con coma")
print("  print('El area es: ' + str(area))  # Opción 2: concatenación")
print("  print(f'El area es: {area}')  # Opción 3: f-string (recomendado)")
print()

print("2. ERROR LÓGICO en el cálculo del área")
print("-" * 80)
print("Ubicación: Línea 2")
print("Código erróneo:")
print("  area = base ** altura")
print()
print("Problema:")
print("  Se usa ** (potencia) en lugar de * (multiplicación)")
print("  El área de un rectángulo es base × altura, no base^altura")
print()
print("Corrección:")
print("  area = base * altura")
print()

print("3. ERROR DE TIPO en las entradas")
print("-" * 80)
print("Ubicación: Líneas 5 y 6")
print("Código erróneo:")
print("  base = input('Introduce la base: ')")
print("  altura = input('Introduce la altura: ')")
print()
print("Problema:")
print("  input() devuelve un string (str), no se puede operar matemáticamente")
print("  con strings sin convertirlos a números")
print()
print("Corrección:")
print("  base = float(input('Introduce la base: '))")
print("  altura = float(input('Introduce la altura: '))")
print()

# CÓDIGO CORREGIDO
print("=" * 80)
print("CÓDIGO CORREGIDO:")
print("=" * 80)
print()

codigo_corregido = """
def area_rectangulo(base, altura):
    area = base * altura  # Corregido: * en lugar de **
    return area

base = float(input('Introduce la base: '))  # Corregido: float()
altura = float(input('Introduce la altura: '))  # Corregido: float()
area = area_rectangulo(base, altura)
print(f'El area es: {area}')  # Corregido: f-string
"""
print(codigo_corregido)

# RESUMEN DE CORRECCIONES
print("=" * 80)
print("RESUMEN DE CORRECCIONES:")
print("=" * 80)
print("1. Línea 8: Añadido f-string para formatear correctamente el print")
print("2. Línea 2: Cambiado ** (potencia) por * (multiplicación)")
print("3. Líneas 5-6: Añadido float() para convertir input a número decimal")
print()

# EJECUCIÓN DEL PROGRAMA CORREGIDO
print("=" * 80)
print("EJECUCIÓN DEL PROGRAMA CORREGIDO:")
print("=" * 80)
print()


def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo"""
    area = base * altura  # Corregido: usar * (multiplicación)
    return area


try:
    # Corregido: convertir los inputs a float
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))
    
    # Calcular el área
    area = area_rectangulo(base, altura)
    
    # Corregido: usar f-string para el print
    print(f"El area es: {area}")
    
    print()
    print("[OK] El programa se ha ejecutado correctamente")

except ValueError:
    print("Error: Debes introducir números válidos")

print()
print("=" * 80)
print("PRUEBAS CON EL DEPURADOR DE VS CODE:")
print("=" * 80)
print()
print("Para depurar este programa en VS Code:")
print()
print("1. Colocar un breakpoint en: area = base * altura")
print("   (Clic en el margen izquierdo o presionar F9)")
print()
print("2. Presionar F5 para iniciar el depurador")
print()
print("3. Introducir valores de base y altura")
print()
print("4. El programa se detendrá en el breakpoint")
print()
print("5. Inspeccionar las variables 'base' y 'altura' en el panel Variables")
print()
print("6. Usar Step Over (F10) para ejecutar la multiplicación")
print()
print("7. Verificar que 'area' contiene el resultado correcto")
print()
print("8. Continuar (F5) para completar la ejecución")
print()
print("=" * 80)

