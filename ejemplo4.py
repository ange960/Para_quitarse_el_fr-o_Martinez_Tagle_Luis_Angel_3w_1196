
cadena = input("Ingrese una cadena: ")# Solicitar al usuario que ingrese una cadena

# Inicializar el contador de letras mayúsculas
contador_mayusculas = 0

# Recorrer cada carácter de la cadena
for caracter in cadena:
    # Verificar si el carácter es una letra mayúscula
    if caracter.isupper():
        contador_mayusculas += 1

# Mostrar el resultado
print(f"La cadena tiene {contador_mayusculas} letras mayúsculas.")
