#!/usr/bin/env python3
#
#   Programa para pedir la edad al usuario y asignarlo a un rango de edad establecido
#   - Valida entrada (entero, rango 0-120)
#   - Clasifica en: Niño (0-15), Adolescente (16-17), Joven adulto (18-25), Adulto (26-64), Adulto mayor (65+)
#   - Muestra una nota especial si la edad está entre 18 y 25
#

def pedir_edad() -> int:
    """Pide la edad al usuario repetidamente hasta recibir un entero válido entre 0 y 120.
    Maneja EOF para salidas en piping.
    """
    while True:
        try:
            s = input("Ingrese su edad: ").strip()
        except EOFError:
            print("\nNo hay más entrada. Saliendo...")
            raise SystemExit(1)

        if s == "":
            print("Entrada vacía. Intente de nuevo.")
            continue

        try:
            edad = int(s)
        except ValueError:
            print("Entrada inválida: por favor ingrese un número entero.")
            continue

        if not (0 <= edad <= 120):
            print("Edad debe estar entre 0 y 120. Intente de nuevo.")
            continue

        return edad

    # Código técnicamente inalcanzable: añadimos una excepción para dejar claro al analizador
    # que la función nunca devuelve `None`.
    raise RuntimeError("No se pudo obtener la edad — flujo inesperado")


def categorizar_edad(edad: int) -> str:
    """Devuelve una cadena con la categoría de edad para un entero válido.

    Categorías usadas:
    - Niño: 0-15
    - Adolescente: 16-17
    - Joven adulto: 18-25
    - Adulto: 26-64
    - Adulto mayor: 65+
    """
    if edad <= 15:
        return "Niño (0-15)"
    if 16 <= edad <= 17:
        return "Adolescente (16-17)"
    if 18 <= edad <= 25:
        return "Joven adulto (18-25)"
    if 26 <= edad <= 64:
        return "Adulto (26-64)"
    return "Adulto mayor (65+)"




if __name__ == "__main__":
    edad = pedir_edad()
    categoria = categorizar_edad(edad)
    print(f"Tu edad: {edad} -> {categoria}")
