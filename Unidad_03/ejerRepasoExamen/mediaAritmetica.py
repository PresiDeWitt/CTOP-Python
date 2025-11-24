try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
except ValueError:
    print("Entrada inválida. Por favor, introduce números válidos.")
else:
    media = (num1 + num2) / 2
    print(f"La media aritmética de {num1} y {num2} es: {media}")



