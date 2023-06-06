import datetime


class StatusHistoryModel:
    def __init__(self, data: dict) -> None:
        self.id: int = data["id"]
        self.property_id: int = data["property_id"]
        self.status_id: int = data["status_id"]
        self.update_date: datetime = data["update_date"]

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "property_id": self.property_id,
            "status_id": self.status_id,
            "update_date": str(self.update_date),
        }
