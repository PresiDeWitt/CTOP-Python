"""
Ejercicio de manejo de archivos con try-except-finally
Escribe un mensaje en un archivo de texto con manejo de excepciones
"""

texto = ''
try:
    f = open('../../data/archivo.txt', 'w')
    f.write('Hola muy buenas')

except IOError as e:
    print('Ocurrió un error:', e)
else:
    print('Se ha escrito correctamente el mensaje en el archivo')

finally:
    f.close()

