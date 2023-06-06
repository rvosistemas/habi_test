class StatusModel:
    def __init__(self, data: dict) -> None:
        self.id: int = data["id"]
        self.name: str = data["name"]
        self.label: str = data["label"]

    def serialize(self) -> dict:
        return {"id": self.id, "name": self.name, "label": self.label}
