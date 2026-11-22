from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.shopping_activity_output_body import ShoppingActivityOutputBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    list_id: str,
    *,
    before: int | Unset = UNSET,
    limit: int | Unset = 50,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_savorum_library, Unset):
        headers["X-Savorum-Library"] = x_savorum_library

    if not isinstance(x_savorum_principal, Unset):
        headers["X-Savorum-Principal"] = x_savorum_principal



    

    params: dict[str, Any] = {}

    params["before"] = before

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/shopping/lists/{list_id}/activity".format(list_id=quote(str(list_id), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | ShoppingActivityOutputBody:
    if response.status_code == 200:
        response_200 = ShoppingActivityOutputBody.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = ErrorModel.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | ShoppingActivityOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    before: int | Unset = UNSET,
    limit: int | Unset = 50,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | ShoppingActivityOutputBody]:
    """ List shopping list activity

    Args:
        list_id (str):
        before (int | Unset): Return entries older than this entry identity
        limit (int | Unset):  Default: 50.
        x_savorum_library (str | Unset):
        x_savorum_principal (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ShoppingActivityOutputBody]
     """


    kwargs = _get_kwargs(
        list_id=list_id,
before=before,
limit=limit,
x_savorum_library=x_savorum_library,
x_savorum_principal=x_savorum_principal,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    before: int | Unset = UNSET,
    limit: int | Unset = 50,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | ShoppingActivityOutputBody | None:
    """ List shopping list activity

    Args:
        list_id (str):
        before (int | Unset): Return entries older than this entry identity
        limit (int | Unset):  Default: 50.
        x_savorum_library (str | Unset):
        x_savorum_principal (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ShoppingActivityOutputBody
     """


    return sync_detailed(
        list_id=list_id,
client=client,
before=before,
limit=limit,
x_savorum_library=x_savorum_library,
x_savorum_principal=x_savorum_principal,

    ).parsed

async def asyncio_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    before: int | Unset = UNSET,
    limit: int | Unset = 50,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | ShoppingActivityOutputBody]:
    """ List shopping list activity

    Args:
        list_id (str):
        before (int | Unset): Return entries older than this entry identity
        limit (int | Unset):  Default: 50.
        x_savorum_library (str | Unset):
        x_savorum_principal (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ShoppingActivityOutputBody]
     """


    kwargs = _get_kwargs(
        list_id=list_id,
before=before,
limit=limit,
x_savorum_library=x_savorum_library,
x_savorum_principal=x_savorum_principal,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    before: int | Unset = UNSET,
    limit: int | Unset = 50,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | ShoppingActivityOutputBody | None:
    """ List shopping list activity

    Args:
        list_id (str):
        before (int | Unset): Return entries older than this entry identity
        limit (int | Unset):  Default: 50.
        x_savorum_library (str | Unset):
        x_savorum_principal (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ShoppingActivityOutputBody
     """


    return (await asyncio_detailed(
        list_id=list_id,
client=client,
before=before,
limit=limit,
x_savorum_library=x_savorum_library,
x_savorum_principal=x_savorum_principal,

    )).parsed
