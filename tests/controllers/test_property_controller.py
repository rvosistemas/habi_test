import pytest

from ...app.controllers.property_controller import PropertyController


@pytest.mark.usefixtures("db_connection")
def test_get_properties():
    controller = PropertyController()
    properties = controller.get_properties()

    assert len(properties) == 10
    assert properties[0]["id"] == 1
    assert properties[0]["address"] == "calle 23 #45-67"
    assert properties[1]["id"] == 2
    assert properties[1]["address"] == "carrera 100 #15-90"
    assert properties[9]["id"] == 10
    assert properties[9]["address"] == "calle 95 # 78 - 49"
