from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.finish_passkey_registration_body import FinishPasskeyRegistrationBody
from ...models.finish_passkey_registration_response_200 import FinishPasskeyRegistrationResponse200
from typing import cast



def _get_kwargs(
    *,
    body: FinishPasskeyRegistrationBody,
    name: str,
    x_csrf_token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-CSRF-Token"] = x_csrf_token



    

    params: dict[str, Any] = {}

    params["name"] = name


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/account/passkeys/register/finish",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | FinishPasskeyRegistrationResponse200:
    if response.status_code == 200:
        response_200 = FinishPasskeyRegistrationResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = AccountProblem.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | FinishPasskeyRegistrationResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FinishPasskeyRegistrationBody,
    name: str,
    x_csrf_token: str,

) -> Response[AccountProblem | FinishPasskeyRegistrationResponse200]:
    """ Finish passkey registration

     Verifies the creation response and stores only public material. Browser session authentication and
    CSRF apply to protected mutations. Recent authentication means a session created within five
    minutes. WebAuthn challenges are one-use, browser-bound and expire after five minutes. Public sign-
    in requires the configured Origin header. Responses must not be cached.

    Args:
        name (str):
        x_csrf_token (str):
        body (FinishPasskeyRegistrationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | FinishPasskeyRegistrationResponse200]
     """


    kwargs = _get_kwargs(
        body=body,
name=name,
x_csrf_token=x_csrf_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: FinishPasskeyRegistrationBody,
    name: str,
    x_csrf_token: str,

) -> AccountProblem | FinishPasskeyRegistrationResponse200 | None:
    """ Finish passkey registration

     Verifies the creation response and stores only public material. Browser session authentication and
    CSRF apply to protected mutations. Recent authentication means a session created within five
    minutes. WebAuthn challenges are one-use, browser-bound and expire after five minutes. Public sign-
    in requires the configured Origin header. Responses must not be cached.

    Args:
        name (str):
        x_csrf_token (str):
        body (FinishPasskeyRegistrationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | FinishPasskeyRegistrationResponse200
     """


    return sync_detailed(
        client=client,
body=body,
name=name,
x_csrf_token=x_csrf_token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FinishPasskeyRegistrationBody,
    name: str,
    x_csrf_token: str,

) -> Response[AccountProblem | FinishPasskeyRegistrationResponse200]:
    """ Finish passkey registration

     Verifies the creation response and stores only public material. Browser session authentication and
    CSRF apply to protected mutations. Recent authentication means a session created within five
    minutes. WebAuthn challenges are one-use, browser-bound and expire after five minutes. Public sign-
    in requires the configured Origin header. Responses must not be cached.

    Args:
        name (str):
        x_csrf_token (str):
        body (FinishPasskeyRegistrationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | FinishPasskeyRegistrationResponse200]
     """


    kwargs = _get_kwargs(
        body=body,
name=name,
x_csrf_token=x_csrf_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FinishPasskeyRegistrationBody,
    name: str,
    x_csrf_token: str,

) -> AccountProblem | FinishPasskeyRegistrationResponse200 | None:
    """ Finish passkey registration

     Verifies the creation response and stores only public material. Browser session authentication and
    CSRF apply to protected mutations. Recent authentication means a session created within five
    minutes. WebAuthn challenges are one-use, browser-bound and expire after five minutes. Public sign-
    in requires the configured Origin header. Responses must not be cached.

    Args:
        name (str):
        x_csrf_token (str):
        body (FinishPasskeyRegistrationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | FinishPasskeyRegistrationResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,
name=name,
x_csrf_token=x_csrf_token,

    )).parsed
