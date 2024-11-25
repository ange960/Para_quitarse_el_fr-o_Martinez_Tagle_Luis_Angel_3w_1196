def contar_vocales(palabra):
    # Convertimos la palabra a minúsculas para no tener en cuenta mayúsculas
    palabra = palabra.lower()
    
    # Inicializamos un diccionario para contar las vocales
    contador_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Recorremos cada letra de la palabra y contamos las vocales
    for letra in palabra:
        if letra in contador_vocales:
            contador_vocales[letra] += 1
    
    # Devolvemos el contador de las vocales
    return contador_vocales

# Pedimos al usuario que ingrese la palabra
palabra_usuario = input("¡Escribe una palabra para contar las vocales: ")

# Llamamos a la función y mostramos el resultado
resultado = contar_vocales(palabra_usuario)

# Imprimimos el resultado
print("Contador de vocales:")
for vocal, cantidad in resultado.items():
    print(f"{vocal.upper()}: {cantidad}")
