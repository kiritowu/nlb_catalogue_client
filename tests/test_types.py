import io
from http import HTTPStatus

import pytest

from nlb_catalogue_client.types import UNSET, File, Response


class TestUnset:
    def test_unset_bool(self):
        """Test that UNSET evaluates to False"""
        assert bool(UNSET) is False
        assert not UNSET

    def test_identity(self):
        """Test that UNSET is UNSET"""
        assert UNSET is UNSET


class TestFile:
    @pytest.fixture
    def sample_binary_data(self):
        return b"Sample file content"

    @pytest.fixture
    def sample_file_obj(self, sample_binary_data):
        return io.BytesIO(sample_binary_data)

    def test_file_basic_initialization(self, sample_file_obj):
        """Test basic File initialization"""
        file = File(payload=sample_file_obj)
        assert file.payload == sample_file_obj
        assert file.file_name is None
        assert file.mime_type is None

    def test_file_full_initialization(self, sample_file_obj):
        """Test File initialization with all parameters"""
        file = File(payload=sample_file_obj, file_name="test.txt", mime_type="text/plain")
        assert file.payload == sample_file_obj
        assert file.file_name == "test.txt"
        assert file.mime_type == "text/plain"

    def test_file_to_tuple(self, sample_file_obj):
        """Test conversion to tuple format"""
        file = File(payload=sample_file_obj, file_name="test.txt", mime_type="text/plain")
        tuple_result = file.to_tuple()
        assert tuple_result == ("test.txt", sample_file_obj, "text/plain")


class TestResponse:
    def test_response_initialization(self):
        """Test basic Response initialization"""
        response = Response(
            status_code=HTTPStatus.OK,
            content=b"Test content",
            headers={"Content-Type": "text/plain"},
            parsed="Parsed content",
        )
        assert response.status_code == HTTPStatus.OK
        assert response.content == b"Test content"
        assert response.headers == {"Content-Type": "text/plain"}
        assert response.parsed == "Parsed content"

    def test_response_with_none_parsed(self):
        """Test Response with None parsed content"""
        response = Response(status_code=HTTPStatus.NO_CONTENT, content=b"", headers={}, parsed=None)
        assert response.status_code == HTTPStatus.NO_CONTENT
        assert response.content == b""
        assert response.headers == {}
        assert response.parsed is None

    def test_response_with_different_status_codes(self):
        """Test Response with various HTTP status codes"""
        status_codes = [
            HTTPStatus.OK,
            HTTPStatus.CREATED,
            HTTPStatus.ACCEPTED,
            HTTPStatus.NO_CONTENT,
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.NOT_FOUND,
        ]
        for status_code in status_codes:
            response = Response(status_code=status_code, content=b"", headers={}, parsed=None)
            assert response.status_code == status_code

    def test_response_with_different_content_types(self):
        """Test Response with different content types in headers"""
        content_types = ["text/plain", "application/json", "application/xml", "text/html"]
        for content_type in content_types:
            response = Response(
                status_code=HTTPStatus.OK, content=b"Test content", headers={"Content-Type": content_type}, parsed=None
            )
            assert response.headers["Content-Type"] == content_type

    def test_response_with_binary_content(self):
        """Test Response with binary content"""
        binary_content = b"\x00\x01\x02\x03"
        response = Response(
            status_code=HTTPStatus.OK,
            content=binary_content,
            headers={"Content-Type": "application/octet-stream"},
            parsed=None,
        )
        assert response.content == binary_content

    def test_response_with_multiple_headers(self):
        """Test Response with multiple headers"""
        headers = {
            "Content-Type": "application/json",
            "Content-Length": "100",
            "Authorization": "Bearer token",
            "X-Custom-Header": "custom-value",
        }
        response = Response(status_code=HTTPStatus.OK, content=b"{}", headers=headers, parsed=None)
        assert response.headers == headers
