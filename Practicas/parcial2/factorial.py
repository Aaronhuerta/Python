def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
num = float(input("Introduce un número para calcular su factorial: "))
print(f"El factorial de {num} es {factorial(num)}")