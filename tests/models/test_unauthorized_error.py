import pytest

from nlb_catalogue_client.models.unauthorized_error import UnauthorizedError
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def error_with_status() -> tuple[UnauthorizedError, dict]:
    return UnauthorizedError(error="Unauthorized", message="Invalid API Key", status_code=401), {
        "error": "Unauthorized",
        "message": "Invalid API Key",
        "statusCode": 401,
    }


@pytest.fixture()
def error_without_status() -> tuple[UnauthorizedError, dict]:
    return UnauthorizedError(error="Unauthorized", message="Invalid API Key"), {
        "error": "Unauthorized",
        "message": "Invalid API Key",
    }


class TestUnauthorizedError:
    @pytest.mark.parametrize(
        "error,message,status_code,expected_status",
        [
            ("Unauthorized", "Invalid API Key", 401, 401),
            ("Unauthorized", "Invalid API Key", None, None),
            ("Unauthorized", "Invalid API Key", UNSET, UNSET),
        ],
    )
    def test_basic_initialization(self, error, message, status_code, expected_status):
        error_obj = UnauthorizedError(error=error, message=message, status_code=status_code)
        assert error_obj.error == error
        assert error_obj.message == message
        assert error_obj.status_code == expected_status

    def test_to_dict_with_status(self, error_with_status):
        assert error_with_status[0].to_dict() == error_with_status[1]

    def test_to_dict_without_status(self, error_without_status):
        assert error_without_status[0].to_dict() == error_without_status[1]

    def test_from_dict_with_status(self, error_with_status):
        assert UnauthorizedError.from_dict(error_with_status[1]) == error_with_status[0]

    def test_from_dict_without_status(self, error_without_status):
        assert UnauthorizedError.from_dict(error_without_status[1]) == error_without_status[0]

    @pytest.mark.parametrize(
        "input_data",
        [
            {"error": "Unauthorized", "message": "Invalid API Key", "statusCode": 401},
            {"error": "Unauthorized", "message": "Invalid API Key"},
        ],
    )
    def test_dict_roundtrip(self, input_data):
        """Test that to_dict and from_dict are inverse operations"""
        original = UnauthorizedError.from_dict(input_data)
        dict_form = original.to_dict()
        recreated = UnauthorizedError.from_dict(dict_form)
        assert original == recreated

    def test_from_dict_preserves_original(self, error_with_status):
        """Test that from_dict doesn't modify the input dictionary"""
        input_dict = error_with_status[1].copy()
        UnauthorizedError.from_dict(input_dict)
        assert input_dict == error_with_status[1]
