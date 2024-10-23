from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request_error import BadRequestError
from ...models.internal_server_error import InternalServerError
from ...models.method_not_allowed_error import MethodNotAllowedError
from ...models.not_found_error import NotFoundError
from ...models.search_new_titles_response_v2 import SearchNewTitlesResponseV2
from ...models.service_unavailable_error import ServiceUnavailableError
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date_range: str = "Weekly",
    limit: Union[Unset, int] = 200,
    sort_fields: Union[Unset, str] = UNSET,
    set_id: Union[Unset, int] = 0,
    offset: Union[Unset, int] = 0,
    material_types: Union[Unset, List[str]] = UNSET,
    intended_audiences: Union[Unset, List[str]] = UNSET,
    date_from: Union[Unset, int] = UNSET,
    date_to: Union[Unset, int] = UNSET,
    locations: Union[Unset, List[str]] = UNSET,
    languages: Union[Unset, List[str]] = UNSET,
    availability: Union[Unset, bool] = UNSET,
    fiction: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["DateRange"] = date_range

    params["Limit"] = limit

    params["SortFields"] = sort_fields

    params["SetId"] = set_id

    params["Offset"] = offset

    json_material_types: Union[Unset, List[str]] = UNSET
    if not isinstance(material_types, Unset):
        json_material_types = material_types

    params["MaterialTypes"] = json_material_types

    json_intended_audiences: Union[Unset, List[str]] = UNSET
    if not isinstance(intended_audiences, Unset):
        json_intended_audiences = intended_audiences

    params["IntendedAudiences"] = json_intended_audiences

    params["DateFrom"] = date_from

    params["DateTo"] = date_to

    json_locations: Union[Unset, List[str]] = UNSET
    if not isinstance(locations, Unset):
        json_locations = locations

    params["Locations"] = json_locations

    json_languages: Union[Unset, List[str]] = UNSET
    if not isinstance(languages, Unset):
        json_languages = languages

    params["Languages"] = json_languages

    params["Availability"] = availability

    params["Fiction"] = fiction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/GetNewTitles",
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
        SearchNewTitlesResponseV2,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    if response.status_code == 200:
        response_200 = SearchNewTitlesResponseV2.from_dict(response.json())

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
        SearchNewTitlesResponseV2,
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
    date_range: str = "Weekly",
    limit: Union[Unset, int] = 200,
    sort_fields: Union[Unset, str] = UNSET,
    set_id: Union[Unset, int] = 0,
    offset: Union[Unset, int] = 0,
    material_types: Union[Unset, List[str]] = UNSET,
    intended_audiences: Union[Unset, List[str]] = UNSET,
    date_from: Union[Unset, int] = UNSET,
    date_to: Union[Unset, int] = UNSET,
    locations: Union[Unset, List[str]] = UNSET,
    languages: Union[Unset, List[str]] = UNSET,
    availability: Union[Unset, bool] = UNSET,
    fiction: Union[Unset, bool] = UNSET,
) -> Response[
    Union[
        BadRequestError,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        SearchNewTitlesResponseV2,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    """This function may be used to browse the new arrival titles.

     This function may be used to Get the New titles using query parameter.

    Args:
        date_range (str):  Default: 'Weekly'.
        limit (Union[Unset, int]):  Default: 200.
        sort_fields (Union[Unset, str]):
        set_id (Union[Unset, int]):  Default: 0.
        offset (Union[Unset, int]):  Default: 0.
        material_types (Union[Unset, List[str]]):
        intended_audiences (Union[Unset, List[str]]):
        date_from (Union[Unset, int]):
        date_to (Union[Unset, int]):
        locations (Union[Unset, List[str]]):
        languages (Union[Unset, List[str]]):
        availability (Union[Unset, bool]):
        fiction (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestError, InternalServerError, MethodNotAllowedError, NotFoundError, SearchNewTitlesResponseV2, ServiceUnavailableError, TooManyRequestsError, UnauthorizedError]]
    """

    kwargs = _get_kwargs(
        date_range=date_range,
        limit=limit,
        sort_fields=sort_fields,
        set_id=set_id,
        offset=offset,
        material_types=material_types,
        intended_audiences=intended_audiences,
        date_from=date_from,
        date_to=date_to,
        locations=locations,
        languages=languages,
        availability=availability,
        fiction=fiction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    date_range: str = "Weekly",
    limit: Union[Unset, int] = 200,
    sort_fields: Union[Unset, str] = UNSET,
    set_id: Union[Unset, int] = 0,
    offset: Union[Unset, int] = 0,
    material_types: Union[Unset, List[str]] = UNSET,
    intended_audiences: Union[Unset, List[str]] = UNSET,
    date_from: Union[Unset, int] = UNSET,
    date_to: Union[Unset, int] = UNSET,
    locations: Union[Unset, List[str]] = UNSET,
    languages: Union[Unset, List[str]] = UNSET,
    availability: Union[Unset, bool] = UNSET,
    fiction: Union[Unset, bool] = UNSET,
) -> Optional[
    Union[
        BadRequestError,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        SearchNewTitlesResponseV2,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    """This function may be used to browse the new arrival titles.

     This function may be used to Get the New titles using query parameter.

    Args:
        date_range (str):  Default: 'Weekly'.
        limit (Union[Unset, int]):  Default: 200.
        sort_fields (Union[Unset, str]):
        set_id (Union[Unset, int]):  Default: 0.
        offset (Union[Unset, int]):  Default: 0.
        material_types (Union[Unset, List[str]]):
        intended_audiences (Union[Unset, List[str]]):
        date_from (Union[Unset, int]):
        date_to (Union[Unset, int]):
        locations (Union[Unset, List[str]]):
        languages (Union[Unset, List[str]]):
        availability (Union[Unset, bool]):
        fiction (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestError, InternalServerError, MethodNotAllowedError, NotFoundError, SearchNewTitlesResponseV2, ServiceUnavailableError, TooManyRequestsError, UnauthorizedError]
    """

    return sync_detailed(
        client=client,
        date_range=date_range,
        limit=limit,
        sort_fields=sort_fields,
        set_id=set_id,
        offset=offset,
        material_types=material_types,
        intended_audiences=intended_audiences,
        date_from=date_from,
        date_to=date_to,
        locations=locations,
        languages=languages,
        availability=availability,
        fiction=fiction,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date_range: str = "Weekly",
    limit: Union[Unset, int] = 200,
    sort_fields: Union[Unset, str] = UNSET,
    set_id: Union[Unset, int] = 0,
    offset: Union[Unset, int] = 0,
    material_types: Union[Unset, List[str]] = UNSET,
    intended_audiences: Union[Unset, List[str]] = UNSET,
    date_from: Union[Unset, int] = UNSET,
    date_to: Union[Unset, int] = UNSET,
    locations: Union[Unset, List[str]] = UNSET,
    languages: Union[Unset, List[str]] = UNSET,
    availability: Union[Unset, bool] = UNSET,
    fiction: Union[Unset, bool] = UNSET,
) -> Response[
    Union[
        BadRequestError,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        SearchNewTitlesResponseV2,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    """This function may be used to browse the new arrival titles.

     This function may be used to Get the New titles using query parameter.

    Args:
        date_range (str):  Default: 'Weekly'.
        limit (Union[Unset, int]):  Default: 200.
        sort_fields (Union[Unset, str]):
        set_id (Union[Unset, int]):  Default: 0.
        offset (Union[Unset, int]):  Default: 0.
        material_types (Union[Unset, List[str]]):
        intended_audiences (Union[Unset, List[str]]):
        date_from (Union[Unset, int]):
        date_to (Union[Unset, int]):
        locations (Union[Unset, List[str]]):
        languages (Union[Unset, List[str]]):
        availability (Union[Unset, bool]):
        fiction (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestError, InternalServerError, MethodNotAllowedError, NotFoundError, SearchNewTitlesResponseV2, ServiceUnavailableError, TooManyRequestsError, UnauthorizedError]]
    """

    kwargs = _get_kwargs(
        date_range=date_range,
        limit=limit,
        sort_fields=sort_fields,
        set_id=set_id,
        offset=offset,
        material_types=material_types,
        intended_audiences=intended_audiences,
        date_from=date_from,
        date_to=date_to,
        locations=locations,
        languages=languages,
        availability=availability,
        fiction=fiction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date_range: str = "Weekly",
    limit: Union[Unset, int] = 200,
    sort_fields: Union[Unset, str] = UNSET,
    set_id: Union[Unset, int] = 0,
    offset: Union[Unset, int] = 0,
    material_types: Union[Unset, List[str]] = UNSET,
    intended_audiences: Union[Unset, List[str]] = UNSET,
    date_from: Union[Unset, int] = UNSET,
    date_to: Union[Unset, int] = UNSET,
    locations: Union[Unset, List[str]] = UNSET,
    languages: Union[Unset, List[str]] = UNSET,
    availability: Union[Unset, bool] = UNSET,
    fiction: Union[Unset, bool] = UNSET,
) -> Optional[
    Union[
        BadRequestError,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        SearchNewTitlesResponseV2,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    ]
]:
    """This function may be used to browse the new arrival titles.

     This function may be used to Get the New titles using query parameter.

    Args:
        date_range (str):  Default: 'Weekly'.
        limit (Union[Unset, int]):  Default: 200.
        sort_fields (Union[Unset, str]):
        set_id (Union[Unset, int]):  Default: 0.
        offset (Union[Unset, int]):  Default: 0.
        material_types (Union[Unset, List[str]]):
        intended_audiences (Union[Unset, List[str]]):
        date_from (Union[Unset, int]):
        date_to (Union[Unset, int]):
        locations (Union[Unset, List[str]]):
        languages (Union[Unset, List[str]]):
        availability (Union[Unset, bool]):
        fiction (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestError, InternalServerError, MethodNotAllowedError, NotFoundError, SearchNewTitlesResponseV2, ServiceUnavailableError, TooManyRequestsError, UnauthorizedError]
    """

    return (
        await asyncio_detailed(
            client=client,
            date_range=date_range,
            limit=limit,
            sort_fields=sort_fields,
            set_id=set_id,
            offset=offset,
            material_types=material_types,
            intended_audiences=intended_audiences,
            date_from=date_from,
            date_to=date_to,
            locations=locations,
            languages=languages,
            availability=availability,
            fiction=fiction,
        )
    ).parsed
