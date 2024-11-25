def es_bisiesto(año):

    if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
        return True
    else:
        return False

# Pedimos al usuario que ingrese un año
año_usuario = int(input("Introduce un año para saber si es bisiesto: "))

# Llamamos a la función y mostramos el resultado
if es_bisiesto(año_usuario):
    print(f"El año {año_usuario} es un año bisiesto.")
else:
    print(f"El año {año_usuario} no es un año bisiesto.")
