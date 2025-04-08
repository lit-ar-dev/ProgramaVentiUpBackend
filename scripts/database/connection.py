import os
from dotenv import load_dotenv
import mariadb

# Cargar el archivo .env
load_dotenv()

# Leer las variables desde el .env
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT", 3306)  # Valor por defecto

class Connection():
    connection = None
    def conectar(self):
        # Conectarse a la base de datos
        try:
            self.connection = mariadb.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                port=int(DB_PORT)
            )
            print("Conexión exitosa a la base de datos")
        except mariadb.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def query(self, sql, params=None):
        # Crear un cursor
        cursor = self.connection.cursor()

        try:
            # Ejecutar la consulta
            if params is not None:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)

            # Guardar los cambios
            self.connection.commit()

            # Retornar los resultados
            return cursor
        except mariadb.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None

    def desconectar(self):
        if 'connection' in locals():
            self.connection.close()