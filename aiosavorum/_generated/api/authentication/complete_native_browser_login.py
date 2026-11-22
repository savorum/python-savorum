from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.complete_native_browser_login_body import CompleteNativeBrowserLoginBody
from ...models.complete_native_browser_login_response_200 import CompleteNativeBrowserLoginResponse200
from ...models.complete_native_browser_login_response_400 import CompleteNativeBrowserLoginResponse400
from ...models.complete_native_browser_login_response_401 import CompleteNativeBrowserLoginResponse401
from ...models.complete_native_browser_login_response_403 import CompleteNativeBrowserLoginResponse403
from ...models.complete_native_browser_login_response_404 import CompleteNativeBrowserLoginResponse404
from ...models.complete_native_browser_login_response_429 import CompleteNativeBrowserLoginResponse429
from ...models.complete_native_browser_login_response_500 import CompleteNativeBrowserLoginResponse500
from typing import cast



def _get_kwargs(
    *,
    body: CompleteNativeBrowserLoginBody,
    origin: str,
    x_csrf_token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    headers["X-CSRF-Token"] = x_csrf_token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/auth/native-browser/finish",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> CompleteNativeBrowserLoginResponse200 | CompleteNativeBrowserLoginResponse400 | CompleteNativeBrowserLoginResponse401 | CompleteNativeBrowserLoginResponse403 | CompleteNativeBrowserLoginResponse404 | CompleteNativeBrowserLoginResponse429 | CompleteNativeBrowserLoginResponse500 | None:
    if response.status_code == 200:
        response_200 = CompleteNativeBrowserLoginResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = CompleteNativeBrowserLoginResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = CompleteNativeBrowserLoginResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = CompleteNativeBrowserLoginResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = CompleteNativeBrowserLoginResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = CompleteNativeBrowserLoginResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = CompleteNativeBrowserLoginResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[CompleteNativeBrowserLoginResponse200 | CompleteNativeBrowserLoginResponse400 | CompleteNativeBrowserLoginResponse401 | CompleteNativeBrowserLoginResponse403 | CompleteNativeBrowserLoginResponse404 | CompleteNativeBrowserLoginResponse429 | CompleteNativeBrowserLoginResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CompleteNativeBrowserLoginBody,
    origin: str,
    x_csrf_token: str,

) -> Response[CompleteNativeBrowserLoginResponse200 | CompleteNativeBrowserLoginResponse400 | CompleteNativeBrowserLoginResponse401 | CompleteNativeBrowserLoginResponse403 | CompleteNativeBrowserLoginResponse404 | CompleteNativeBrowserLoginResponse429 | CompleteNativeBrowserLoginResponse500]:
    """ Return sign-in to the app

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        origin (str):
        x_csrf_token (str):
        body (CompleteNativeBrowserLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompleteNativeBrowserLoginResponse200 | CompleteNativeBrowserLoginResponse400 | CompleteNativeBrowserLoginResponse401 | CompleteNativeBrowserLoginResponse403 | CompleteNativeBrowserLoginResponse404 | CompleteNativeBrowserLoginResponse429 | CompleteNativeBrowserLoginResponse500]
     """


    kwargs = _get_kwargs(
        body=body,
origin=origin,
x_csrf_token=x_csrf_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CompleteNativeBrowserLoginBody,
    origin: str,
    x_csrf_token: str,

) -> CompleteNativeBrowserLoginResponse200 | CompleteNativeBrowserLoginResponse400 | CompleteNativeBrowserLoginResponse401 | CompleteNativeBrowserLoginResponse403 | CompleteNativeBrowserLoginResponse404 | CompleteNativeBrowserLoginResponse429 | CompleteNativeBrowserLoginResponse500 | None:
    """ Return sign-in to the app

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        origin (str):
        x_csrf_token (str):
        body (CompleteNativeBrowserLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompleteNativeBrowserLoginResponse200 | CompleteNativeBrowserLoginResponse400 | CompleteNativeBrowserLoginResponse401 | CompleteNativeBrowserLoginResponse403 | CompleteNativeBrowserLoginResponse404 | CompleteNativeBrowserLoginResponse429 | CompleteNativeBrowserLoginResponse500
     """


    return sync_detailed(
        client=client,
body=body,
origin=origin,
x_csrf_token=x_csrf_token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CompleteNativeBrowserLoginBody,
    origin: str,
    x_csrf_token: str,

) -> Response[CompleteNativeBrowserLoginResponse200 | CompleteNativeBrowserLoginResponse400 | CompleteNativeBrowserLoginResponse401 | CompleteNativeBrowserLoginResponse403 | CompleteNativeBrowserLoginResponse404 | CompleteNativeBrowserLoginResponse429 | CompleteNativeBrowserLoginResponse500]:
    """ Return sign-in to the app

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        origin (str):
        x_csrf_token (str):
        body (CompleteNativeBrowserLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompleteNativeBrowserLoginResponse200 | CompleteNativeBrowserLoginResponse400 | CompleteNativeBrowserLoginResponse401 | CompleteNativeBrowserLoginResponse403 | CompleteNativeBrowserLoginResponse404 | CompleteNativeBrowserLoginResponse429 | CompleteNativeBrowserLoginResponse500]
     """


    kwargs = _get_kwargs(
        body=body,
origin=origin,
x_csrf_token=x_csrf_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CompleteNativeBrowserLoginBody,
    origin: str,
    x_csrf_token: str,

) -> CompleteNativeBrowserLoginResponse200 | CompleteNativeBrowserLoginResponse400 | CompleteNativeBrowserLoginResponse401 | CompleteNativeBrowserLoginResponse403 | CompleteNativeBrowserLoginResponse404 | CompleteNativeBrowserLoginResponse429 | CompleteNativeBrowserLoginResponse500 | None:
    """ Return sign-in to the app

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        origin (str):
        x_csrf_token (str):
        body (CompleteNativeBrowserLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompleteNativeBrowserLoginResponse200 | CompleteNativeBrowserLoginResponse400 | CompleteNativeBrowserLoginResponse401 | CompleteNativeBrowserLoginResponse403 | CompleteNativeBrowserLoginResponse404 | CompleteNativeBrowserLoginResponse429 | CompleteNativeBrowserLoginResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,
origin=origin,
x_csrf_token=x_csrf_token,

    )).parsed
