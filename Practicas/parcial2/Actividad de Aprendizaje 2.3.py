# Variables globales
ganancias = 0
gastos = 0

def menu():
    print("--Menú de Opciones--")
    print("1) Iniciar un viaje")
    print("2) Registrar combustible")
    print("3) Finalizar jornada")
    print("0) Salir")
    opcion = int(input("Elige una opción: "))
    return opcion

def iniciar_viaje():
    global ganancias
    destino = input("Introduce el destino del viaje: ")
    distancia = float(input("Introduce la distancia en kilómetros: "))
    tarifa_por_km = float(input("Introduce la tarifa por kilómetro: "))
    costo_viaje = distancia * tarifa_por_km
    ganancias += costo_viaje
    print(f"El costo del viaje a {destino} es de {costo_viaje:.2f} unidades.")
    saldo = ganancias - gastos
    print(f"El saldo es de {saldo:.2f} unidades.")
    

def registrar_combustible():
    global gastos
    litros = float(input("Introduce la cantidad de litros: "))
    precio_por_litro = float(input("Introduce el precio por litro: "))
    costo_combustible = litros * precio_por_litro
    gastos += costo_combustible
    print(f"El costo total del combustible es de {costo_combustible:.2f} unidades.")
    saldo = ganancias - gastos
    print(f"El saldo es de {saldo:.2f} unidades.")

def finalizar_jornada():
    saldo_final = ganancias - gastos
    print("=== Resumen de la Jornada ===")
    print(f"Ganancias: {ganancias:.2f} unidades")
    print(f"Gastos: {gastos:.2f} unidades")
    print(f"Saldo final acumulado: {saldo_final:.2f} unidades")

def main():
    while True:
        opcion = menu()
        match opcion:
            case 1:
                iniciar_viaje()
            case 2:
                registrar_combustible()
            case 3:
                finalizar_jornada()
            case 0:
                print("gracias por su coperación y registro")
                break
            case _:
                print("Opción incorrecta. Por favor, elige una opción válida.")

main()
