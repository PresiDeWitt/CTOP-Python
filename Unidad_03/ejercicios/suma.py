i = 1
suma = 0
pares = []

while i <= 20:
    if i % 2 == 0:
        pares.append(i)
        suma += i
    i += 1

print(f'Números pares del 1 al 20: {pares}')
print(f'Suma de los números pares: {suma}')
