from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.assistant_connections_response import AssistantConnectionsResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/account/connections",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | AssistantConnectionsResponse:
    if response.status_code == 200:
        response_200 = AssistantConnectionsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = AccountProblem.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | AssistantConnectionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | AssistantConnectionsResponse]:
    """ List connected assistants

     Lists current grants without credentials. Refreshing access does not add another connection. Uses
    the persisted local-mode user when authentication is disabled. Otherwise an authenticated browser
    session is required, except for the current account and sign-in. Modifying authenticated requests
    require the current X-CSRF-Token. Credentials and responses must not be cached.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | AssistantConnectionsResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | AssistantConnectionsResponse | None:
    """ List connected assistants

     Lists current grants without credentials. Refreshing access does not add another connection. Uses
    the persisted local-mode user when authentication is disabled. Otherwise an authenticated browser
    session is required, except for the current account and sign-in. Modifying authenticated requests
    require the current X-CSRF-Token. Credentials and responses must not be cached.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | AssistantConnectionsResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | AssistantConnectionsResponse]:
    """ List connected assistants

     Lists current grants without credentials. Refreshing access does not add another connection. Uses
    the persisted local-mode user when authentication is disabled. Otherwise an authenticated browser
    session is required, except for the current account and sign-in. Modifying authenticated requests
    require the current X-CSRF-Token. Credentials and responses must not be cached.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | AssistantConnectionsResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | AssistantConnectionsResponse | None:
    """ List connected assistants

     Lists current grants without credentials. Refreshing access does not add another connection. Uses
    the persisted local-mode user when authentication is disabled. Otherwise an authenticated browser
    session is required, except for the current account and sign-in. Modifying authenticated requests
    require the current X-CSRF-Token. Credentials and responses must not be cached.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | AssistantConnectionsResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
