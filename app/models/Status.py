class StatusModel:
    """
    Inicializa una instancia de la clase StatusModel.

    Args:
        data (dict): Un diccionario que contiene los datos del estado.
            Los elementos esperados son: "id" (int), "name" (str) y "label" (str).
    """

    def __init__(self, data: dict) -> None:
        self.id: int = data["id"]
        self.name: str = data["name"]
        self.label: str = data["label"]

    def serialize(self) -> dict:
        """
        Devuelve un diccionario con el estado serializado.

        Returns:
            dict: Un diccionario que contiene todos los datos del estado.
        """
        return {"id": self.id, "name": self.name, "label": self.label}
