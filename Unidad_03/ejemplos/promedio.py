
def promedio(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total / len(numeros)

def main():
    nums = [2, 4, 6]
    print('lista',nums)
    print('Promedio',promedio(nums))
