from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.begin_passkey_registration_response_200 import BeginPasskeyRegistrationResponse200
from typing import cast



def _get_kwargs(
    *,
    x_csrf_token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-CSRF-Token"] = x_csrf_token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/account/passkeys/register/begin",
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | BeginPasskeyRegistrationResponse200:
    if response.status_code == 200:
        response_200 = BeginPasskeyRegistrationResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = AccountProblem.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | BeginPasskeyRegistrationResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_csrf_token: str,

) -> Response[AccountProblem | BeginPasskeyRegistrationResponse200]:
    """ Begin passkey registration

     Requests a discoverable, user-verified credential. Requires recent authentication. Browser session
    authentication and CSRF apply to protected mutations. Recent authentication means a session created
    within five minutes. WebAuthn challenges are one-use, browser-bound and expire after five minutes.
    Public sign-in requires the configured Origin header. Responses must not be cached.

    Args:
        x_csrf_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | BeginPasskeyRegistrationResponse200]
     """


    kwargs = _get_kwargs(
        x_csrf_token=x_csrf_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    x_csrf_token: str,

) -> AccountProblem | BeginPasskeyRegistrationResponse200 | None:
    """ Begin passkey registration

     Requests a discoverable, user-verified credential. Requires recent authentication. Browser session
    authentication and CSRF apply to protected mutations. Recent authentication means a session created
    within five minutes. WebAuthn challenges are one-use, browser-bound and expire after five minutes.
    Public sign-in requires the configured Origin header. Responses must not be cached.

    Args:
        x_csrf_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | BeginPasskeyRegistrationResponse200
     """


    return sync_detailed(
        client=client,
x_csrf_token=x_csrf_token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_csrf_token: str,

) -> Response[AccountProblem | BeginPasskeyRegistrationResponse200]:
    """ Begin passkey registration

     Requests a discoverable, user-verified credential. Requires recent authentication. Browser session
    authentication and CSRF apply to protected mutations. Recent authentication means a session created
    within five minutes. WebAuthn challenges are one-use, browser-bound and expire after five minutes.
    Public sign-in requires the configured Origin header. Responses must not be cached.

    Args:
        x_csrf_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | BeginPasskeyRegistrationResponse200]
     """


    kwargs = _get_kwargs(
        x_csrf_token=x_csrf_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    x_csrf_token: str,

) -> AccountProblem | BeginPasskeyRegistrationResponse200 | None:
    """ Begin passkey registration

     Requests a discoverable, user-verified credential. Requires recent authentication. Browser session
    authentication and CSRF apply to protected mutations. Recent authentication means a session created
    within five minutes. WebAuthn challenges are one-use, browser-bound and expire after five minutes.
    Public sign-in requires the configured Origin header. Responses must not be cached.

    Args:
        x_csrf_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | BeginPasskeyRegistrationResponse200
     """


    return (await asyncio_detailed(
        client=client,
x_csrf_token=x_csrf_token,

    )).parsed
