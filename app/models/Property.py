class PropertyModel:
    def __init__(self, data: dict) -> None:
        self.id: int = data["id"]
        self.address: str = data["address"]
        self.city: str = data["city"]
        self.price: int = data["price"]
        self.description: str = data["description"]
        self.year: int = data["year"]

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "address": self.address,
            "city": self.city,
            "price": self.price,
            "description": self.description,
            "year": self.year,
        }
