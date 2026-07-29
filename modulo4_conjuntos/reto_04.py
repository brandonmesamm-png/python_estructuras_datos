# Definir tienda_centro, tienda_norte y tienda_sur
tienda_centro = {"Laptop", "Mouse", "Teclado", "Monitor"}
tienda_norte = {"Laptop", "Impresora", "Mouse", "Parlantes"}
tienda_sur = {"Monitor", "Teclado", "Webcam", "Mouse"}

# Calcular catalogo_completo con union()
catalogo_completo = tienda_centro.union(tienda_norte).union(tienda_sur)

# Calcular productos_comunes con intersection()
productos_comunes = tienda_centro.intersection(tienda_norte).intersection(tienda_sur)

# Exclusivos de cada tienda con difference(union())
exclusivos_centro = tienda_centro.difference(tienda_norte.union(tienda_sur))
exclusivos_norte = tienda_norte.difference(tienda_centro.union(tienda_sur))
exclusivos_sur = tienda_sur.difference(tienda_centro.union(tienda_norte))

# Verificar pares con isdisjoint()
print("¿Centro y Norte no comparten productos?:", tienda_centro.isdisjoint(tienda_norte))
print("¿Centro y Sur no comparten productos?:", tienda_centro.isdisjoint(tienda_sur))
print("¿Norte y Sur no comparten productos?:", tienda_norte.isdisjoint(tienda_sur))

# Definir usuario1, usuario2, usuario3
usuario1 = {"Python", "Java", "C++"}
usuario2 = {"Python", "JavaScript", "SQL"}
usuario3 = {"Python", "Java", "SQL", "C++"}

# Calcular con & | - ^ <= y mostrar resumen
print("\n=== OPERACIONES CON CONJUNTOS ===")

print("Intersección (usuario1 & usuario2):", usuario1 & usuario2)

print("Unión (usuario1 | usuario2):", usuario1 | usuario2)

print("Diferencia (usuario1 - usuario2):", usuario1 - usuario2)

print("Diferencia simétrica (usuario1 ^ usuario2):", usuario1 ^ usuario2)

print("¿usuario1 es subconjunto de usuario3?:", usuario1 <= usuario3)

print("\n=== CATÁLOGO DE TIENDAS ===")
print("Catálogo completo:", catalogo_completo)
print("Productos comunes:", productos_comunes)
print("Exclusivos Centro:", exclusivos_centro)
print("Exclusivos Norte:", exclusivos_norte)
print("Exclusivos Sur:", exclusivos_sur)