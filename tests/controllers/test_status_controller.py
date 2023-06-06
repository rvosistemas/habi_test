import pytest

from ...app.controllers.status_controller import StatusController


@pytest.mark.usefixtures("db_connection")
def test_get_status():
    controller = StatusController()
    status_list = controller.get_status()

    assert len(status_list) == 6
    assert status_list[0]["id"] == 1
    assert status_list[0]["name"] == "comprando"
    assert status_list[1]["id"] == 2
    assert status_list[1]["name"] == "comprado"
    assert status_list[5]["id"] == 6
    assert status_list[5]["name"] == ""
