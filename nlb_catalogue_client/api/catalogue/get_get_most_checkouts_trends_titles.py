from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request_error import BadRequestError
from ...models.internal_server_error import InternalServerError
from ...models.method_not_allowed_error import MethodNotAllowedError
from ...models.not_found_error import NotFoundError
from ...models.search_most_checkouts_titles_response import SearchMostCheckoutsTitlesResponse
from ...models.service_unavailable_error import ServiceUnavailableError
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    location_code: str,
    duration: Union[Unset, str] = "past30days",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["LocationCode"] = location_code

    params["Duration"] = duration

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/GetMostCheckoutsTrendsTitles",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        BadRequestError,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        SearchMostCheckoutsTitlesResponse,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    if response.status_code == 200:
        response_200 = SearchMostCheckoutsTitlesResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = BadRequestError.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = NotFoundError.from_dict(response.json())

        return response_404
    if response.status_code == 405:
        response_405 = MethodNotAllowedError.from_dict(response.json())

        return response_405
    if response.status_code == 429:
        response_429 = TooManyRequestsError.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = InternalServerError.from_dict(response.json())

        return response_500
    if response.status_code == 503:
        response_503 = ServiceUnavailableError.from_dict(response.json())

        return response_503
    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        BadRequestError,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        SearchMostCheckoutsTitlesResponse,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    location_code: str,
    duration: Union[Unset, str] = "past30days",
) -> Response[
    Union[
        BadRequestError,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        SearchMostCheckoutsTitlesResponse,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    """This function may be used to search and retrieve statistics of most checkout trends titles and
    filter by location.

     This function may be used to retrieve the most checkout trends titles by location.

    Args:
        location_code (str):  Example: AMKPL.
        duration (Union[Unset, str]):  Default: 'past30days'. Example: past30days.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestError, InternalServerError, MethodNotAllowedError, NotFoundError, SearchMostCheckoutsTitlesResponse, ServiceUnavailableError, TooManyRequestsError, UnauthorizedError]]
    """

    kwargs = _get_kwargs(
        location_code=location_code,
        duration=duration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    location_code: str,
    duration: Union[Unset, str] = "past30days",
) -> Optional[
    Union[
        BadRequestError,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        SearchMostCheckoutsTitlesResponse,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    """This function may be used to search and retrieve statistics of most checkout trends titles and
    filter by location.

     This function may be used to retrieve the most checkout trends titles by location.

    Args:
        location_code (str):  Example: AMKPL.
        duration (Union[Unset, str]):  Default: 'past30days'. Example: past30days.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestError, InternalServerError, MethodNotAllowedError, NotFoundError, SearchMostCheckoutsTitlesResponse, ServiceUnavailableError, TooManyRequestsError, UnauthorizedError]
    """

    return sync_detailed(
        client=client,
        location_code=location_code,
        duration=duration,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    location_code: str,
    duration: Union[Unset, str] = "past30days",
) -> Response[
    Union[
        BadRequestError,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        SearchMostCheckoutsTitlesResponse,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    """This function may be used to search and retrieve statistics of most checkout trends titles and
    filter by location.

     This function may be used to retrieve the most checkout trends titles by location.

    Args:
        location_code (str):  Example: AMKPL.
        duration (Union[Unset, str]):  Default: 'past30days'. Example: past30days.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestError, InternalServerError, MethodNotAllowedError, NotFoundError, SearchMostCheckoutsTitlesResponse, ServiceUnavailableError, TooManyRequestsError, UnauthorizedError]]
    """

    kwargs = _get_kwargs(
        location_code=location_code,
        duration=duration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    location_code: str,
    duration: Union[Unset, str] = "past30days",
) -> Optional[
    Union[
        BadRequestError,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        SearchMostCheckoutsTitlesResponse,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    """This function may be used to search and retrieve statistics of most checkout trends titles and
    filter by location.

     This function may be used to retrieve the most checkout trends titles by location.

    Args:
        location_code (str):  Example: AMKPL.
        duration (Union[Unset, str]):  Default: 'past30days'. Example: past30days.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestError, InternalServerError, MethodNotAllowedError, NotFoundError, SearchMostCheckoutsTitlesResponse, ServiceUnavailableError, TooManyRequestsError, UnauthorizedError]
    """

    return (
        await asyncio_detailed(
            client=client,
            location_code=location_code,
            duration=duration,
        )
    ).parsed
