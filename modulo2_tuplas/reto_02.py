# Definir catalogo como tupla de subtuplas
catalogo = (
    ("El Padrino", "Francis Ford Coppola", 1972, 9.2),
    ("Titanic", "James Cameron", 1997, 7.9),
    ("Avatar", "James Cameron", 2009, 7.8),
    ("Interestelar", "Christopher Nolan", 2014, 8.7),
)

# Recorrer catalogo con for desempaquetando los cuatro campos
print("=== Catálogo de películas ===")
for titulo, director, anio, calificacion in catalogo:
    print(f"{titulo} | {director} | {anio} | {calificacion}")

# Usar operador * para separar primera pelicula del resto
primera_pelicula, *resto = catalogo

print("\nPrimera película:")
print(primera_pelicula)

print("\nResto de películas:")
for pelicula in resto:
    print(pelicula)

# Definir buscar_por_director(director)
def buscar_por_director(director):
    return [pelicula for pelicula in catalogo if pelicula[1] == director]

# Definir obtener_estadisticas(peliculas)
def obtener_estadisticas(peliculas):
    calificaciones = [pelicula[3] for pelicula in peliculas]
    minimo = min(calificaciones)
    maximo = max(calificaciones)
    promedio = sum(calificaciones) / len(calificaciones)
    return minimo, maximo, promedio

# Llamar a buscar_por_director e imprimir coincidencias
director = "James Cameron"
coincidencias = buscar_por_director(director)

print(f"\nPelículas dirigidas por {director}:")
for pelicula in coincidencias:
    print(pelicula)

# Desempaquetar retorno de obtener_estadisticas
minima, maxima, promedio = obtener_estadisticas(catalogo)

# Imprimir minima, maxima y promedio
print("\n=== Estadísticas ===")
print("Calificación mínima:", minima)
print("Calificación máxima:", maxima)
print("Calificación promedio:", round(promedio, 2))