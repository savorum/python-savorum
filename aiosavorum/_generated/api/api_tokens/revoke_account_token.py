from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.revoke_account_token_response_200 import RevokeAccountTokenResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    x_csrf_token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_csrf_token, Unset):
        headers["X-CSRF-Token"] = x_csrf_token



    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/account/tokens/{id}".format(id=quote(str(id), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | RevokeAccountTokenResponse200:
    if response.status_code == 200:
        response_200 = RevokeAccountTokenResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = AccountProblem.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | RevokeAccountTokenResponse200]:
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
    x_csrf_token: str | Unset = UNSET,

) -> Response[AccountProblem | RevokeAccountTokenResponse200]:
    """ Revoke an API token

     Takes effect immediately; the token is not reissued. Uses the persisted local-mode user when
    authentication is disabled. Otherwise an authenticated browser session is required, except for the
    current account and sign-in. Modifying authenticated requests require the current X-CSRF-Token.
    Credentials and responses must not be cached.

    Args:
        id (str):
        x_csrf_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | RevokeAccountTokenResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
x_csrf_token=x_csrf_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    x_csrf_token: str | Unset = UNSET,

) -> AccountProblem | RevokeAccountTokenResponse200 | None:
    """ Revoke an API token

     Takes effect immediately; the token is not reissued. Uses the persisted local-mode user when
    authentication is disabled. Otherwise an authenticated browser session is required, except for the
    current account and sign-in. Modifying authenticated requests require the current X-CSRF-Token.
    Credentials and responses must not be cached.

    Args:
        id (str):
        x_csrf_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | RevokeAccountTokenResponse200
     """


    return sync_detailed(
        id=id,
client=client,
x_csrf_token=x_csrf_token,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    x_csrf_token: str | Unset = UNSET,

) -> Response[AccountProblem | RevokeAccountTokenResponse200]:
    """ Revoke an API token

     Takes effect immediately; the token is not reissued. Uses the persisted local-mode user when
    authentication is disabled. Otherwise an authenticated browser session is required, except for the
    current account and sign-in. Modifying authenticated requests require the current X-CSRF-Token.
    Credentials and responses must not be cached.

    Args:
        id (str):
        x_csrf_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | RevokeAccountTokenResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
x_csrf_token=x_csrf_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    x_csrf_token: str | Unset = UNSET,

) -> AccountProblem | RevokeAccountTokenResponse200 | None:
    """ Revoke an API token

     Takes effect immediately; the token is not reissued. Uses the persisted local-mode user when
    authentication is disabled. Otherwise an authenticated browser session is required, except for the
    current account and sign-in. Modifying authenticated requests require the current X-CSRF-Token.
    Credentials and responses must not be cached.

    Args:
        id (str):
        x_csrf_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | RevokeAccountTokenResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
x_csrf_token=x_csrf_token,

    )).parsed
