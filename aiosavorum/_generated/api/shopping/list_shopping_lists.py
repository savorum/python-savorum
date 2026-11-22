from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.shopping_list_summary import ShoppingListSummary
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_savorum_library, Unset):
        headers["X-Savorum-Library"] = x_savorum_library

    if not isinstance(x_savorum_principal, Unset):
        headers["X-Savorum-Principal"] = x_savorum_principal



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/shopping/lists",
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | list[ShoppingListSummary] | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> list[ShoppingListSummary] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = []
                _response_200_type_0 = data
                for response_200_type_0_item_data in (_response_200_type_0):
                    response_200_type_0_item = ShoppingListSummary.from_dict(response_200_type_0_item_data)



                    response_200_type_0.append(response_200_type_0_item)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ShoppingListSummary] | None, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = ErrorModel.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | list[ShoppingListSummary] | None]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | list[ShoppingListSummary] | None]:
    """ List household shopping lists

    Args:
        x_savorum_library (str | Unset):
        x_savorum_principal (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | list[ShoppingListSummary] | None]
     """


    kwargs = _get_kwargs(
        x_savorum_library=x_savorum_library,
x_savorum_principal=x_savorum_principal,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | list[ShoppingListSummary] | None | None:
    """ List household shopping lists

    Args:
        x_savorum_library (str | Unset):
        x_savorum_principal (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | list[ShoppingListSummary] | None
     """


    return sync_detailed(
        client=client,
x_savorum_library=x_savorum_library,
x_savorum_principal=x_savorum_principal,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | list[ShoppingListSummary] | None]:
    """ List household shopping lists

    Args:
        x_savorum_library (str | Unset):
        x_savorum_principal (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | list[ShoppingListSummary] | None]
     """


    kwargs = _get_kwargs(
        x_savorum_library=x_savorum_library,
x_savorum_principal=x_savorum_principal,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    x_savorum_library: str | Unset = UNSET,
    x_savorum_principal: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | list[ShoppingListSummary] | None | None:
    """ List household shopping lists

    Args:
        x_savorum_library (str | Unset):
        x_savorum_principal (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | list[ShoppingListSummary] | None
     """


    return (await asyncio_detailed(
        client=client,
x_savorum_library=x_savorum_library,
x_savorum_principal=x_savorum_principal,

    )).parsed
