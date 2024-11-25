# Solicitar al usuario que ingrese 10 edades
edades = []
for i in range(1, 11):
    edad = int(input(f"Ingrese la edad de la persona {i}: "))
    edades.append(edad)

# Convertir la lista de edades a una tupla
edades_tuple = tuple(edades)

# Contar cuántas personas tienen edades superiores a 20
personas_mayores_20 = sum(1 for edad in edades_tuple if edad > 20)

# Imprimir el resultado
print(f"Cantidad de personas con edades superiores a 20: {personas_mayores_20}")
