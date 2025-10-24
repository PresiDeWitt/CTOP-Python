import sys
lista =[1,2,3,4]

try:
    for n in lista:
        print(n)
except IndexError as e:
    print(f"Error: {e}")
else:
    print("Se ha ejecutado correctamente")
finally:
    sys.exit(0)