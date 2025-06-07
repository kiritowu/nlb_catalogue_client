import pytest

from nlb_catalogue_client.models.not_implemented_error import NotImplementedError_
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def error_with_status() -> tuple[NotImplementedError_, dict]:
    return NotImplementedError_(error="Not Implemented", message="Not Implemented", status_code=501), {
        "error": "Not Implemented",
        "message": "Not Implemented",
        "statusCode": 501,
    }


@pytest.fixture()
def error_without_status() -> tuple[NotImplementedError_, dict]:
    return NotImplementedError_(error="Not Implemented", message="Not Implemented"), {
        "error": "Not Implemented",
        "message": "Not Implemented",
    }


class TestNotImplementedError:
    @pytest.mark.parametrize(
        "error,message,status_code,expected_status",
        [
            ("Not Implemented", "Not Implemented", 501, 501),
            ("Not Implemented", "Not Implemented", None, None),
            ("Not Implemented", "Not Implemented", UNSET, UNSET),
        ],
    )
    def test_basic_initialization(self, error, message, status_code, expected_status):
        error_obj = NotImplementedError_(error=error, message=message, status_code=status_code)
        assert error_obj.error == error
        assert error_obj.message == message
        assert error_obj.status_code == expected_status

    def test_to_dict_with_status(self, error_with_status):
        assert error_with_status[0].to_dict() == error_with_status[1]

    def test_to_dict_without_status(self, error_without_status):
        assert error_without_status[0].to_dict() == error_without_status[1]

    def test_from_dict_with_status(self, error_with_status):
        assert NotImplementedError_.from_dict(error_with_status[1]) == error_with_status[0]

    def test_from_dict_without_status(self, error_without_status):
        assert NotImplementedError_.from_dict(error_without_status[1]) == error_without_status[0]

    @pytest.mark.parametrize(
        "input_data",
        [
            {"error": "Not Implemented", "message": "Not Implemented", "statusCode": 501},
            {"error": "Not Implemented", "message": "Not Implemented"},
        ],
    )
    def test_dict_roundtrip(self, input_data):
        """Test that to_dict and from_dict are inverse operations"""
        original = NotImplementedError_.from_dict(input_data)
        dict_form = original.to_dict()
        recreated = NotImplementedError_.from_dict(dict_form)
        assert original == recreated

    def test_from_dict_preserves_original(self, error_with_status):
        """Test that from_dict doesn't modify the input dictionary"""
        input_dict = error_with_status[1].copy()
        NotImplementedError_.from_dict(input_dict)
        assert input_dict == error_with_status[1]
