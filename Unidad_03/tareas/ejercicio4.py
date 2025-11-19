# Autor: Alejandro
# Fecha: 17/11/2025
# Descripción: Programa que calcula el área de un rectángulo.
# Se ha corregido el código con errores proporcionado.
#
# ERRORES CORREGIDOS:
# 1. Error de sintaxis en la línea print - faltaba una coma entre el texto y la variable
# 2. Error lógico - se usaba ** (potencia) en lugar de * (multiplicación)
# 3. Error de tipo - input() devuelve string, hay que convertir a float para operaciones numéricas
#
# Ejemplo de entrada/salida:
# Introduce la base: 5
# Introduce la altura: 3
# El area es: 15.0

def area_rectangulo(base, altura):
    # Corregido: usar * (multiplicación) en lugar de ** (potencia)
    area = base * altura
    return area

# Corregido: convertir los inputs a float para poder operar con ellos
base = float(input('Introduce la base: '))
altura = float(input('Introduce la altura: '))

# Calcular el área
area = area_rectangulo(base, altura)

# Corregido: añadir coma entre el string y la variable en el print
print('El area es:', area)

