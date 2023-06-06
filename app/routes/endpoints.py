from fastapi import HTTPException, Depends, APIRouter, Body

from app.controllers.property_controller import PropertyController
from app.controllers.status_controller import StatusController
from app.controllers.status_history_controller import StatusHistoryController
from app.controllers.search_controller import SearchController

from app.utils.SearchRequest_example import example_search_request_filters

router = APIRouter()


@router.get("/properties")
async def get_properties():
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
