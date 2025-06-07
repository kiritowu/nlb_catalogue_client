import httpx
import pytest

from nlb_catalogue_client.client import AuthenticatedClient, Client


@pytest.fixture
def base_url():
    return "https://api.example.com"


@pytest.fixture
def test_client(base_url):
    return Client(base_url=base_url)


@pytest.fixture
def test_auth_client(base_url):
    return AuthenticatedClient(base_url=base_url, token="test_token")


class TestClient:
    def test_client_initialization(self, base_url):
        client = Client(base_url=base_url)
        assert client._base_url == base_url
        assert client._cookies == {}
        assert client._headers == {}
        assert client._timeout is None
        assert client._verify_ssl is True
        assert client._follow_redirects is False
        assert client._httpx_args == dict()

    def test_client_is_none_when_initialized(self, base_url):
        # HTTPX Client are not initialized when Client is declared
        client = Client(base_url=base_url)
        assert client._client is None
        assert client._async_client is None

    def test_with_headers(self, test_client):
        new_headers = {"X-Test": "test"}
        updated_client = test_client.with_headers(new_headers)
        assert updated_client._headers == new_headers

    def test_with_headers_sync(self, test_client):
        new_headers = {"X-Test": "test"}
        with test_client as test_client:
            updated_client = test_client.with_headers(new_headers)
            assert updated_client._headers == new_headers

    @pytest.mark.asyncio
    async def test_with_headers_async(self, test_client):
        new_headers = {"X-Test": "test"}
        async with test_client as test_client:
            updated_client = test_client.with_headers(new_headers)
            assert updated_client._headers == new_headers

    def test_with_cookies(self, test_client):
        new_cookies = {"session": "test123"}
        updated_client = test_client.with_cookies(new_cookies)
        assert updated_client._cookies == new_cookies

    def test_with_cookies_sync(self, test_client):
        new_cookies = {"session": "test123"}
        with test_client as test_client:
            updated_client = test_client.with_cookies(new_cookies)
            assert updated_client._cookies == new_cookies

    @pytest.mark.asyncio
    async def test_with_cookies_async(self, test_client):
        new_cookies = {"session": "test123"}
        async with test_client as test_client:
            updated_client = test_client.with_cookies(new_cookies)
            assert updated_client._cookies == new_cookies

    def test_with_timeout(self, test_client):
        timeout = httpx.Timeout(10.0)
        updated_client = test_client.with_timeout(timeout)
        assert updated_client._timeout == timeout

    def test_with_timeout_sync(self, test_client):
        timeout = httpx.Timeout(10.0)
        with test_client as test_client:
            updated_client = test_client.with_timeout(timeout)
            assert updated_client._timeout == timeout

    @pytest.mark.asyncio
    async def test_with_timeout_async(self, test_client):
        timeout = httpx.Timeout(10.0)
        async with test_client as test_client:
            updated_client = test_client.with_timeout(timeout)
            assert updated_client._timeout == timeout

    def test_get_httpx_client(self, test_client):
        httpx_client = test_client.get_httpx_client()
        assert isinstance(httpx_client, httpx.Client)
        assert httpx_client.base_url == test_client._base_url

    @pytest.mark.asyncio
    async def test_get_async_httpx_client(self, test_client):
        async_client = test_client.get_async_httpx_client()
        assert isinstance(async_client, httpx.AsyncClient)
        assert async_client.base_url == test_client._base_url

    def test_context_manager(self, test_client):
        with test_client as client:
            assert isinstance(client, Client)
            assert client._client is not None

    def test_set_httpx_client(self, test_client):
        custom_client = httpx.Client(base_url="https://custom.example.com")
        updated_client = test_client.set_httpx_client(custom_client)
        assert updated_client._client == custom_client

    def test_set_async_httpx_client(self, test_client):
        custom_client = httpx.AsyncClient(base_url="https://custom.example.com")
        updated_client = test_client.set_async_httpx_client(custom_client)
        assert updated_client._async_client == custom_client

    @pytest.mark.asyncio
    async def test_async_context_manager(self, test_client):
        async with test_client as client:
            assert isinstance(client, Client)
            assert client._async_client is not None

    def test_client_with_custom_settings(self, base_url):
        custom_headers = {"X-Custom": "value"}
        custom_cookies = {"session": "123"}
        custom_timeout = httpx.Timeout(30.0)

        client = Client(
            base_url=base_url,
            headers=custom_headers,
            cookies=custom_cookies,
            timeout=custom_timeout,
            verify_ssl=False,
            follow_redirects=True,
            httpx_args={"http2": True},
        )

        assert client._headers == custom_headers
        assert client._cookies == custom_cookies
        assert client._timeout == custom_timeout
        assert client._verify_ssl is False
        assert client._follow_redirects is True
        assert client._httpx_args == {"http2": True}


class TestAuthenticatedClient:
    def test_auth_client_initialization(self, base_url):
        client = AuthenticatedClient(base_url=base_url, token="test_token")
        assert client._base_url == base_url
        assert client.token == "test_token"
        assert client.prefix == "Bearer"
        assert client.auth_header_name == "Authorization"
        assert client._cookies == {}
        assert client._headers == {}
        assert client._timeout is None
        assert client._verify_ssl is True
        assert client._follow_redirects is False
        assert client._httpx_args == dict()

    def test_auth_header_in_client(self, test_auth_client):
        httpx_client = test_auth_client.get_httpx_client()
        assert httpx_client.headers["Authorization"] == "Bearer test_token"

    def test_custom_auth_prefix(self, base_url):
        client = AuthenticatedClient(base_url=base_url, token="test_token", prefix="Basic")
        httpx_client = client.get_httpx_client()
        assert httpx_client.headers["Authorization"] == "Basic test_token"

    def test_with_headers_auth_client(self, test_auth_client):
        new_headers = {"X-Test": "test"}
        updated_client = test_auth_client.with_headers(new_headers)
        assert updated_client._headers == {
            **new_headers,
        }

    def test_with_headers_auth_client_sync(self, test_auth_client):
        new_headers = {"X-Test": "test"}
        with test_auth_client as test_auth_client:
            updated_client = test_auth_client.with_headers(new_headers)
            assert updated_client._headers.get("X-Test") == "test"

    @pytest.mark.asyncio
    async def test_with_headers_auth_client_async(self, test_auth_client):
        new_headers = {"X-Test": "test"}
        async with test_auth_client as test_auth_client:
            updated_client = test_auth_client.with_headers(new_headers)
            assert updated_client._headers.get("X-Test") == "test"

    def test_with_cookies(self, test_auth_client):
        new_cookies = {"session": "test123"}
        updated_client = test_auth_client.with_cookies(new_cookies)
        assert updated_client._cookies == new_cookies

    def test_with_cookies_sync(self, test_auth_client):
        new_cookies = {"session": "test123"}
        with test_auth_client as test_client:
            updated_client = test_client.with_cookies(new_cookies)
            assert updated_client._cookies == new_cookies

    @pytest.mark.asyncio
    async def test_with_cookies_async(self, test_auth_client):
        new_cookies = {"session": "test123"}
        async with test_auth_client as test_client:
            updated_client = test_client.with_cookies(new_cookies)
            assert updated_client._cookies == new_cookies

    def test_with_timeout(self, test_auth_client):
        timeout = httpx.Timeout(10.0)
        updated_client = test_auth_client.with_timeout(timeout)
        assert updated_client._timeout == timeout

    def test_with_timeout_sync(self, test_auth_client):
        timeout = httpx.Timeout(10.0)
        with test_auth_client as test_client:
            updated_client = test_client.with_timeout(timeout)
            assert updated_client._timeout == timeout

    @pytest.mark.asyncio
    async def test_with_timeout_async(self, test_auth_client):
        timeout = httpx.Timeout(10.0)
        async with test_auth_client as test_client:
            updated_client = test_client.with_timeout(timeout)
            assert updated_client._timeout == timeout

    @pytest.mark.asyncio
    async def test_async_auth_client(self, test_auth_client):
        async_client = test_auth_client.get_async_httpx_client()
        assert isinstance(async_client, httpx.AsyncClient)
        assert async_client.headers["Authorization"] == "Bearer test_token"

    def test_auth_context_manager(self, test_auth_client):
        with test_auth_client as client:
            assert isinstance(client, AuthenticatedClient)
            assert client._client is not None
            assert client._client.headers["Authorization"] == "Bearer test_token"

    def test_auth_client_without_prefix(self, base_url):
        client = AuthenticatedClient(
            base_url=base_url,
            token="test_token",
            prefix="",  # Empty prefix
        )
        httpx_client = client.get_httpx_client()
        assert httpx_client.headers["Authorization"] == "test_token"

    def test_set_httpx_client_auth(self, test_auth_client):
        custom_client = httpx.Client(base_url="https://custom.example.com")
        updated_client = test_auth_client.set_httpx_client(custom_client)
        assert updated_client._client == custom_client

    def test_set_async_httpx_client_auth(self, test_auth_client):
        custom_client = httpx.AsyncClient(base_url="https://custom.example.com")
        updated_client = test_auth_client.set_async_httpx_client(custom_client)
        assert updated_client._async_client == custom_client

    @pytest.mark.asyncio
    async def test_async_context_manager_auth(self, test_auth_client):
        async with test_auth_client as client:
            assert isinstance(client, AuthenticatedClient)
            assert client._async_client is not None
            assert client._async_client.headers["Authorization"] == "Bearer test_token"

    def test_auth_client_with_custom_settings(self, base_url):
        custom_headers = {"X-Custom": "value"}
        custom_cookies = {"session": "123"}
        custom_timeout = httpx.Timeout(30.0)

        client = AuthenticatedClient(
            base_url=base_url,
            token="test_token",
            headers=custom_headers,
            cookies=custom_cookies,
            timeout=custom_timeout,
            verify_ssl=False,
            follow_redirects=True,
            httpx_args={"http2": True},
        )

        assert client._headers == custom_headers
        assert client._cookies == custom_cookies
        assert client._timeout == custom_timeout
        assert client._verify_ssl is False
        assert client._follow_redirects is True
        assert client._httpx_args == {"http2": True}
