class PropertyModel:
    def __init__(self, data: dict) -> None:
        """
        Inicializa una instancia de la clase PropertyModel.

        Args:
            data (dict): Un diccionario que contiene los datos de la propiedad.
                Los elementos esperados son: "id" (int), "address" (str), "city" (str),
                "price" (int), "description" (str) y "year" (int).
        """
        self.id: int = data["id"]
        self.address: str = data["address"]
        self.city: str = data["city"]
        self.price: int = data["price"]
        self.description: str = data["description"]
        self.year: int = data["year"]

    def serialize(self) -> dict:
        """
        Devuelve un diccionario con la propiedad serializada.

        Returns:
            dict: Un diccionario que contiene todos los datos de la propiedad.
        """
        return {
            "id": self.id,
            "address": self.address,
            "city": self.city,
            "price": self.price,
            "description": self.description,
            "year": self.year,
        }
