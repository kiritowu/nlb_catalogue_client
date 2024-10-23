from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request_error import BadRequestError
from ...models.get_titles_response_v2 import GetTitlesResponseV2
from ...models.internal_server_error import InternalServerError
from ...models.method_not_allowed_error import MethodNotAllowedError
from ...models.not_found_error import NotFoundError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    keywords: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    author: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
    isbn: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    sort_fields: Union[Unset, str] = UNSET,
    set_id: Union[Unset, int] = 0,
    offset: Union[Unset, int] = 0,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["Keywords"] = keywords

    params["Title"] = title

    params["Author"] = author

    params["Subject"] = subject

    params["ISBN"] = isbn

    params["Limit"] = limit

    params["SortFields"] = sort_fields

    params["SetId"] = set_id

    params["Offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/GetTitles",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        BadRequestError,
        GetTitlesResponseV2,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    if response.status_code == 200:
        response_200 = GetTitlesResponseV2.from_dict(response.json())

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
        GetTitlesResponseV2,
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
    keywords: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    author: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
    isbn: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    sort_fields: Union[Unset, str] = UNSET,
    set_id: Union[Unset, int] = 0,
    offset: Union[Unset, int] = 0,
) -> Response[
    Union[
        BadRequestError,
        GetTitlesResponseV2,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    """Searching catalogue content according to search criteria

     This function may be used to search for titles using query parameter.
                                                        <p>This function provide multiple combination search, they will be processed with AND
    operation.</p>
                                                        <p>The request must contain at least one of the Keywords, ISBN, Author, Subject or Title.</p>

    Args:
        keywords (Union[Unset, str]):
        title (Union[Unset, str]):
        author (Union[Unset, str]):
        subject (Union[Unset, str]):
        isbn (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 20.
        sort_fields (Union[Unset, str]):
        set_id (Union[Unset, int]):  Default: 0.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestError, GetTitlesResponseV2, InternalServerError, MethodNotAllowedError, NotFoundError, ServiceUnavailableError, TooManyRequestsError, UnauthorizedError]]
    """

    kwargs = _get_kwargs(
        keywords=keywords,
        title=title,
        author=author,
        subject=subject,
        isbn=isbn,
        limit=limit,
        sort_fields=sort_fields,
        set_id=set_id,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keywords: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    author: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
    isbn: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    sort_fields: Union[Unset, str] = UNSET,
    set_id: Union[Unset, int] = 0,
    offset: Union[Unset, int] = 0,
) -> Optional[
    Union[
        BadRequestError,
        GetTitlesResponseV2,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    """Searching catalogue content according to search criteria

     This function may be used to search for titles using query parameter.
                                                        <p>This function provide multiple combination search, they will be processed with AND
    operation.</p>
                                                        <p>The request must contain at least one of the Keywords, ISBN, Author, Subject or Title.</p>

    Args:
        keywords (Union[Unset, str]):
        title (Union[Unset, str]):
        author (Union[Unset, str]):
        subject (Union[Unset, str]):
        isbn (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 20.
        sort_fields (Union[Unset, str]):
        set_id (Union[Unset, int]):  Default: 0.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestError, GetTitlesResponseV2, InternalServerError, MethodNotAllowedError, NotFoundError, ServiceUnavailableError, TooManyRequestsError, UnauthorizedError]
    """

    return sync_detailed(
        client=client,
        keywords=keywords,
        title=title,
        author=author,
        subject=subject,
        isbn=isbn,
        limit=limit,
        sort_fields=sort_fields,
        set_id=set_id,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keywords: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    author: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
    isbn: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    sort_fields: Union[Unset, str] = UNSET,
    set_id: Union[Unset, int] = 0,
    offset: Union[Unset, int] = 0,
) -> Response[
    Union[
        BadRequestError,
        GetTitlesResponseV2,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    """Searching catalogue content according to search criteria

     This function may be used to search for titles using query parameter.
                                                        <p>This function provide multiple combination search, they will be processed with AND
    operation.</p>
                                                        <p>The request must contain at least one of the Keywords, ISBN, Author, Subject or Title.</p>

    Args:
        keywords (Union[Unset, str]):
        title (Union[Unset, str]):
        author (Union[Unset, str]):
        subject (Union[Unset, str]):
        isbn (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 20.
        sort_fields (Union[Unset, str]):
        set_id (Union[Unset, int]):  Default: 0.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestError, GetTitlesResponseV2, InternalServerError, MethodNotAllowedError, NotFoundError, ServiceUnavailableError, TooManyRequestsError, UnauthorizedError]]
    """

    kwargs = _get_kwargs(
        keywords=keywords,
        title=title,
        author=author,
        subject=subject,
        isbn=isbn,
        limit=limit,
        sort_fields=sort_fields,
        set_id=set_id,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keywords: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    author: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
    isbn: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    sort_fields: Union[Unset, str] = UNSET,
    set_id: Union[Unset, int] = 0,
    offset: Union[Unset, int] = 0,
) -> Optional[
    Union[
        BadRequestError,
        GetTitlesResponseV2,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    """Searching catalogue content according to search criteria

     This function may be used to search for titles using query parameter.
                                                        <p>This function provide multiple combination search, they will be processed with AND
    operation.</p>
                                                        <p>The request must contain at least one of the Keywords, ISBN, Author, Subject or Title.</p>

    Args:
        keywords (Union[Unset, str]):
        title (Union[Unset, str]):
        author (Union[Unset, str]):
        subject (Union[Unset, str]):
        isbn (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 20.
        sort_fields (Union[Unset, str]):
        set_id (Union[Unset, int]):  Default: 0.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestError, GetTitlesResponseV2, InternalServerError, MethodNotAllowedError, NotFoundError, ServiceUnavailableError, TooManyRequestsError, UnauthorizedError]
    """

    return (
        await asyncio_detailed(
            client=client,
            keywords=keywords,
            title=title,
            author=author,
            subject=subject,
            isbn=isbn,
            limit=limit,
            sort_fields=sort_fields,
            set_id=set_id,
            offset=offset,
        )
    ).parsed
