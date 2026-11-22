from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.account_user import AccountUser
from ...models.create_user_request import CreateUserRequest
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: CreateUserRequest,
    x_csrf_token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_csrf_token, Unset):
        headers["X-CSRF-Token"] = x_csrf_token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/users",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | AccountUser:
    if response.status_code == 200:
        response_200 = AccountUser.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = AccountProblem.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | AccountUser]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateUserRequest,
    x_csrf_token: str | Unset = UNSET,

) -> Response[AccountProblem | AccountUser]:
    """ Create a user

     Creates an ordinary local account. Instance administration. Uses the persisted local-mode user when
    authentication is disabled. Otherwise an authenticated browser session is required, except for the
    current account and sign-in. Modifying authenticated requests require the current X-CSRF-Token.
    Credentials and responses must not be cached.

    Args:
        x_csrf_token (str | Unset):
        body (CreateUserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | AccountUser]
     """


    kwargs = _get_kwargs(
        body=body,
x_csrf_token=x_csrf_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateUserRequest,
    x_csrf_token: str | Unset = UNSET,

) -> AccountProblem | AccountUser | None:
    """ Create a user

     Creates an ordinary local account. Instance administration. Uses the persisted local-mode user when
    authentication is disabled. Otherwise an authenticated browser session is required, except for the
    current account and sign-in. Modifying authenticated requests require the current X-CSRF-Token.
    Credentials and responses must not be cached.

    Args:
        x_csrf_token (str | Unset):
        body (CreateUserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | AccountUser
     """


    return sync_detailed(
        client=client,
body=body,
x_csrf_token=x_csrf_token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateUserRequest,
    x_csrf_token: str | Unset = UNSET,

) -> Response[AccountProblem | AccountUser]:
    """ Create a user

     Creates an ordinary local account. Instance administration. Uses the persisted local-mode user when
    authentication is disabled. Otherwise an authenticated browser session is required, except for the
    current account and sign-in. Modifying authenticated requests require the current X-CSRF-Token.
    Credentials and responses must not be cached.

    Args:
        x_csrf_token (str | Unset):
        body (CreateUserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | AccountUser]
     """


    kwargs = _get_kwargs(
        body=body,
x_csrf_token=x_csrf_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateUserRequest,
    x_csrf_token: str | Unset = UNSET,

) -> AccountProblem | AccountUser | None:
    """ Create a user

     Creates an ordinary local account. Instance administration. Uses the persisted local-mode user when
    authentication is disabled. Otherwise an authenticated browser session is required, except for the
    current account and sign-in. Modifying authenticated requests require the current X-CSRF-Token.
    Credentials and responses must not be cached.

    Args:
        x_csrf_token (str | Unset):
        body (CreateUserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | AccountUser
     """


    return (await asyncio_detailed(
        client=client,
body=body,
x_csrf_token=x_csrf_token,

    )).parsed
