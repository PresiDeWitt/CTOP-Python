"""
Autor: Alejandro
Fecha: 20/11/2025
Descripción: Realiza tres pruebas del programa del ejercicio 2 (par/impar)

Unidad 2 - OPT2 - Tarea individual
RA2_c) Realizar pruebas para validar la funcionalidad de los algoritmos
"""


def es_par_o_impar(num):
    if num % 2 == 0:
        return "par"
    else:
        return "impar"


pruebas = [
    {"número": 10, "esperado": "par"},
    {"número": 7, "esperado": "impar"},
    {"número": -8, "esperado": "par"},
]

for prueba in pruebas:
    obtenido = es_par_o_impar(prueba["número"])
    coincide = "OK COINCIDE" if obtenido == prueba["esperado"] else "NO COINCIDE"
    print(
        f"Número: {prueba['número']}, Esperado: {prueba['esperado']}, Obtenido: {obtenido}, {coincide}"
    )
