from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.suggestion_page_saved_meal_summary import SuggestionPageSavedMealSummary
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    limit: int | Unset = 10,
    offset: int | Unset = 0,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/saved-meals/suggestions",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | SuggestionPageSavedMealSummary:
    if response.status_code == 200:
        response_200 = SuggestionPageSavedMealSummary.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = ErrorModel.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | SuggestionPageSavedMealSummary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = 10,
    offset: int | Unset = 0,

) -> Response[AccountProblem | ErrorModel | SuggestionPageSavedMealSummary]:
    """ Suggest saved meals

    Args:
        q (str | Unset):
        limit (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | SuggestionPageSavedMealSummary]
     """


    kwargs = _get_kwargs(
        q=q,
limit=limit,
offset=offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = 10,
    offset: int | Unset = 0,

) -> AccountProblem | ErrorModel | SuggestionPageSavedMealSummary | None:
    """ Suggest saved meals

    Args:
        q (str | Unset):
        limit (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | SuggestionPageSavedMealSummary
     """


    return sync_detailed(
        client=client,
q=q,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = 10,
    offset: int | Unset = 0,

) -> Response[AccountProblem | ErrorModel | SuggestionPageSavedMealSummary]:
    """ Suggest saved meals

    Args:
        q (str | Unset):
        limit (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | SuggestionPageSavedMealSummary]
     """


    kwargs = _get_kwargs(
        q=q,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = 10,
    offset: int | Unset = 0,

) -> AccountProblem | ErrorModel | SuggestionPageSavedMealSummary | None:
    """ Suggest saved meals

    Args:
        q (str | Unset):
        limit (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | SuggestionPageSavedMealSummary
     """


    return (await asyncio_detailed(
        client=client,
q=q,
limit=limit,
offset=offset,

    )).parsed
