# Definir ventas con 6 productos (producto, unidades, precio, categoria)
ventas = [
    ("Laptop", 5, 2500, "Tecnología"),
    ("Mouse", 20, 25, "Accesorios"),
    ("Teclado", 15, 45, "Accesorios"),
    ("Monitor", 8, 300, "Tecnología"),
    ("Silla", 10, 120, "Muebles"),
    ("Escritorio", 4, 250, "Muebles")
]

# List comp: valor_total = unidades * precio
valor_total = [unidades * precio for producto, unidades, precio, categoria in ventas]

# List comp con filtro: productos_destacados (valor > 1000)
productos_destacados = [
    producto
    for producto, unidades, precio, categoria in ventas
    if unidades * precio > 1000
]

# Dict comp: producto_info nombre: {valor, unidades}
producto_info = {
    producto: {
        "valor": unidades * precio,
        "unidades": unidades
    }
    for producto, unidades, precio, categoria in ventas
}

# Dict comp con filtro: ranking_premium (precio > 50)
ranking_premium = {
    producto: precio
    for producto, unidades, precio, categoria in ventas
    if precio > 50
}

# Set comp: categorias_unicas
categorias_unicas = {
    categoria
    for producto, unidades, precio, categoria in ventas
}

# Set comp con filtro: productos_baratos (precio <= 50)
productos_baratos = {
    producto
    for producto, unidades, precio, categoria in ventas
    if precio <= 50
}

# Combinar: resumen_formateado dict comp filtrado
resumen_formateado = {
    producto: f"{unidades} unidades - Total: ${unidades * precio}"
    for producto, unidades, precio, categoria in ventas
    if unidades * precio > 500
}

# Calcular e imprimir gran_total
gran_total = sum(valor_total)

print("=== VALOR TOTAL POR PRODUCTO ===")
print(valor_total)

print("\n=== PRODUCTOS DESTACADOS ===")
print(productos_destacados)

print("\n=== INFORMACIÓN DE PRODUCTOS ===")
for producto, info in producto_info.items():
    print(producto, "->", info)

print("\n=== RANKING PREMIUM ===")
for producto, precio in ranking_premium.items():
    print(producto, "-> $", precio)

print("\n=== CATEGORÍAS ÚNICAS ===")
print(categorias_unicas)

print("\n=== PRODUCTOS BARATOS ===")
print(productos_baratos)

print("\n=== RESUMEN FORMATEADO ===")
for producto, resumen in resumen_formateado.items():
    print(producto, "->", resumen)

print("\n=== GRAN TOTAL ===")
print(f"${gran_total}")