"""
obtener la estatura promedio de un grupo de personas cuyo numero
de miembros se desconoce, el ciclo whilw debe efectuarse simple 
y cuando se tenga una estatura registrada 
"""
cont=0
Estatura=0
suma=0
while True:
    cont= 1 + cont 
    Estatura=float(input(f"ingrese la altura {cont} para realizar su promedio"))
    if Estatura>0:
        suma=Estatura+suma
    else:
        print("fin del programa")
        break
print(f"el promedio de las estaturas es {(suma/cont):.2f}")