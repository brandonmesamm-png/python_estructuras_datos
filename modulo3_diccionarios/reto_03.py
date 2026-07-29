# Definir ventas_por_region
ventas_por_region = {
    "Norte": {
        "T1": 12000,
        "T2": 15000,
        "T3": 18000,
        "T4": 20000
    },
    "Centro": {
        "T1": 10000,
        "T2": 14000,
        "T3": 16000,
        "T4": 19000
    },
    "Sur": {
        "T1": 9000,
        "T2": 11000,
        "T3": 13000,
        "T4": 17000
    }
}

# Calcular ventas totales con items() y sum(values())
ventas_totales = {}

for region, ventas in ventas_por_region.items():
    ventas_totales[region] = sum(ventas.values())

# Encontrar region con max() key=lambda
mejor_region = max(ventas_totales, key=lambda r: ventas_totales[r])

# Inicializar totales_por_trimestre
totales_por_trimestre = {
    "T1": 0,
    "T2": 0,
    "T3": 0,
    "T4": 0
}

# Acumular con iteracion anidada
for region, ventas in ventas_por_region.items():
    for trimestre, valor in ventas.items():
        totales_por_trimestre[trimestre] += valor

# Calcular gran_total
gran_total = sum(ventas_totales.values())

# Generar porcentajes con dict comprehension
porcentajes = {
    region: (total / gran_total) * 100
    for region, total in ventas_totales.items()
}

# Imprimir reporte ordenado
print("=== REPORTE DE VENTAS ===\n")

print("Ventas por región:")
for region, total in ventas_totales.items():
    print(f"{region}: ${total}")

print(f"\nRegión con mayores ventas: {mejor_region}")

print("\nTotales por trimestre:")
for trimestre, total in totales_por_trimestre.items():
    print(f"{trimestre}: ${total}")

print(f"\nGran Total: ${gran_total}")

print("\nPorcentaje por región:")
for region, porcentaje in porcentajes.items():
    print(f"{region}: {porcentaje:.2f}%")