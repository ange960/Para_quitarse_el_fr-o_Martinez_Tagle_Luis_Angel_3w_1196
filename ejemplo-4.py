def contar_mayusculas(cadena):
    # Inicializamos el contador de letras mayúsculas
    contador = 0
    
    # Iteramos a través de cada carácter de la cadena
    for char in cadena:
        if char.isupper():  # Verificamos si el carácter es una letra mayúscula
            contador += 1
    
    return contador

# Solicitar al usuario que ingrese una cadena
cadena_usuario = input("Por favor, ingresa una cadena: ")

# Contar las letras mayúsculas en la cadena
numero_mayusculas = contar_mayusculas(cadena_usuario)

# Mostrar el resultado
print(f"La cantidad de letras mayúsculas en la cadena es: {numero_mayusculas}")
