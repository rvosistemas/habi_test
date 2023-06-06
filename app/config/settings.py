import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    Inicializa una instancia de la clase Settings.

    Lee los valores de configuración desde las variables de entorno y los asigna a los atributos de la clase.
    """

    def __init__(self) -> None:
        # Database
        self.DB_HOST = os.getenv("DB_HOST")
        self.DB_PORT = os.getenv("DB_PORT")
        self.DB_USER = os.getenv("DB_USER")
        self.DB_PASS = os.getenv("DB_PASS")
        self.DB_SCHEMA = os.getenv("DB_SCHEMA")

        # APP
        self.APP_HOST = os.getenv("APP_HOST")
        self.APP_PORT = os.getenv("APP_PORT")

    def serialize(self) -> dict:
        """
        Devuelve un diccionario con la configuración serializada.

        Returns:
            dict: Un diccionario que contiene todos los valores de configuración de la instancia.
        """
        return {
            "DB_HOST": self.DB_HOST,
            "DB_PORT": self.DB_PORT,
            "DB_USER": self.DB_USER,
            "DB_PASS": self.DB_PASS,
            "DB_SCHEMA": self.DB_SCHEMA,
            "APP_HOST": self.APP_HOST,
            "APP_PORT": self.APP_PORT,
        }


settings = Settings()
