# Inventario con tres productos [nombre, cantidad, precio]
inventario = [
    ["Laptop", 10, 2500000],
    ["Mouse", 20, 50000],
    ["Teclado", 15, 120000]
]

def actualizar_precio(producto, nuevo_precio):
    producto[2] = nuevo_precio

def registrar_venta(producto, cantidad):
    if producto[1] >= cantidad:
        producto[1] -= cantidad
        print(f"Venta registrada de {cantidad} unidades de {producto[0]}")
    else:
        print("No hay suficiente inventario.")

def anadir_producto(nombre, cantidad, precio):
    inventario.append([nombre, cantidad, precio])

def mostrar_inventario():
    print("\n=== INVENTARIO ===")
    for producto in inventario:
        print(f"Producto: {producto[0]} | Cantidad: {producto[1]} | Precio: ${producto[2]}")

# Actualizar precio del segundo producto
actualizar_precio(inventario[1], 60000)

# Registrar venta del primer producto
registrar_venta(inventario[0], 2)

# Añadir un nuevo producto
anadir_producto("Monitor", 8, 800000)

# Mostrar inventario
mostrar_inventario()