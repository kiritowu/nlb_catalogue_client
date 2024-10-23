from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request_error import BadRequestError
from ...models.get_title_details_response_v2 import GetTitleDetailsResponseV2
from ...models.internal_server_error import InternalServerError
from ...models.method_not_allowed_error import MethodNotAllowedError
from ...models.not_found_error import NotFoundError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    brn: Union[Unset, int] = UNSET,
    isbn: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["BRN"] = brn

    params["ISBN"] = isbn

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/GetTitleDetails",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        BadRequestError,
        GetTitleDetailsResponseV2,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    if response.status_code == 200:
        response_200 = GetTitleDetailsResponseV2.from_dict(response.json())

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
        GetTitleDetailsResponseV2,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
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
    brn: Union[Unset, int] = UNSET,
    isbn: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        BadRequestError,
        GetTitleDetailsResponseV2,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    """Getting the detailed information of an item

     This function may be used to retrieve the title information.
                                                        <p>At least one of the search fields is required:</p>
                                <ul>
                                <li>BRN</li>
                                <li>ISBN</li>
                                </ul>

    Args:
        brn (Union[Unset, int]):
        isbn (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestError, GetTitleDetailsResponseV2, InternalServerError, MethodNotAllowedError, NotFoundError, ServiceUnavailableError, TooManyRequestsError, UnauthorizedError]]
    """

    kwargs = _get_kwargs(
        brn=brn,
        isbn=isbn,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    brn: Union[Unset, int] = UNSET,
    isbn: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        BadRequestError,
        GetTitleDetailsResponseV2,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    """Getting the detailed information of an item

     This function may be used to retrieve the title information.
                                                        <p>At least one of the search fields is required:</p>
                                <ul>
                                <li>BRN</li>
                                <li>ISBN</li>
                                </ul>

    Args:
        brn (Union[Unset, int]):
        isbn (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestError, GetTitleDetailsResponseV2, InternalServerError, MethodNotAllowedError, NotFoundError, ServiceUnavailableError, TooManyRequestsError, UnauthorizedError]
    """

    return sync_detailed(
        client=client,
        brn=brn,
        isbn=isbn,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    brn: Union[Unset, int] = UNSET,
    isbn: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        BadRequestError,
        GetTitleDetailsResponseV2,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    """Getting the detailed information of an item

     This function may be used to retrieve the title information.
                                                        <p>At least one of the search fields is required:</p>
                                <ul>
                                <li>BRN</li>
                                <li>ISBN</li>
                                </ul>

    Args:
        brn (Union[Unset, int]):
        isbn (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestError, GetTitleDetailsResponseV2, InternalServerError, MethodNotAllowedError, NotFoundError, ServiceUnavailableError, TooManyRequestsError, UnauthorizedError]]
    """

    kwargs = _get_kwargs(
        brn=brn,
        isbn=isbn,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    brn: Union[Unset, int] = UNSET,
    isbn: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        BadRequestError,
        GetTitleDetailsResponseV2,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    """Getting the detailed information of an item

     This function may be used to retrieve the title information.
                                                        <p>At least one of the search fields is required:</p>
                                <ul>
                                <li>BRN</li>
                                <li>ISBN</li>
                                </ul>

    Args:
        brn (Union[Unset, int]):
        isbn (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestError, GetTitleDetailsResponseV2, InternalServerError, MethodNotAllowedError, NotFoundError, ServiceUnavailableError, TooManyRequestsError, UnauthorizedError]
    """

    return (
        await asyncio_detailed(
            client=client,
            brn=brn,
            isbn=isbn,
        )
    ).parsed
