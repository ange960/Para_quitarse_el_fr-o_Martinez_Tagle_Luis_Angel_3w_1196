# Solicitar el año en curso
año_actual = int(input("Ingrese el año en curso: "))

# Solicitar los datos de tres personas (nombre y año de nacimiento)
personas = []
for i in range(1, 4):
    nombre = input(f"Ingrese el nombre de la persona {i}: ")
    año_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
    personas.append((nombre, año_nacimiento))

# Calcular cuántos años cumplirán durante el año en curso
for persona in personas:
    nombre, año_nacimiento = persona
    edad = año_actual - año_nacimiento
    print(f"{nombre} cumplirá {edad} años en el año {año_actual}.")
