import mysql.connector


class Database:
    """
    Inicializa una instancia de la clase Database.

    Args:
        settings (dict): Un diccionario que contiene los datos de configuración de la base de datos.
            Los elementos esperados son: "DB_HOST" (str), "DB_PORT" (int), "DB_USER" (str),
            "DB_PASS" (str) y "DB_SCHEMA" (str).
    """

    def __init__(self, settings: dict) -> None:
        self.host = settings["DB_HOST"]
        self.port = settings["DB_PORT"]
        self.user = settings["DB_USER"]
        self.password = settings["DB_PASS"]
        self.schema = settings["DB_SCHEMA"]
        self.connection = None

    def connect(self):
        """
        Establece una conexión con la base de datos MySQL.

        Prints:
            Mensaje indicando que se ha establecido la conexión a la base de datos, en caso de éxito.

        Raises:
            mysql.connector.Error: Si ocurre algún error al intentar conectarse a la base de datos.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host, port=self.port, user=self.user, passwd=self.password, database=self.schema
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except mysql.connector.Error as error:
            print(f"Failed to connect to MySQL database: {error}")

    def disconnect(self):
        """
        Cierra la conexión a la base de datos MySQL.

        Prints:
            Mensaje indicando que se ha cerrado la conexión a la base de datos.
        """
        if self.connection.is_connected():
            self.connection.close()
            print("Connection to MySQL database closed")
