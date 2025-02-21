import sys

def consultar_tipos_datos():
    print("Consulta general de tipos de datos en Python:\n")

    # Entero
    entero = 42
    print("Entero:")
    print("  Valor:", entero)
    print("  Tamaño en memoria:", sys.getsizeof(entero), "bytes")
    print()

    # Flotante
    flotante = 3.14159
    print("Flotante:")
    print("  Valor:", flotante)
    print("  Tamaño en memoria:", sys.getsizeof(flotante), "bytes")
    print("  Rango de flotante:")
    print("    Mínimo positivo:", sys.float_info.min)
    print("    Máximo:", sys.float_info.max)
    print("    Precisión:", sys.float_info.dig, "dígitos")
    print()

    # Cadena de texto
    cadena = "Hola, mundo"
    print("Cadena de texto:")
    print("  Valor:", cadena)
    print("  Tamaño en memoria:", sys.getsizeof(cadena), "bytes")
    print("  Longitud de la cadena:", len(cadena))
    print()

    # Booleano
    booleano = True
    print("Booleano:")
    print("  Valor:", booleano)
    print("  Tamaño en memoria:", sys.getsizeof(booleano), "bytes")
    print()

    # Lista
    lista = [1, 2, 3, 4, 5]
    print("Lista:")
    print("  Valor:", lista)
    print("  Tamaño en memoria:", sys.getsizeof(lista), "bytes")
    print("  Longitud de la lista:", len(lista))
    print()

    # Diccionario
    diccionario = {"clave1": "valor1", "clave2": "valor2"}
    print("Diccionario:")
    print("  Valor:", diccionario)
    print("  Tamaño en memoria:", sys.getsizeof(diccionario), "bytes")
    print("  Número de elementos:", len(diccionario))
    print()

    # Número complejo
    complejo = 3 + 4j
    print("Número complejo:")
    print("  Valor:", complejo)
    print("  Tamaño en memoria:", sys.getsizeof(complejo), "bytes")
    print()

if __name__ == "__main__":
    consultar_tipos_datos()