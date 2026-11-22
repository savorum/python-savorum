from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.members_response import MembersResponse
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/libraries/{id}/members".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | MembersResponse:
    if response.status_code == 200:
        response_200 = MembersResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = AccountProblem.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | MembersResponse]:
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

) -> Response[AccountProblem | MembersResponse]:
    """ List library members

     Library ownership required. Uses the persisted local-mode user when authentication is disabled.
    Otherwise an authenticated browser session is required, except for the current account and sign-in.
    Modifying authenticated requests require the current X-CSRF-Token. Credentials and responses must
    not be cached.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | MembersResponse]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | MembersResponse | None:
    """ List library members

     Library ownership required. Uses the persisted local-mode user when authentication is disabled.
    Otherwise an authenticated browser session is required, except for the current account and sign-in.
    Modifying authenticated requests require the current X-CSRF-Token. Credentials and responses must
    not be cached.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | MembersResponse
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | MembersResponse]:
    """ List library members

     Library ownership required. Uses the persisted local-mode user when authentication is disabled.
    Otherwise an authenticated browser session is required, except for the current account and sign-in.
    Modifying authenticated requests require the current X-CSRF-Token. Credentials and responses must
    not be cached.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | MembersResponse]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | MembersResponse | None:
    """ List library members

     Library ownership required. Uses the persisted local-mode user when authentication is disabled.
    Otherwise an authenticated browser session is required, except for the current account and sign-in.
    Modifying authenticated requests require the current X-CSRF-Token. Credentials and responses must
    not be cached.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | MembersResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
