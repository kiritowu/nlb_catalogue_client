from http import HTTPStatus
from typing import Any, Dict

import httpx
import pytest
from tenacity import wait_none

from nlb_catalogue_client.api.catalogue import get_get_new_titles
from nlb_catalogue_client.client import AuthenticatedClient
from nlb_catalogue_client.errors import UnexpectedStatus
from nlb_catalogue_client.models.search_new_titles_response_v2 import SearchNewTitlesResponseV2


@pytest.fixture()
def client() -> AuthenticatedClient:
    return AuthenticatedClient(base_url="https://api.example.com", token="test_token", raise_on_unexpected_status=True)


@pytest.fixture()
def success_response() -> Dict[str, Any]:
    return {
        "totalRecords": 100,
        "count": 20,
        "nextRecordsOffset": 20,
        "hasMoreRecords": True,
        "titles": [
            {
                "format": {"code": "BK", "name": "BOOK"},
                "brn": 123456,
                "digitalId": None,
                "title": "Sample Book Title",
                "nativeTitle": None,
                "author": "John Doe",
                "nativeAuthor": None,
                "otherAuthors": ["Jane Smith"],
                "nativeOtherAuthors": None,
                "isbns": ["9781234567890"],
                "language": ["English"],
                "allowReservation": True,
                "isRestricted": False,
                "activeReservationsCount": 0,
            }
        ],
    }


@pytest.fixture()
def error_responses() -> Dict[int, Dict[str, Any]]:
    return {
        400: {"error": "Bad Request", "message": "Invalid request parameters", "statusCode": 400},
        401: {"error": "Unauthorized", "message": "Authentication token is invalid", "statusCode": 401},
        404: {"error": "Not Found", "message": "Resource not found", "statusCode": 404},
        405: {"error": "Method Not Allowed", "message": "HTTP method not allowed", "statusCode": 405},
        429: {"error": "Too Many Requests", "message": "Rate limit exceeded", "statusCode": 429},
        500: {"error": "Internal Server Error", "message": "An unexpected error occurred", "statusCode": 500},
        503: {"error": "Service Unavailable", "message": "Service is temporarily unavailable", "statusCode": 503},
    }


@pytest.fixture()
def mock_response(success_response) -> httpx.Response:
    return httpx.Response(
        status_code=200,
        json=success_response,
    )


class TestGetNewTitles:
    def test_get_kwargs(self):
        kwargs = get_get_new_titles._get_kwargs(
            date_range="Monthly",
            limit=50,
            sort_fields="title",
            set_id=1,
            offset=20,
            material_types=["BK", "DVD"],
            intended_audiences=["ADULT", "TEEN"],
            languages=["ENG", "CHI"],
            availability=True,
            fiction=True,
            locations=["ABC"],
        )

        assert kwargs == {
            "method": "get",
            "url": "/GetNewTitles",
            "params": {
                "DateRange": "Monthly",
                "Limit": 50,
                "SortFields": "title",
                "SetId": 1,
                "Offset": 20,
                "MaterialTypes": ["BK", "DVD"],
                "IntendedAudiences": ["ADULT", "TEEN"],
                "Languages": ["ENG", "CHI"],
                "Availability": True,
                "Fiction": True,
                "Locations": ["ABC"],
            },
        }

    def test_get_kwargs_with_defaults(self):
        kwargs = get_get_new_titles._get_kwargs()

        assert kwargs == {
            "method": "get",
            "url": "/GetNewTitles",
            "params": {
                "DateRange": "Weekly",
                "Limit": 200,
                "SetId": 0,
                "Offset": 0,
            },
        }

    def test_sync_detailed_success(self, mocker, client: AuthenticatedClient, mock_response: httpx.Response):
        mocker.patch("httpx.Client.request", return_value=mock_response)

        response = get_get_new_titles.sync_detailed(client=client)

        assert response.status_code == HTTPStatus.OK
        assert isinstance(response.parsed, SearchNewTitlesResponseV2)
        assert response.parsed.total_records == 100
        assert response.parsed.count == 20
        assert response.parsed.next_records_offset == 20
        assert response.parsed.has_more_records is True
        assert len(response.parsed.titles) == 1
        assert response.parsed.titles[0].brn == 123456

    def test_sync_success(self, mocker, client: AuthenticatedClient, mock_response: httpx.Response):
        mocker.patch("httpx.Client.request", return_value=mock_response)

        response = get_get_new_titles.sync(client=client)

        assert isinstance(response, SearchNewTitlesResponseV2)
        assert response.total_records == 100
        assert response.count == 20
        assert response.next_records_offset == 20
        assert response.has_more_records is True
        assert len(response.titles) == 1
        assert response.titles[0].brn == 123456

    @pytest.mark.asyncio
    async def test_asyncio_detailed_success(self, mocker, client: AuthenticatedClient, mock_response: httpx.Response):
        mocker.patch("httpx.AsyncClient.request", return_value=mock_response)

        response = await get_get_new_titles.asyncio_detailed(client=client)

        assert response.status_code == HTTPStatus.OK
        assert isinstance(response.parsed, SearchNewTitlesResponseV2)
        assert response.parsed.total_records == 100
        assert response.parsed.count == 20
        assert response.parsed.next_records_offset == 20
        assert response.parsed.has_more_records is True
        assert len(response.parsed.titles) == 1
        assert response.parsed.titles[0].brn == 123456

    @pytest.mark.asyncio
    async def test_asyncio_success(self, mocker, client: AuthenticatedClient, mock_response: httpx.Response):
        mocker.patch("httpx.AsyncClient.request", return_value=mock_response)

        response = await get_get_new_titles.asyncio(client=client)

        assert isinstance(response, SearchNewTitlesResponseV2)
        assert response.total_records == 100
        assert response.count == 20
        assert response.next_records_offset == 20
        assert response.has_more_records is True
        assert len(response.titles) == 1
        assert response.titles[0].brn == 123456

    @pytest.mark.parametrize(
        "status_code,error_type",
        [
            (400, "BadRequestError"),
            (401, "UnauthorizedError"),
            (404, "NotFoundError"),
            (405, "MethodNotAllowedError"),
            (429, "TooManyRequestsError"),
            (500, "InternalServerError"),
            (503, "ServiceUnavailableError"),
        ],
    )
    def test_error_responses_sync(
        self,
        mocker,
        client: AuthenticatedClient,
        error_responses: Dict[int, Dict[str, Any]],
        status_code: int,
        error_type: str,
    ):
        error_mock_response = httpx.Response(
            status_code=status_code,
            json=error_responses[status_code],
        )
        mocker.patch("httpx.Client.request", return_value=error_mock_response)

        # Tenacity to stop waiting
        get_get_new_titles.sync_detailed.retry.wait = wait_none()

        response = get_get_new_titles.sync_detailed(client=client)

        assert response.status_code == status_code
        assert error_type in str(type(response.parsed))
        assert response.parsed
        assert not isinstance(response.parsed, SearchNewTitlesResponseV2)
        assert response.parsed.error == error_responses[status_code]["error"]
        assert response.parsed.message == error_responses[status_code]["message"]
        assert response.parsed.status_code == status_code

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "status_code,error_type",
        [
            (400, "BadRequestError"),
            (401, "UnauthorizedError"),
            (404, "NotFoundError"),
            (405, "MethodNotAllowedError"),
            (429, "TooManyRequestsError"),
            (500, "InternalServerError"),
            (503, "ServiceUnavailableError"),
        ],
    )
    async def test_error_responses_async(
        self,
        mocker,
        client: AuthenticatedClient,
        error_responses: Dict[int, Dict[str, Any]],
        status_code: int,
        error_type: str,
    ):
        error_mock_response = httpx.Response(
            status_code=status_code,
            json=error_responses[status_code],
        )
        mocker.patch("httpx.AsyncClient.request", return_value=error_mock_response)

        # Tenacity to stop waiting
        get_get_new_titles.asyncio_detailed.retry.wait = wait_none()

        response = await get_get_new_titles.asyncio_detailed(client=client)

        assert response.status_code == status_code
        assert error_type in str(type(response.parsed))
        assert response.parsed
        assert not isinstance(response.parsed, SearchNewTitlesResponseV2)
        assert response.parsed.error == error_responses[status_code]["error"]
        assert response.parsed.message == error_responses[status_code]["message"]
        assert response.parsed.status_code == status_code

    def test_sync_detailed_unexpected_status_raises(
        self,
        mocker,
        client: AuthenticatedClient,
    ):
        unexpected_response = httpx.Response(
            status_code=418,  # I'm a teapot - unexpected status
            json={"error": "Unexpected", "message": "I'm a teapot", "statusCode": 418},
        )
        mocker.patch("httpx.Client.request", return_value=unexpected_response)

        with pytest.raises(UnexpectedStatus):
            get_get_new_titles.sync_detailed(client=client)

    def test_sync_detailed_unexpected_status_return_none(
        self,
        mocker,
        client: AuthenticatedClient,
    ):
        unexpected_response = httpx.Response(
            status_code=418,  # I'm a teapot - unexpected status
            json={"error": "Unexpected", "message": "I'm a teapot", "statusCode": 418},
        )
        mocker.patch("httpx.Client.request", return_value=unexpected_response)
        client.raise_on_unexpected_status = False

        assert get_get_new_titles.sync_detailed(client=client).parsed is None
