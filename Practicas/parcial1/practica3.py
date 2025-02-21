print("seleccione")
print("1)pizza")
print("2)hamburguesa")
print("3)ensalada")
opc = input()
while True:
    match opc:
        case 1:
            print("Pizza..... 10")
        case 2:
            print("hambuergeza.....8")
        case 3:
            print("ensalada..... 6")
        case _:
            print("no existe esa opcion")
    