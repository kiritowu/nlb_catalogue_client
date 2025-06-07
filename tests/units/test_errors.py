from nlb_catalogue_client.errors import UnexpectedStatus


class TestUnexpectedStatus:
    def test_basic_initialization(self):
        """Test basic initialization with simple values"""
        error = UnexpectedStatus(404, b"Not Found")
        assert error.status_code == 404
        assert error.content == b"Not Found"

    def test_error_message_format(self):
        """Test the formatted error message"""
        error = UnexpectedStatus(500, b"Server Error")
        expected_message = "Unexpected status code: 500\n\nResponse content:\nServer Error"
        assert str(error) == expected_message

    def test_with_empty_content(self):
        """Test initialization with empty content"""
        error = UnexpectedStatus(400, b"")
        assert error.status_code == 400
        assert error.content == b""
        assert str(error) == "Unexpected status code: 400\n\nResponse content:\n"

    def test_inheritance(self):
        """Test proper inheritance from Exception"""
        error = UnexpectedStatus(404, b"Not Found")
        assert isinstance(error, Exception)
        assert isinstance(error, UnexpectedStatus)
