# Declaración de variables
continuar = "si"
valor_total_inventario = 0

# Estructura repetitiva para ingresar varios productos
while continuar == "si":
    # Entrada de datos
    nombre = input("Ingresa el nombre del producto: ")

    # Validación del precio
    while True:
        precio = float(input("Ingresa el precio del producto: "))
        if precio > 0:
            break
        print("Precio no válido. Por favor, ingresa un precio mayor que 0.")

    cantidad = int(input("Ingresa la cantidad en inventario: "))

    # Determinación del estado del inventario
    if cantidad == 0:
        estado = "Agotado"
    elif 1 <= cantidad <= 20:
        estado = "Bajo stock"
    else:
        estado = "Stock suficiente"

    # Cálculo del valor total del inventario del producto
    valor_total_producto = precio * cantidad

    # Manejo de descuentos
    if valor_total_producto > 50:
        descuento = valor_total_producto * 0.1
        valor_total_producto -= descuento
        print(f"Descuento aplicado: ${descuento:.2f}")

    # Acumulación del valor total del inventario
    valor_total_inventario += valor_total_producto

    # Salida de datos del producto
    print("Resumen del producto:")
    print(f"Nombre del producto: {nombre}")
    print(f"Precio: ${precio:.2f}")
    print(f"Cantidad en inventario: {cantidad}")
    print(f"Estado del producto: {estado}")
    print(f"Valor total del inventario del producto: ${valor_total_producto:.2f}")

    # Pregunta al usuario si desea continuar ingresando productos
    continuar = input("¿Deseas ingresar otro producto? (si/no): ").lower()

# Salida del valor total combinado del inventario
print(f"Valor total combinado del inventario: ${valor_total_inventario:.2f}")
