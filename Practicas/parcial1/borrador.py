import sqlite3 


# Conectar a la base de datos
conn = sqlite3.connect('mi_basededatos.db')

# Crear un cursor para realizar operaciones
cursor = conn.cursor()

# Ejecutar una consulta de ejemplo
cursor.execute('SELECT * FROM mi_tabla')

# Recuperar los resultados
filas = cursor.fetchall()

# Cerrar la conexión
conn.close()

