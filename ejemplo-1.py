def max_in_list(numeros):
    # Verificamos si la lista está vacía
    if len(numeros) == 0:
        return None  # o lanzar un error si lo prefieres

    # Inicializamos el máximo con el primer número de la lista
    maximo = numeros[0]

    # Iteramos a través de la lista para encontrar el valor máximo
    for num in numeros:
        if num > maximo:
            maximo = num  # Actualizamos el máximo si encontramos un número mayor

    return maximo

# Ejemplo de uso
lista_de_numeros = [3, 5, 1, 8, 2, 7]
resultado = max_in_list(lista_de_numeros)
print("El número más grande es:", resultado)
