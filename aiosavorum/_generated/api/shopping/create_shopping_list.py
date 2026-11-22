from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.shopping_list import ShoppingList
from ...models.shopping_list_input import ShoppingListInput
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: ShoppingListInput,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_savorum_library, Unset):
        headers["X-Savorum-Library"] = x_savorum_library

    if not isinstance(x_savorum_principal, Unset):
        headers["X-Savorum-Principal"] = x_savorum_principal

    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/shopping/lists",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | ShoppingList:
    if response.status_code == 201:
        response_201 = ShoppingList.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 409:
        response_409 = ErrorModel.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = ErrorModel.from_dict(response.json())



        return response_422

    if response.status_code == 429:
        response_429 = ErrorModel.from_dict(response.json())



        return response_429

    if response.status_code == 503:
        response_503 = ErrorModel.from_dict(response.json())



        return response_503

    response_default = ErrorModel.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | ShoppingList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ShoppingListInput,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | ShoppingList]:
    """ Create a named shopping list

     The client chooses the list ID, so a retry with the same ID and name returns the same list. Creation
    accepts Idempotency-Key; reuse it only with the same request. Receipts last at least 24 hours.

    Args:
        x_savorum_library (str | Unset):
        x_savorum_principal (str | Unset):
        idempotency_key (str | Unset):
        body (ShoppingListInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ShoppingList]
     """


    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient | Client,
    body: ShoppingListInput,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | ShoppingList | None:
    """ Create a named shopping list

     The client chooses the list ID, so a retry with the same ID and name returns the same list. Creation
    accepts Idempotency-Key; reuse it only with the same request. Receipts last at least 24 hours.

    Args:
        x_savorum_library (str | Unset):
        x_savorum_principal (str | Unset):
        idempotency_key (str | Unset):
        body (ShoppingListInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ShoppingList
     """


    return sync_detailed(
        client=client,
body=body,
x_savorum_library=x_savorum_library,
x_savorum_principal=x_savorum_principal,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ShoppingListInput,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | ShoppingList]:
    """ Create a named shopping list

     The client chooses the list ID, so a retry with the same ID and name returns the same list. Creation
    accepts Idempotency-Key; reuse it only with the same request. Receipts last at least 24 hours.

    Args:
        x_savorum_library (str | Unset):
        x_savorum_principal (str | Unset):
        idempotency_key (str | Unset):
        body (ShoppingListInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ShoppingList]
     """


    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient | Client,
    body: ShoppingListInput,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | ShoppingList | None:
    """ Create a named shopping list

     The client chooses the list ID, so a retry with the same ID and name returns the same list. Creation
    accepts Idempotency-Key; reuse it only with the same request. Receipts last at least 24 hours.

    Args:
        x_savorum_library (str | Unset):
        x_savorum_principal (str | Unset):
        idempotency_key (str | Unset):
        body (ShoppingListInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ShoppingList
     """


    return (await asyncio_detailed(
        client=client,
body=body,
x_savorum_library=x_savorum_library,
x_savorum_principal=x_savorum_principal,
idempotency_key=idempotency_key,

    )).parsed
