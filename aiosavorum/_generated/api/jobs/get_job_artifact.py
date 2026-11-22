from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from typing import cast



def _get_kwargs(
    id: str,
    handle: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/jobs/{id}/downloads/{handle}".format(id=quote(str(id), safe=""),handle=quote(str(handle), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | None:
    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ErrorModel.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorModel.from_dict(response.json())



        return response_404

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    handle: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | ErrorModel]:
    """ Download an export artifact

     Opaque handle, creator and current library authorization required. No unauthenticated/static
    download URL. Expires 24 hours after job creation.

    Args:
        id (str):
        handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel]
     """


    kwargs = _get_kwargs(
        id=id,
handle=handle,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    handle: str,
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | ErrorModel | None:
    """ Download an export artifact

     Opaque handle, creator and current library authorization required. No unauthenticated/static
    download URL. Expires 24 hours after job creation.

    Args:
        id (str):
        handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel
     """


    return sync_detailed(
        id=id,
handle=handle,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    handle: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | ErrorModel]:
    """ Download an export artifact

     Opaque handle, creator and current library authorization required. No unauthenticated/static
    download URL. Expires 24 hours after job creation.

    Args:
        id (str):
        handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel]
     """


    kwargs = _get_kwargs(
        id=id,
handle=handle,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    handle: str,
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | ErrorModel | None:
    """ Download an export artifact

     Opaque handle, creator and current library authorization required. No unauthenticated/static
    download URL. Expires 24 hours after job creation.

    Args:
        id (str):
        handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel
     """


    return (await asyncio_detailed(
        id=id,
handle=handle,
client=client,

    )).parsed
