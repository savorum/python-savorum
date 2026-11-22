from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.delivery import Delivery
from ...models.error_model import ErrorModel
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 25,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/instance-webhooks/{id}/deliveries".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | list[Delivery] | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> list[Delivery] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = []
                _response_200_type_0 = data
                for response_200_type_0_item_data in (_response_200_type_0):
                    response_200_type_0_item = Delivery.from_dict(response_200_type_0_item_data)



                    response_200_type_0.append(response_200_type_0_item)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Delivery] | None, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = ErrorModel.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | list[Delivery] | None]:
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
    offset: int | Unset = 0,
    limit: int | Unset = 25,

) -> Response[AccountProblem | ErrorModel | list[Delivery] | None]:
    """ List instance deliveries

    Args:
        id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | list[Delivery] | None]
     """


    kwargs = _get_kwargs(
        id=id,
offset=offset,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 25,

) -> AccountProblem | ErrorModel | list[Delivery] | None | None:
    """ List instance deliveries

    Args:
        id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | list[Delivery] | None
     """


    return sync_detailed(
        id=id,
client=client,
offset=offset,
limit=limit,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 25,

) -> Response[AccountProblem | ErrorModel | list[Delivery] | None]:
    """ List instance deliveries

    Args:
        id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | list[Delivery] | None]
     """


    kwargs = _get_kwargs(
        id=id,
offset=offset,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 25,

) -> AccountProblem | ErrorModel | list[Delivery] | None | None:
    """ List instance deliveries

    Args:
        id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | list[Delivery] | None
     """


    return (await asyncio_detailed(
        id=id,
client=client,
offset=offset,
limit=limit,

    )).parsed
