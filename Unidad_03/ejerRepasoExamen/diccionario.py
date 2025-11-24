# Crear diccionario para el usuario
usuario = {
    "nombre": "Alejandro",
    "edad": 20,
    "estudiante": True
}

# Añadir dos diccionarios más para compañeros
companero1 = {
    "nombre": "Ana",
    "edad": 17,
    "estudiante": True
}

companero2 = {
    "nombre": "Luis",
    "edad": 35,
    "estudiante": False
}

# Lista de personas
personas = [usuario, companero1, companero2]

# Función para mostrar mensaje según edad
def mostrar_mensaje(persona):
    edad = persona["edad"]
    nombre = persona["nombre"]
    if edad < 18:
        print(f"{nombre}: Eres menor de edad")
    elif 18 <= edad <= 25:
        print(f"{nombre}: Eres muy joven")
    elif 26 <= edad <= 40:
        print(f"{nombre}: Eres joven")
    else:
        print(f"{nombre}: Ya no eres joven")

# Mostrar mensajes para cada persona
for persona in personas:
    mostrar_mensaje(persona)

