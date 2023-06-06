import pytest
from ...app.config.database import Database
from ...app.config.settings import settings


@pytest.fixture(scope="session")
def db_connection():
    db = Database(settings=settings.serialize())
    db.connect()
    yield db
    db.disconnect()
