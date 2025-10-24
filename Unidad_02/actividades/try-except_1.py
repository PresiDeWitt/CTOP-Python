from platform import architecture
from selectors import SelectSelector

texto = ''
try:
    f = open('data/archivo.txt','w')
   # texto = f.read()
    f.write('Hola muy buenas')

except IOError as e:
    print('Ocurrio un erro: ',e)
else:
    print('Se ha escrito correctamente el mensaje en el archivo')

finally:
    f.close()

