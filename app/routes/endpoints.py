from fastapi import HTTPException, Depends, APIRouter, Body

from ..controllers.property_controller import PropertyController
from ..controllers.status_controller import StatusController
from ..controllers.status_history_controller import StatusHistoryController
from ..controllers.search_controller import SearchController

from ..utils.SearchRequest_example import example_search_request_filters

router = APIRouter()


@router.get("/properties")
async def get_properties():
    """
    Obtiene una lista de propiedades.

    Returns:
        dict: Respuesta con la lista de propiedades recuperadas.
    """
    try:
        property_controller = PropertyController()
        properties = property_controller.get_properties()

        response = {"properties": [], "message": "No data found", "status": 200}
        if properties:
            response = {"properties": properties, "message": "Properties retrieved", "status": 200}
        return response

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/status")
async def get_status():
    """
    Obtiene una lista de estados.

    Returns:
        dict: Respuesta con la lista de estados recuperados.
    """
    try:
        status_controller = StatusController()
        status_list = status_controller.get_status()

        response = {"status_list": [], "message": "No data found", "status": 200}
        if status_list:
            response = {
                "status_list": status_list,
                "message": "Status retrieved",
                "status": 200,
            }
        return response

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/status_history")
async def get_status_history():
    """
    Obtiene una lista de historiales de estado.

    Returns:
        dict: Respuesta con la lista de historiales de estado recuperados.
    """
    try:
        status_history_controller = StatusHistoryController()
        status_histories = status_history_controller.get_status_history()

        response = {"status_histories": [], "message": "No data found", "status": 200}
        if status_histories:
            response = {
                "status_histories": status_histories,
                "message": "Status_histories retrieved",
                "status": 200,
            }
        return response

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/search")
async def search_data(filters: dict = Body(example=example_search_request_filters)):
    """
    Realiza una búsqueda de datos con los filtros especificados.

    Args:
        filters (dict): Filtros de búsqueda.

    Returns:
        dict: Respuesta con los datos de búsqueda recuperados.
    """
    try:
        search_controller = SearchController()

        property_filters = filters.get("property_filters")
        status_history_filters = filters.get("status_history_filters")
        status_filter = filters.get("status_filter")

        result_data = search_controller.get_search(property_filters, status_history_filters, status_filter)

        response = {"data": [], "message": "No data found", "status": 200}
        if result_data:
            response = {"data": result_data, "message": "Data retrieved", "status": 200}
        return response

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
