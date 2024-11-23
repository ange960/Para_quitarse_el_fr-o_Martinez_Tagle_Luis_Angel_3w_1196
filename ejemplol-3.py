def filtrar_palabras(lista_palabras, n):
    # Usamos una lista de comprensión para filtrar las palabras con más de n caracteres
    palabras_filtradas = [palabra for palabra in lista_palabras if len(palabra) > n]
    
    return palabras_filtradas

# Ejemplo de uso
lista_de_palabras = ["neymar jr ", "cristiano ronaldo ", "messi", "ronaldhiño", "puyol", "haaland"]
n = 5
resultado = filtrar_palabras(lista_de_palabras, n)
print("Palabras con más de", n, "caracteres:", resultado)
