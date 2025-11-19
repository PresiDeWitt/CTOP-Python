edad = int(input("Ingresa tu edad: "))
if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad < 64:
    print("Eres adulto")
else:
    print("Eres un adulto mayor")