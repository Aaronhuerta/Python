#debemos realizar una calculadora basica de suma, resta y multiplicacion, cada uno empleando una funcion 
def suma ():
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    print("La suma de los dos numeros es: ", num1 + num2)

def resta ():
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    print("La Resta de los dos numeros es: ", num1 - num2)

def multiplicacion():
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    print("La multiplicacion de los dos numeros es: ", num1 * num2)

def dicicion():
    num1 = float(input("Ingrese el divisor: "))
    num2 = float(input("Ingrese el denominador: "))
    if num2!= 0:
        print("La divicion de los dos numeros es: ", num1 / num2)
    else:
        print("Error: División por cero no permitida")

def menu():
    print("Calculadora Basica")
    print("1)Suma")
    print("2)Resta")
    print("3)Multiplicacion")
    print("4)Divicion")
    print("5)Salir")

while True:
    menu()
    opc=  int(input())
    match opc :
        case 1:
            suma()
        case 2:
            resta()
        case 3:
            multiplicacion()
        case 4:
            dicicion()
        case 5:
            print("gracias por usar nuestra calculadora")
            break
        case _:
            print("Opcion invalida, por favor vuelva a intentarlo")
print("")