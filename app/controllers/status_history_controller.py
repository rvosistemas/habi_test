from ..models.StatusHistory import StatusHistoryModel
from ..config.database import Database
from ..config.settings import settings


class StatusHistoryController:
    @staticmethod
    def get_status_history() -> list:
        """
        Obtiene una lista de historial de status (status_history) de la propiedades (property) y el status (status)  desde la base de datos.

        Returns:
            list: Una lista de historial de status (status_history) serializadas.
        """
        db_connection = Database(settings=settings.serialize())
        db_connection.connect()
        cursor = db_connection.connection.cursor()

        query = "SELECT * FROM status_history limit 10"
        cursor.execute(query)

        results_db = cursor.fetchall()
        results_dict = [dict(zip(["id", "property_id", "status_id", "update_date"], row)) for row in results_db]

        serialized_status_history = []
        for row in results_dict:
            status_history_instance = StatusHistoryModel(data=row)
            serialized_status_history.append(status_history_instance.serialize())

        cursor.close()
        db_connection.disconnect()

        return serialized_status_history
