from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.create_grocery_items_request import CreateGroceryItemsRequest
from ...models.error_model import ErrorModel
from ...models.shopping_list import ShoppingList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    list_id: str,
    *,
    body: CreateGroceryItemsRequest,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,
    idempotency_key: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_savorum_library, Unset):
        headers["X-Savorum-Library"] = x_savorum_library

    if not isinstance(x_savorum_principal, Unset):
        headers["X-Savorum-Principal"] = x_savorum_principal

    headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/shopping/lists/{list_id}/items".format(list_id=quote(str(list_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | ShoppingList | None:
    if response.status_code == 200:
        response_200 = ShoppingList.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = ErrorModel.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = ErrorModel.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = ErrorModel.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = ErrorModel.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | ShoppingList]:
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
    body: CreateGroceryItemsRequest,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,
    idempotency_key: str,

) -> Response[AccountProblem | ErrorModel | ShoppingList]:
    """ Add groceries atomically

    Args:
        list_id (str):
        x_savorum_library (str | Unset):
        x_savorum_principal (str | Unset):
        idempotency_key (str):
        body (CreateGroceryItemsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ShoppingList]
     """


    kwargs = _get_kwargs(
        list_id=list_id,
body=body,
x_savorum_library=x_savorum_library,
x_savorum_principal=x_savorum_principal,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateGroceryItemsRequest,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,
    idempotency_key: str,

) -> AccountProblem | ErrorModel | ShoppingList | None:
    """ Add groceries atomically

    Args:
        list_id (str):
        x_savorum_library (str | Unset):
        x_savorum_principal (str | Unset):
        idempotency_key (str):
        body (CreateGroceryItemsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ShoppingList
     """


    return sync_detailed(
        list_id=list_id,
client=client,
body=body,
x_savorum_library=x_savorum_library,
x_savorum_principal=x_savorum_principal,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateGroceryItemsRequest,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,
    idempotency_key: str,

) -> Response[AccountProblem | ErrorModel | ShoppingList]:
    """ Add groceries atomically

    Args:
        list_id (str):
        x_savorum_library (str | Unset):
        x_savorum_principal (str | Unset):
        idempotency_key (str):
        body (CreateGroceryItemsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ShoppingList]
     """


    kwargs = _get_kwargs(
        list_id=list_id,
body=body,
x_savorum_library=x_savorum_library,
x_savorum_principal=x_savorum_principal,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateGroceryItemsRequest,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,
    idempotency_key: str,

) -> AccountProblem | ErrorModel | ShoppingList | None:
    """ Add groceries atomically

    Args:
        list_id (str):
        x_savorum_library (str | Unset):
        x_savorum_principal (str | Unset):
        idempotency_key (str):
        body (CreateGroceryItemsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ShoppingList
     """


    return (await asyncio_detailed(
        list_id=list_id,
client=client,
body=body,
x_savorum_library=x_savorum_library,
x_savorum_principal=x_savorum_principal,
idempotency_key=idempotency_key,

    )).parsed
