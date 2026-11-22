from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.saved_meal import SavedMeal
from ...models.saved_meal_input import SavedMealInput
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: SavedMealInput,
    if_match: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match



    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/saved-meals/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | SavedMeal | None:
    if response.status_code == 200:
        response_200 = SavedMeal.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorModel.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = ErrorModel.from_dict(response.json())



        return response_404

    if response.status_code == 412:
        response_412 = ErrorModel.from_dict(response.json())



        return response_412

    if response.status_code == 422:
        response_422 = ErrorModel.from_dict(response.json())



        return response_422

    if response.status_code == 428:
        response_428 = ErrorModel.from_dict(response.json())



        return response_428

    if response.status_code == 500:
        response_500 = ErrorModel.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | SavedMeal]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SavedMealInput,
    if_match: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | SavedMeal]:
    """ Replace a reusable meal

    Args:
        id (str):
        if_match (str | Unset): The current response body revision in double quotes, such as "4".
            Do not use the GET response ETag or put revision in the body.
        body (SavedMealInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | SavedMeal]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
if_match=if_match,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SavedMealInput,
    if_match: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | SavedMeal | None:
    """ Replace a reusable meal

    Args:
        id (str):
        if_match (str | Unset): The current response body revision in double quotes, such as "4".
            Do not use the GET response ETag or put revision in the body.
        body (SavedMealInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | SavedMeal
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
if_match=if_match,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SavedMealInput,
    if_match: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | SavedMeal]:
    """ Replace a reusable meal

    Args:
        id (str):
        if_match (str | Unset): The current response body revision in double quotes, such as "4".
            Do not use the GET response ETag or put revision in the body.
        body (SavedMealInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | SavedMeal]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
if_match=if_match,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SavedMealInput,
    if_match: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | SavedMeal | None:
    """ Replace a reusable meal

    Args:
        id (str):
        if_match (str | Unset): The current response body revision in double quotes, such as "4".
            Do not use the GET response ETag or put revision in the body.
        body (SavedMealInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | SavedMeal
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
if_match=if_match,

    )).parsed
