import pytest
import datetime

from ...app.controllers.search_controller import SearchController


@pytest.mark.usefixtures("db_connection")
def test_get_search():
    filters = {
        "property_filters": {
            "address": "calle 23 #45-67",
            "city": "bogota",
            "price_min": 100000000,
            "price_max": 300000000,
            "year": 2000,
        },
        "status_history_filters": {"update_date": "2021-04-10"},
        "status_filter": {"name": "comprando", "label": "Imueble en proceso de compra"},
    }
    controller = SearchController()
    data_result = controller.get_search(
        property_filters=filters["property_filters"],
        status_history_filters=filters["status_history_filters"],
        status_filter=filters["status_filter"],
    )

    assert len(data_result) == 1
    assert data_result[0]["id_property"] == 1
    assert data_result[0]["address"] == "calle 23 #45-67"
    assert data_result[0]["city"] == "bogota"
    assert data_result[0]["year"] == 2000
    assert data_result[0]["status_label"] == "Imueble en proceso de compra"
    assert data_result[0]["update_date"] == datetime.datetime(2021, 4, 10, 22, 23, 56)
