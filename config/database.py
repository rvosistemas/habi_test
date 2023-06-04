import _mysql_connector


class Database:
    def __init__(self, settings: dict) -> None:
        self.host = settings["HOST"]
        self.port = settings["PORT"]
        self.user = settings["USER"]
        self.password = settings["PASS"]
        self.schema = settings["SCHEMA"]
        self.connection = None

    def connect(self):
        try:
            self.connection = _mysql_connector.connect(
                host=self.HOST, port=self.PORT, user=self.USER, passwd=self.PASS, database=self.SCHEMA
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except _mysql_connector.Error as error:
            print(f"Failed to connect to MySQL database: {error}")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connection to MySQL database closed")
