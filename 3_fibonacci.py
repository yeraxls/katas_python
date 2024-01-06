# Escribe un programa que imprima los 50 primeros números de la sucesión
# de Fibonacci empezando en 0.
# - La serie Fibonacci se compone por una sucesión de números en
# la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...
def fibonacci():
    p = 0
    result = []
    while p < 51:
        if p < 2:
            result.append(p+0)
        else:
            result.append(result[p-1]+result[p-2])
        print(result[p])
        p += 1


fibonacci()