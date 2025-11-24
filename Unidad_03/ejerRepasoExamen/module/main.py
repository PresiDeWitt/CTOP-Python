from operaciones import suma, resta

def main():
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    sumarNums = suma(num1, num2)
    restarNums = resta(num1, num2)
    print(f"La suma de {num1} y {num2} es: {sumarNums}")
    print(f"La resta de {num1} y {num2} es: {restarNums}")

if __name__ == "__main__":
    main()
