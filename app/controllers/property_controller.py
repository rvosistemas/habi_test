from ..models.Property import PropertyModel
from ..config.database import Database
from ..config.settings import settings


class PropertyController:
    @staticmethod
    def get_properties() -> list:
        db_connection = Database(settings=settings.serialize())
        db_connection.connect()
        cursor = db_connection.connection.cursor()

        query = "SELECT * FROM property limit 10"
        cursor.execute(query)

        results_db = cursor.fetchall()
        results_dict = [
            dict(zip(["id", "address", "city", "price", "description", "year"], row)) for row in results_db
        ]

        serialized_properties = []
        for row in results_dict:
            property_instance = PropertyModel(data=row)
            serialized_properties.append(property_instance.serialize())

        cursor.close()
        db_connection.disconnect()

        return serialized_properties
