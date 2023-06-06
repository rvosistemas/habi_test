import pytest

from ...app.config.database import Database
from ...app.config.settings import settings


# Fixture para establecer y cerrar la conexión a la base de datos en cada prueba
@pytest.fixture
def database():
    settings_test = {
        "DB_HOST": settings.DB_HOST,
        "DB_PORT": settings.DB_PORT,
        "DB_USER": settings.DB_USER,
        "DB_PASS": settings.DB_PASS,
        "DB_SCHEMA": settings.DB_SCHEMA,
    }
    db = Database(settings_test)
    db.connect()
    yield db
    db.disconnect()


# Prueba para verificar que la conexión a la base de datos se establece correctamente
def test_connect(database):
    assert database.connection.is_connected()


def test_database_connect_failure():
    settings_fail_test = {
        "DB_HOST": settings.DB_HOST,
        "DB_PORT": settings.DB_PORT,
        "DB_USER": settings.DB_USER,
        "DB_PASS": settings.DB_PASS,
        "DB_SCHEMA": "non-existent-database",
    }
    db = Database(settings_fail_test)
    assert db.connect() is None


# Prueba para verificar que la conexión a la base de datos se cierra correctamente
def test_disconnect(database):
    database.disconnect()
    assert not database.connection.is_connected()
