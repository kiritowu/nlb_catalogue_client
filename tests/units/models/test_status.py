from datetime import date

from nlb_catalogue_client.models.status import Status
from nlb_catalogue_client.types import UNSET


class TestStatus:
    def test_basic_initialization(self):
        status = Status(name="In Transit", code="I", set_date=date(2019, 7, 21))
        assert status.name == "In Transit"
        assert status.code == "I"
        assert status.set_date == date(2019, 7, 21)

    def test_initialization_with_required_only(self):
        status = Status(name="In Transit")
        assert status.name == "In Transit"
        assert status.code is UNSET
        assert status.set_date is UNSET

    def test_with_none_values(self):
        status = Status(name="In Transit", code=None, set_date=None)
        assert status.name == "In Transit"
        assert status.code is None
        assert status.set_date is None

    def test_to_dict_full(self):
        status = Status(name="In Transit", code="I", set_date=date(2019, 7, 21))
        expected = {"name": "In Transit", "code": "I", "setDate": "2019-07-21"}
        assert status.to_dict() == expected

    def test_to_dict_required_only(self):
        status = Status(name="In Transit")
        expected = {"name": "In Transit"}
        assert status.to_dict() == expected

    def test_to_dict_with_none(self):
        status = Status(name="In Transit", code=None, set_date=None)
        expected = {"name": "In Transit", "code": None, "setDate": None}
        assert status.to_dict() == expected

    def test_from_dict_full(self):
        data = {"name": "In Transit", "code": "I", "setDate": "2019-07-21"}
        status = Status.from_dict(data)
        assert status.name == "In Transit"
        assert status.code == "I"
        assert status.set_date == date(2019, 7, 21)

    def test_from_dict_required_only(self):
        data = {"name": "In Transit"}
        status = Status.from_dict(data)
        assert status.name == "In Transit"
        assert status.code is UNSET
        assert status.set_date is UNSET

    def test_from_dict_with_none(self):
        data = {"name": "In Transit", "code": None, "setDate": None}
        status = Status.from_dict(data)
        assert status.name == "In Transit"
        assert status.code is None
        assert status.set_date is None

    def test_from_dict_with_unset(self):
        data = {"name": "In Transit", "code": UNSET, "setDate": UNSET}
        status = Status.from_dict(data)
        assert status.name == "In Transit"
        assert status.code is UNSET
        assert status.set_date is UNSET

    def test_from_dict_with_invalid_set_date(self):
        data = {
            "name": "In Transit",
            "code": "I",
            "setDate": 0,  # Invalid date format
        }
        status = Status.from_dict(data)
        assert status.name == "In Transit"
        assert status.code == "I"
        assert status.set_date == 0  # Should return the original invalid value
