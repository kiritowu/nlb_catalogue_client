import pytest

from nlb_catalogue_client.models.too_many_requests_error import TooManyRequestsError
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def error_with_status() -> tuple[TooManyRequestsError, dict]:
    return TooManyRequestsError(error="Too Many Requests", message="API calls quota exceeded", status_code=429), {
        "error": "Too Many Requests",
        "message": "API calls quota exceeded",
        "statusCode": 429,
    }


@pytest.fixture()
def error_without_status() -> tuple[TooManyRequestsError, dict]:
    return TooManyRequestsError(error="Too Many Requests", message="API calls quota exceeded"), {
        "error": "Too Many Requests",
        "message": "API calls quota exceeded",
    }


class TestTooManyRequestsError:
    @pytest.mark.parametrize(
        "error,message,status_code,expected_status",
        [
            ("Too Many Requests", "API calls quota exceeded", 429, 429),
            ("Too Many Requests", "API calls quota exceeded", None, None),
            ("Too Many Requests", "API calls quota exceeded", UNSET, UNSET),
        ],
    )
    def test_basic_initialization(self, error, message, status_code, expected_status):
        error_obj = TooManyRequestsError(error=error, message=message, status_code=status_code)
        assert error_obj.error == error
        assert error_obj.message == message
        assert error_obj.status_code == expected_status

    def test_to_dict_with_status(self, error_with_status):
        assert error_with_status[0].to_dict() == error_with_status[1]

    def test_to_dict_without_status(self, error_without_status):
        assert error_without_status[0].to_dict() == error_without_status[1]

    def test_from_dict_with_status(self, error_with_status):
        assert TooManyRequestsError.from_dict(error_with_status[1]) == error_with_status[0]

    def test_from_dict_without_status(self, error_without_status):
        assert TooManyRequestsError.from_dict(error_without_status[1]) == error_without_status[0]

    @pytest.mark.parametrize(
        "input_data",
        [
            {"error": "Too Many Requests", "message": "API calls quota exceeded", "statusCode": 429},
            {"error": "Too Many Requests", "message": "API calls quota exceeded"},
        ],
    )
    def test_dict_roundtrip(self, input_data):
        """Test that to_dict and from_dict are inverse operations"""
        original = TooManyRequestsError.from_dict(input_data)
        dict_form = original.to_dict()
        recreated = TooManyRequestsError.from_dict(dict_form)
        assert original == recreated

    def test_from_dict_preserves_original(self, error_with_status):
        """Test that from_dict doesn't modify the input dictionary"""
        input_dict = error_with_status[1].copy()
        TooManyRequestsError.from_dict(input_dict)
        assert input_dict == error_with_status[1]
