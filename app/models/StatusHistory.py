import datetime


class StatusHistoryModel:
    def __init__(self, data: dict) -> None:
        """
        Inicializa una instancia de la clase StatusHistoryModel.

        Args:
            data (dict): Un diccionario que contiene los datos del historial de estado.
                Los elementos esperados son: "id" (int), "property_id" (int), "status_id" (int)
                y "update_date" (datetime).
        """
        self.id: int = data["id"]
        self.property_id: int = data["property_id"]
        self.status_id: int = data["status_id"]
        self.update_date: datetime = data["update_date"]

    def serialize(self) -> dict:
        """
        Devuelve un diccionario con el historial de estado serializado.

        Returns:
            dict: Un diccionario que contiene todos los datos del historial de estado.
        """
        return {
            "id": self.id,
            "property_id": self.property_id,
            "status_id": self.status_id,
            "update_date": str(self.update_date),
        }
