import pytest

from nlb_catalogue_client.models.service_unavailable_error import ServiceUnavailableError
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def error_with_status() -> tuple[ServiceUnavailableError, dict]:
    return ServiceUnavailableError(error="Service unavailable", message="Service unavailable", status_code=503), {
        "error": "Service unavailable",
        "message": "Service unavailable",
        "statusCode": 503,
    }


@pytest.fixture()
def error_without_status() -> tuple[ServiceUnavailableError, dict]:
    return ServiceUnavailableError(error="Service unavailable", message="Service unavailable"), {
        "error": "Service unavailable",
        "message": "Service unavailable",
    }


class TestServiceUnavailableError:
    @pytest.mark.parametrize(
        "error,message,status_code,expected_status",
        [
            ("Service unavailable", "Service unavailable", 503, 503),
            ("Service unavailable", "Service unavailable", None, None),
            ("Service unavailable", "Service unavailable", UNSET, UNSET),
        ],
    )
    def test_basic_initialization(self, error, message, status_code, expected_status):
        error_obj = ServiceUnavailableError(error=error, message=message, status_code=status_code)
        assert error_obj.error == error
        assert error_obj.message == message
        assert error_obj.status_code == expected_status

    def test_to_dict_with_status(self, error_with_status):
        assert error_with_status[0].to_dict() == error_with_status[1]

    def test_to_dict_without_status(self, error_without_status):
        assert error_without_status[0].to_dict() == error_without_status[1]

    def test_from_dict_with_status(self, error_with_status):
        assert ServiceUnavailableError.from_dict(error_with_status[1]) == error_with_status[0]

    def test_from_dict_without_status(self, error_without_status):
        assert ServiceUnavailableError.from_dict(error_without_status[1]) == error_without_status[0]
