def conversion_tipos_datos():
    print("=== Conversión entre Tipos de Datos en Python ===\n")

    # 1. Conversión a Entero
    print("1. Conversión a Entero (`int`):")
    print("De flotante a entero:", int(3.9))  # Trunca la parte decimal
    print("De cadena a entero:", int("42"))  # Cadena válida
    print("De booleano a entero:", int(True), int(False))  # True = 1, False = 0
    print()

    # 2. Conversión a Flotante
    print("2. Conversión a Flotante (`float`):")
    print("De entero a flotante:", float(10))  # 10.0
    print("De cadena a flotante:", float("3.14"))  # Cadena válida
    print("De booleano a flotante:", float(True), float(False))  # True = 1.0, False = 0.0
    print()

    # 3. Conversión a Cadena
    print("3. Conversión a Cadena (`str`):")
    print("De entero a cadena:", str(42))  # "42"
    print("De flotante a cadena:", str(3.14))  # "3.14"
    print("De booleano a cadena:", str(True), str(False))  # "True", "False"
    print("De lista a cadena:", str([1, 2, 3]))  # "[1, 2, 3]"
    print()

    # 4. Conversión a Booleano
    print("4. Conversión a Booleano (`bool`):")
    print("De entero a booleano:", bool(0), bool(42))  # 0 = False, cualquier otro número = True
    print("De cadena a booleano:", bool(""), bool("Hola"))  # Cadena vacía = False
    print("De lista a booleano:", bool([]), bool([1, 2]))  # Lista vacía = False
    print()

    # 5. Conversión a Lista
    print("5. Conversión a Lista (`list`):")
    print("De cadena a lista:", list("Hola"))  # ['H', 'o', 'l', 'a']
    print("De tupla a lista:", list((1, 2, 3)))  # [1, 2, 3]
    print("De conjunto a lista:", list({1, 2, 3}))  # [1, 2, 3]
    print()

    # 6. Conversión a Tupla
    print("6. Conversión a Tupla (`tuple`):")
    print("De lista a tupla:", tuple([1, 2, 3]))  # (1, 2, 3)
    print("De cadena a tupla:", tuple("Hola"))  # ('H', 'o', 'l', 'a')
    print()

    # 7. Conversión a Conjunto
    print("7. Conversión a Conjunto (`set`):")
    print("De lista a conjunto:", set([1, 2, 2, 3]))  # {1, 2, 3}
    print("De cadena a conjunto:", set("banana"))  # {'b', 'a', 'n'}
    print()

    # 8. Conversión a Diccionario
    print("8. Conversión a Diccionario (`dict`):")
    print("De lista de tuplas a diccionario:", dict([("a", 1), ("b", 2)]))  # {'a': 1, 'b': 2}
    print("De tupla de tuplas a diccionario:", dict((("x", 10), ("y", 20))))  # {'x': 10, 'y': 20}
    print()

    # Ejemplo general de transformación entre tipos
    print("=== Ejemplo General ===")
    x = "123"         # Cadena inicial
    y = int(x)        # Cadena -> Entero
    z = float(y)      # Entero -> Flotante
    w = str(z)        # Flotante -> Cadena
    print(f"Cadena inicial: {x} ({type(x)})")
    print(f"Cadena a Entero: {y} ({type(y)})")
    print(f"Entero a Flotante: {z} ({type(z)})")
    print(f"Flotante a Cadena: {w} ({type(w)})")

if __name__ == "__main__":
    conversion_tipos_datos()
