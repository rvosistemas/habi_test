import pytest

from ...app.controllers.status_history_controller import StatusHistoryController


@pytest.mark.usefixtures("db_connection")
def test_status_history():
    controller = StatusHistoryController()
    status_history_list = controller.get_status_history()

    assert len(status_history_list) == 10
    assert status_history_list[0]["id"] == 1
    assert status_history_list[0]["update_date"] == "2021-04-10 22:23:56"
    assert status_history_list[1]["id"] == 2
    assert status_history_list[1]["update_date"] == "2021-04-11 22:23:56"
    assert status_history_list[9]["id"] == 10
    assert status_history_list[9]["update_date"] == "2021-04-12 22:26:54"
