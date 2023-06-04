import os


class Settings:
    def __init__(self) -> None:
        self.HOST = os.getenv("HOST")
        self.PORT = os.getenv("PORT")
        self.USER = os.getenv("USER")
        self.PASS = os.getenv("PASS")
        self.SCHEMA = os.getenv("SCHEMA")

    def serialize(self) -> dict:
        return {
            "HOST": self.HOST,
            "PORT": self.PORT,
            "USER": self.USER,
            "PASS": self.PASS,
            "SCHEMA": self.SCHEMA,
        }


settings = Settings()
