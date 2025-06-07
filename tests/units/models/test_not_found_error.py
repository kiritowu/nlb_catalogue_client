import pytest

from nlb_catalogue_client.models.not_found_error import NotFoundError
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def error_with_status() -> tuple[NotFoundError, dict]:
    return NotFoundError(error="Not Found", message="Record(s) not found", status_code=404), {
        "error": "Not Found",
        "message": "Record(s) not found",
        "statusCode": 404,
    }


@pytest.fixture()
def error_without_status() -> tuple[NotFoundError, dict]:
    return NotFoundError(error="Not Found", message="Record(s) not found"), {
        "error": "Not Found",
        "message": "Record(s) not found",
    }


class TestNotFoundError:
    @pytest.mark.parametrize(
        "error,message,status_code,expected_status",
        [
            ("Not Found", "Record(s) not found", 404, 404),
            ("Not Found", "Record(s) not found", None, None),
            ("Not Found", "Record(s) not found", UNSET, UNSET),
        ],
    )
    def test_basic_initialization(self, error, message, status_code, expected_status):
        error_obj = NotFoundError(error=error, message=message, status_code=status_code)
        assert error_obj.error == error
        assert error_obj.message == message
        assert error_obj.status_code == expected_status

    def test_to_dict_with_status(self, error_with_status):
        assert error_with_status[0].to_dict() == error_with_status[1]

    def test_to_dict_without_status(self, error_without_status):
        assert error_without_status[0].to_dict() == error_without_status[1]

    def test_from_dict_with_status(self, error_with_status):
        assert NotFoundError.from_dict(error_with_status[1]) == error_with_status[0]

    def test_from_dict_without_status(self, error_without_status):
        assert NotFoundError.from_dict(error_without_status[1]) == error_without_status[0]

    @pytest.mark.parametrize(
        "input_data",
        [
            {"error": "Not Found", "message": "Record(s) not found", "statusCode": 404},
            {"error": "Not Found", "message": "Record(s) not found"},
        ],
    )
    def test_dict_roundtrip(self, input_data):
        """Test that to_dict and from_dict are inverse operations"""
        original = NotFoundError.from_dict(input_data)
        dict_form = original.to_dict()
        recreated = NotFoundError.from_dict(dict_form)
        assert original == recreated

    def test_from_dict_preserves_original(self, error_with_status):
        """Test that from_dict doesn't modify the input dictionary"""
        input_dict = error_with_status[1].copy()
        NotFoundError.from_dict(input_dict)
        assert input_dict == error_with_status[1]
