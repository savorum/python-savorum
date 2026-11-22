from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.rename_passkey_body import RenamePasskeyBody
from ...models.rename_passkey_response_200 import RenamePasskeyResponse200
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: RenamePasskeyBody,
    x_csrf_token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-CSRF-Token"] = x_csrf_token



    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/account/passkeys/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | RenamePasskeyResponse200:
    if response.status_code == 200:
        response_200 = RenamePasskeyResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = AccountProblem.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | RenamePasskeyResponse200]:
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
    body: RenamePasskeyBody,
    x_csrf_token: str,

) -> Response[AccountProblem | RenamePasskeyResponse200]:
    """ Rename a passkey

     Requires recent authentication. Browser session authentication and CSRF apply to protected
    mutations. Recent authentication means a session created within five minutes. WebAuthn challenges
    are one-use, browser-bound and expire after five minutes. Public sign-in requires the configured
    Origin header. Responses must not be cached.

    Args:
        id (str):
        x_csrf_token (str):
        body (RenamePasskeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | RenamePasskeyResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
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
    body: RenamePasskeyBody,
    x_csrf_token: str,

) -> AccountProblem | RenamePasskeyResponse200 | None:
    """ Rename a passkey

     Requires recent authentication. Browser session authentication and CSRF apply to protected
    mutations. Recent authentication means a session created within five minutes. WebAuthn challenges
    are one-use, browser-bound and expire after five minutes. Public sign-in requires the configured
    Origin header. Responses must not be cached.

    Args:
        id (str):
        x_csrf_token (str):
        body (RenamePasskeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | RenamePasskeyResponse200
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
x_csrf_token=x_csrf_token,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RenamePasskeyBody,
    x_csrf_token: str,

) -> Response[AccountProblem | RenamePasskeyResponse200]:
    """ Rename a passkey

     Requires recent authentication. Browser session authentication and CSRF apply to protected
    mutations. Recent authentication means a session created within five minutes. WebAuthn challenges
    are one-use, browser-bound and expire after five minutes. Public sign-in requires the configured
    Origin header. Responses must not be cached.

    Args:
        id (str):
        x_csrf_token (str):
        body (RenamePasskeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | RenamePasskeyResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
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
    body: RenamePasskeyBody,
    x_csrf_token: str,

) -> AccountProblem | RenamePasskeyResponse200 | None:
    """ Rename a passkey

     Requires recent authentication. Browser session authentication and CSRF apply to protected
    mutations. Recent authentication means a session created within five minutes. WebAuthn challenges
    are one-use, browser-bound and expire after five minutes. Public sign-in requires the configured
    Origin header. Responses must not be cached.

    Args:
        id (str):
        x_csrf_token (str):
        body (RenamePasskeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | RenamePasskeyResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
x_csrf_token=x_csrf_token,

    )).parsed
