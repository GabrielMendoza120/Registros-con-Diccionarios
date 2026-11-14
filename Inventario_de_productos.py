inventario = {
    "P01": {"nombre": "Laptop", "precio": 15000, "stock": 4},
    "P02": {"nombre": "Mouse", "precio": 300, "stock": 10},
    "P03": {"nombre": "Teclado", "precio": 800, "stock": 2},
    "P04": {"nombre": "Monitor", "precio": 3500, "stock": 6}
}

valor_total = 0
mas_caro = ""
precio_mayor = 0
mas_barato = ""
precio_menor = 999999999

print("--- PRODUCTOS CON STOCK BAJO (< 5) ---")
for codigo in inventario:
    producto = inventario[codigo]
    nombre = producto["nombre"]
    precio = producto["precio"]
    stock = producto["stock"]

    # 1. Sumar al valor total
    valor_total = valor_total + (precio * stock)

    # 2. Revisar si es el más caro o el más barato
    if precio > precio_mayor:
        precio_mayor = precio
        mas_caro = nombre

    if precio < precio_menor:
        precio_menor = precio
        mas_barato = nombre

    # 3. Revisar si tiene stock bajo
    if stock < 5:
        print(codigo, "-", nombre, "(Stock:", stock, ")")

print("\n--- RESUMEN DEL INVENTARIO ---")
print("Valor total del inventario: $", valor_total)
print("Producto más caro:", mas_caro, "($", precio_mayor, ")")
print("Producto más barato:", mas_barato, "($", precio_menor, ")")
