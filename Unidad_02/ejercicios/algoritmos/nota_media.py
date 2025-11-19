
notas = []
alumnoX = [
    10,
    5.5,
    4.5,
    6
]
alumnoY = [
    8.5,
    4,
    5.7,
    9.2
]
alumnoA = [
    10,
    10,
    0,
    3,9
]
notas.extend(alumnoX)
notas.extend(alumnoY)
notas.extend(alumnoA)

media = sum(notas) / len(notas)

print("La media de la clase son: " + str(media))