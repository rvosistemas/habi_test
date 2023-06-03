class Status:
    def __init__(self, id, name, label) -> None:
        self.id: int = id
        self.name: str = name
        self.label: str = label

    def __repr__(self) -> str:
        return f"<Status {self.name}>"

    def serialize(self) -> dict:
        return {"id": self.id, "name": self.name, "label": self.label}
