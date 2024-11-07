import pytest

from nlb_catalogue_client.models.method_not_allowed_error import MethodNotAllowedError
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def error_with_status() -> tuple[MethodNotAllowedError, dict]:
    return MethodNotAllowedError(
        error="Method Not Allowed", message="The requested resource does not support http method 'PUT'", status_code=405
    ), {
        "error": "Method Not Allowed",
        "message": "The requested resource does not support http method 'PUT'",
        "statusCode": 405,
    }


@pytest.fixture()
def error_without_status() -> tuple[MethodNotAllowedError, dict]:
    return MethodNotAllowedError(
        error="Method Not Allowed", message="The requested resource does not support http method 'PUT'"
    ), {"error": "Method Not Allowed", "message": "The requested resource does not support http method 'PUT'"}


class TestMethodNotAllowedError:
    @pytest.mark.parametrize(
        "error,message,status_code,expected_status",
        [
            ("Method Not Allowed", "The requested resource does not support http method 'PUT'", 405, 405),
            ("Method Not Allowed", "The requested resource does not support http method 'PUT'", None, None),
            ("Method Not Allowed", "The requested resource does not support http method 'PUT'", UNSET, UNSET),
        ],
    )
    def test_basic_initialization(self, error, message, status_code, expected_status):
        error_obj = MethodNotAllowedError(error=error, message=message, status_code=status_code)
        assert error_obj.error == error
        assert error_obj.message == message
        assert error_obj.status_code == expected_status

    def test_to_dict_with_status(self, error_with_status):
        assert error_with_status[0].to_dict() == error_with_status[1]

    def test_to_dict_without_status(self, error_without_status):
        assert error_without_status[0].to_dict() == error_without_status[1]

    def test_from_dict_with_status(self, error_with_status):
        assert MethodNotAllowedError.from_dict(error_with_status[1]) == error_with_status[0]

    def test_from_dict_without_status(self, error_without_status):
        assert MethodNotAllowedError.from_dict(error_without_status[1]) == error_without_status[0]

    @pytest.mark.parametrize(
        "input_data",
        [
            {
                "error": "Method Not Allowed",
                "message": "The requested resource does not support http method 'PUT'",
                "statusCode": 405,
            },
            {"error": "Method Not Allowed", "message": "The requested resource does not support http method 'PUT'"},
        ],
    )
    def test_dict_roundtrip(self, input_data):
        """Test that to_dict and from_dict are inverse operations"""
        original = MethodNotAllowedError.from_dict(input_data)
        dict_form = original.to_dict()
        recreated = MethodNotAllowedError.from_dict(dict_form)
        assert original == recreated

    def test_from_dict_preserves_original(self, error_with_status):
        """Test that from_dict doesn't modify the input dictionary"""
        input_dict = error_with_status[1].copy()
        MethodNotAllowedError.from_dict(input_dict)
        assert input_dict == error_with_status[1]
