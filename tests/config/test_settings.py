import os
from dotenv import load_dotenv
import pytest

load_dotenv()

from ...app.config.settings import Settings


@pytest.fixture
def settings():
    # Configurar el entorno de prueba
    os.environ["DB_HOST"] = "localhost"
    os.environ["DB_PORT"] = "3306"
    os.environ["DB_USER"] = "testuser"
    os.environ["DB_PASS"] = "testpass"
    os.environ["DB_SCHEMA"] = "testdb"
    os.environ["APP_HOST"] = "127.0.0.1"
    os.environ["APP_PORT"] = "8000"

    # Crear una instancia de Settings
    settings = Settings()

    yield settings

    # Limpiar las variables de entorno después de cada prueba
    os.environ.pop("DB_HOST")
    os.environ.pop("DB_PORT")
    os.environ.pop("DB_USER")
    os.environ.pop("DB_PASS")
    os.environ.pop("DB_SCHEMA")
    os.environ.pop("APP_HOST")
    os.environ.pop("APP_PORT")


def test_settings_serialize(settings):
    # Serializar los valores
    serialized_settings = settings.serialize()

    # Verificar los valores serializados
    assert serialized_settings["DB_HOST"] == "localhost"
    assert serialized_settings["DB_PORT"] == "3306"
    assert serialized_settings["DB_USER"] == "testuser"
    assert serialized_settings["DB_PASS"] == "testpass"
    assert serialized_settings["DB_SCHEMA"] == "testdb"
    assert serialized_settings["APP_HOST"] == "127.0.0.1"
    assert serialized_settings["APP_PORT"] == "8000"
