texto = "Hola buenas tardes que tal como estais"

vocales = "aeiou"
conteo = sum(texto.lower().count(v) for v in vocales)

print(f"Vocales del texto: {conteo}")
