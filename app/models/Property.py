class Propierty:
    def __init__(self, id, address, city, price, description, year) -> None:
        self.id: int = id
        self.address: str = address
        self.city: str = city
        self.price: int = price
        self.description: str = description
        self.year: int = year

    def __repr__(self) -> str:
        return f"<Propierty {self.description if self.description else 'without Description'}>"
    
    def serialize(self) -> dict:
        return {
            'id': self.id,
            'address': self.address,
            'city': self.city,
            'price': self.price,
            'description': self.description,
            'year': self.year
        }