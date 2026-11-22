from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.credential_login_response import CredentialLoginResponse
from ...models.finish_passkey_login_body import FinishPasskeyLoginBody
from typing import cast



def _get_kwargs(
    *,
    body: FinishPasskeyLoginBody,
    origin: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/account/passkeys/login/finish",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | CredentialLoginResponse:
    if response.status_code == 200:
        response_200 = CredentialLoginResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = AccountProblem.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | CredentialLoginResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FinishPasskeyLoginBody,
    origin: str,

) -> Response[AccountProblem | CredentialLoginResponse]:
    """ Finish passkey sign-in

     Verifies the assertion and rotates the browser session. Browser session authentication and CSRF
    apply to protected mutations. Recent authentication means a session created within five minutes.
    WebAuthn challenges are one-use, browser-bound and expire after five minutes. Public sign-in
    requires the configured Origin header. Responses must not be cached.

    Args:
        origin (str):
        body (FinishPasskeyLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | CredentialLoginResponse]
     """


    kwargs = _get_kwargs(
        body=body,
origin=origin,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: FinishPasskeyLoginBody,
    origin: str,

) -> AccountProblem | CredentialLoginResponse | None:
    """ Finish passkey sign-in

     Verifies the assertion and rotates the browser session. Browser session authentication and CSRF
    apply to protected mutations. Recent authentication means a session created within five minutes.
    WebAuthn challenges are one-use, browser-bound and expire after five minutes. Public sign-in
    requires the configured Origin header. Responses must not be cached.

    Args:
        origin (str):
        body (FinishPasskeyLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | CredentialLoginResponse
     """


    return sync_detailed(
        client=client,
body=body,
origin=origin,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FinishPasskeyLoginBody,
    origin: str,

) -> Response[AccountProblem | CredentialLoginResponse]:
    """ Finish passkey sign-in

     Verifies the assertion and rotates the browser session. Browser session authentication and CSRF
    apply to protected mutations. Recent authentication means a session created within five minutes.
    WebAuthn challenges are one-use, browser-bound and expire after five minutes. Public sign-in
    requires the configured Origin header. Responses must not be cached.

    Args:
        origin (str):
        body (FinishPasskeyLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | CredentialLoginResponse]
     """


    kwargs = _get_kwargs(
        body=body,
origin=origin,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FinishPasskeyLoginBody,
    origin: str,

) -> AccountProblem | CredentialLoginResponse | None:
    """ Finish passkey sign-in

     Verifies the assertion and rotates the browser session. Browser session authentication and CSRF
    apply to protected mutations. Recent authentication means a session created within five minutes.
    WebAuthn challenges are one-use, browser-bound and expire after five minutes. Public sign-in
    requires the configured Origin header. Responses must not be cached.

    Args:
        origin (str):
        body (FinishPasskeyLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | CredentialLoginResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
origin=origin,

    )).parsed
