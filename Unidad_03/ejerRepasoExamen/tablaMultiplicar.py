
try:
    numUser = int(input("Introduce un número para mostrar su tabla de multiplicar, el numero tiene que estar entre el 5 y el 12: "))
    
    # Verificar si el número está en el rango
    if 5 <= numUser <= 12:
        print(f"Tabla de multiplicar del {numUser}:")
        for i in range(1, 11):
            resultado = numUser * i
            print(f"{numUser} x {i} = {resultado}")
    else:
        print("Número fuera de rango. Por favor, introduce un número entre 5 y 12.")
    
except ValueError:
    print("Entrada inválida. Por favor, introduce un número entero.")
