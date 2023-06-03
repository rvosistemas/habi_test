import datetime


class StatusHistory:
    def __init__(self, id, property_id, status_id, update_date):
        self.id: int = id
        self.property_id: int = property_id
        self.status_id: int = status_id
        self.update_date: datetime = update_date

    def __repr__(self):
        f"{self.status_id} {self.update_date}"

    def serialize(self):
        return {
            "id": self.id,
            "property_id": self.property_id,
            "status_id": self.status_id,
            "update_date": self.update_date,
        }
