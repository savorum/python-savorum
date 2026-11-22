from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.removed_response import RemovedResponse
from typing import cast



def _get_kwargs(
    id: str,
    method: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/users/{id}/methods/{method}".format(id=quote(str(id), safe=""),method=quote(str(method), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | RemovedResponse:
    if response.status_code == 200:
        response_200 = RemovedResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = AccountProblem.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | RemovedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    method: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | RemovedResponse]:
    """ Force-unlink a sign-in method

     Audited administrator action for a compromised identity. Browser session and CSRF protection are
    required for mutations, except invited local registration and bearer invitation previews. Invitation
    secrets are returned once and must never be logged.

    Args:
        id (str):
        method (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | RemovedResponse]
     """


    kwargs = _get_kwargs(
        id=id,
method=method,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    method: str,
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | RemovedResponse | None:
    """ Force-unlink a sign-in method

     Audited administrator action for a compromised identity. Browser session and CSRF protection are
    required for mutations, except invited local registration and bearer invitation previews. Invitation
    secrets are returned once and must never be logged.

    Args:
        id (str):
        method (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | RemovedResponse
     """


    return sync_detailed(
        id=id,
method=method,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    method: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | RemovedResponse]:
    """ Force-unlink a sign-in method

     Audited administrator action for a compromised identity. Browser session and CSRF protection are
    required for mutations, except invited local registration and bearer invitation previews. Invitation
    secrets are returned once and must never be logged.

    Args:
        id (str):
        method (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | RemovedResponse]
     """


    kwargs = _get_kwargs(
        id=id,
method=method,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    method: str,
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | RemovedResponse | None:
    """ Force-unlink a sign-in method

     Audited administrator action for a compromised identity. Browser session and CSRF protection are
    required for mutations, except invited local registration and bearer invitation previews. Invitation
    secrets are returned once and must never be logged.

    Args:
        id (str):
        method (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | RemovedResponse
     """


    return (await asyncio_detailed(
        id=id,
method=method,
client=client,

    )).parsed
