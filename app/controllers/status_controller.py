from ..models.Status import StatusModel
from ..config.database import Database
from ..config.settings import settings


class StatusController:
    @staticmethod
    def get_status() -> list:
        """
        Obtiene una lista de status (status) de la propiedades (property)  desde la base de datos.

        Returns:
            list: Una lista de status (status) serializadas.
        """
        db_connection = Database(settings=settings.serialize())
        db_connection.connect()
        cursor = db_connection.connection.cursor()

        query = "SELECT * FROM status limit 10"
        cursor.execute(query)

        results_db = cursor.fetchall()
        results_dict = [dict(zip(["id", "name", "label", "price"], row)) for row in results_db]

        serialized_status = []
        for row in results_dict:
            status_instance = StatusModel(data=row)
            serialized_status.append(status_instance.serialize())

        cursor.close()
        db_connection.disconnect()

        return serialized_status
