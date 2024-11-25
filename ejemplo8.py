# Definimos una lista con nombres
nombres = ["Ana", "Pedro", "Alberto", "Luis", "Andrés", "María", "Antonio", "Carlos", "Alicia"]

# Pedimos al usuario que ingrese la letra que quiere buscar
letra = input("¡Elige una letra para buscar nombres que comiencen con ella: ").lower()

# Filtramos los nombres que empiezan con la letra elegida
nombres_con_letra = [nombre for nombre in nombres if nombre.lower().startswith(letra)]

# Imprimimos el resultado
print(f"Cantidad de nombres que comienzan con '{letra.upper()}': {len(nombres_con_letra)}")
