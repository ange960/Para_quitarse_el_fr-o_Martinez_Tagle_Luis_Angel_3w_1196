def mas_larga(lista_palabras):
    # Verificamos si la lista está vacía
    if len(lista_palabras) == 0:
        return None  # o lanzar un error si lo prefieres
    
    # Inicializamos la palabra más larga con la primera de la lista
    palabra_larga = lista_palabras[0]
    
    # Iteramos a través de la lista para encontrar la palabra más larga
    for palabra in lista_palabras:
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra  # Actualizamos si encontramos una palabra más larga
    
    return palabra_larga

# Ejemplo de uso
lista_de_palabras = ["valentin", "piedra", "gutierres ", "tagle", "ricardo"]
resultado = mas_larga(lista_de_palabras)
print("La palabra más larga es:", resultado)
