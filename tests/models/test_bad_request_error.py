import pytest

from nlb_catalogue_client.models.bad_request_error import BadRequestError
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def error_with_status() -> tuple[BadRequestError, dict]:
    return BadRequestError(error="Bad Request", message="Field is missing", status_code=400), {
        "error": "Bad Request",
        "message": "Field is missing",
        "statusCode": 400,
    }


@pytest.fixture()
def error_without_status() -> tuple[BadRequestError, dict]:
    return BadRequestError(error="Bad Request", message="Field is missing"), {
        "error": "Bad Request",
        "message": "Field is missing",
    }


class TestBadRequestError:
    @pytest.mark.parametrize(
        "error,message,status_code,expected_status",
        [
            ("Bad Request", "Field is missing", 400, 400),
            ("Bad Request", "Field is missing", None, None),
            ("Bad Request", "Field is missing", UNSET, UNSET),
        ],
    )
    def test_basic_initialization(self, error, message, status_code, expected_status):
        error_obj = BadRequestError(error=error, message=message, status_code=status_code)
        assert error_obj.error == error
        assert error_obj.message == message
        assert error_obj.status_code == expected_status

    def test_to_dict_with_status(self, error_with_status):
        assert error_with_status[0].to_dict() == error_with_status[1]

    def test_to_dict_without_status(self, error_without_status):
        assert error_without_status[0].to_dict() == error_without_status[1]

    def test_from_dict_with_status(self, error_with_status):
        assert BadRequestError.from_dict(error_with_status[1]) == error_with_status[0]

    def test_from_dict_without_status(self, error_without_status):
        assert BadRequestError.from_dict(error_without_status[1]) == error_without_status[0]

    @pytest.mark.parametrize(
        "input_data",
        [
            {"error": "Bad Request", "message": "Field is missing", "statusCode": 400},
            {"error": "Bad Request", "message": "Field is missing"},
        ],
    )
    def test_dict_roundtrip(self, input_data):
        """Test that to_dict and from_dict are inverse operations"""
        original = BadRequestError.from_dict(input_data)
        dict_form = original.to_dict()
        recreated = BadRequestError.from_dict(dict_form)
        assert original == recreated

    def test_from_dict_preserves_original(self, error_with_status):
        """Test that from_dict doesn't modify the input dictionary"""
        input_dict = error_with_status[1].copy()
        BadRequestError.from_dict(input_dict)
        assert input_dict == error_with_status[1]
