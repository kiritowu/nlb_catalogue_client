import pytest

from nlb_catalogue_client.models.internal_server_error import InternalServerError
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def error_with_status() -> tuple[InternalServerError, dict]:
    return InternalServerError(error="Internal Server Error", message="Internal server error", status_code=500), {
        "error": "Internal Server Error",
        "message": "Internal server error",
        "statusCode": 500,
    }


@pytest.fixture()
def error_without_status() -> tuple[InternalServerError, dict]:
    return InternalServerError(error="Internal Server Error", message="Internal server error"), {
        "error": "Internal Server Error",
        "message": "Internal server error",
    }


class TestInternalServerError:
    @pytest.mark.parametrize(
        "error,message,status_code,expected_status",
        [
            ("Internal Server Error", "Internal server error", 500, 500),
            ("Internal Server Error", "Internal server error", None, None),
            ("Internal Server Error", "Internal server error", UNSET, UNSET),
        ],
    )
    def test_basic_initialization(self, error, message, status_code, expected_status):
        error_obj = InternalServerError(error=error, message=message, status_code=status_code)
        assert error_obj.error == error
        assert error_obj.message == message
        assert error_obj.status_code == expected_status

    def test_to_dict_with_status(self, error_with_status):
        assert error_with_status[0].to_dict() == error_with_status[1]

    def test_to_dict_without_status(self, error_without_status):
        assert error_without_status[0].to_dict() == error_without_status[1]

    def test_from_dict_with_status(self, error_with_status):
        assert InternalServerError.from_dict(error_with_status[1]) == error_with_status[0]

    def test_from_dict_without_status(self, error_without_status):
        assert InternalServerError.from_dict(error_without_status[1]) == error_without_status[0]

    @pytest.mark.parametrize(
        "input_data",
        [
            {"error": "Internal Server Error", "message": "Internal server error", "statusCode": 500},
            {"error": "Internal Server Error", "message": "Internal server error"},
        ],
    )
    def test_dict_roundtrip(self, input_data):
        """Test that to_dict and from_dict are inverse operations"""
        original = InternalServerError.from_dict(input_data)
        dict_form = original.to_dict()
        recreated = InternalServerError.from_dict(dict_form)
        assert original == recreated

    def test_from_dict_preserves_original(self, error_with_status):
        """Test that from_dict doesn't modify the input dictionary"""
        input_dict = error_with_status[1].copy()
        InternalServerError.from_dict(input_dict)
        assert input_dict == error_with_status[1]
