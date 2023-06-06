import mysql.connector


class Database:
    def __init__(self, settings: dict) -> None:
        self.host = settings["DB_HOST"]
        self.port = settings["DB_PORT"]
        self.user = settings["DB_USER"]
        self.password = settings["DB_PASS"]
        self.schema = settings["DB_SCHEMA"]
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host, port=self.port, user=self.user, passwd=self.password, database=self.schema
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except mysql.connector.Error as error:
            print(f"Failed to connect to MySQL database: {error}")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connection to MySQL database closed")
