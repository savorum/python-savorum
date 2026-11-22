from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.finish_native_provider_login_body import FinishNativeProviderLoginBody
from ...models.finish_native_provider_login_response_200 import FinishNativeProviderLoginResponse200
from ...models.finish_native_provider_login_response_400 import FinishNativeProviderLoginResponse400
from ...models.finish_native_provider_login_response_401 import FinishNativeProviderLoginResponse401
from ...models.finish_native_provider_login_response_403 import FinishNativeProviderLoginResponse403
from ...models.finish_native_provider_login_response_404 import FinishNativeProviderLoginResponse404
from ...models.finish_native_provider_login_response_429 import FinishNativeProviderLoginResponse429
from ...models.finish_native_provider_login_response_500 import FinishNativeProviderLoginResponse500
from typing import cast



def _get_kwargs(
    *,
    body: FinishNativeProviderLoginBody,
    origin: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/auth/native-sessions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> FinishNativeProviderLoginResponse200 | FinishNativeProviderLoginResponse400 | FinishNativeProviderLoginResponse401 | FinishNativeProviderLoginResponse403 | FinishNativeProviderLoginResponse404 | FinishNativeProviderLoginResponse429 | FinishNativeProviderLoginResponse500 | None:
    if response.status_code == 200:
        response_200 = FinishNativeProviderLoginResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = FinishNativeProviderLoginResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = FinishNativeProviderLoginResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = FinishNativeProviderLoginResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = FinishNativeProviderLoginResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = FinishNativeProviderLoginResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = FinishNativeProviderLoginResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[FinishNativeProviderLoginResponse200 | FinishNativeProviderLoginResponse400 | FinishNativeProviderLoginResponse401 | FinishNativeProviderLoginResponse403 | FinishNativeProviderLoginResponse404 | FinishNativeProviderLoginResponse429 | FinishNativeProviderLoginResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FinishNativeProviderLoginBody,
    origin: str,

) -> Response[FinishNativeProviderLoginResponse200 | FinishNativeProviderLoginResponse400 | FinishNativeProviderLoginResponse401 | FinishNativeProviderLoginResponse403 | FinishNativeProviderLoginResponse404 | FinishNativeProviderLoginResponse429 | FinishNativeProviderLoginResponse500]:
    """ Finish a native sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        origin (str):
        body (FinishNativeProviderLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinishNativeProviderLoginResponse200 | FinishNativeProviderLoginResponse400 | FinishNativeProviderLoginResponse401 | FinishNativeProviderLoginResponse403 | FinishNativeProviderLoginResponse404 | FinishNativeProviderLoginResponse429 | FinishNativeProviderLoginResponse500]
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
    body: FinishNativeProviderLoginBody,
    origin: str,

) -> FinishNativeProviderLoginResponse200 | FinishNativeProviderLoginResponse400 | FinishNativeProviderLoginResponse401 | FinishNativeProviderLoginResponse403 | FinishNativeProviderLoginResponse404 | FinishNativeProviderLoginResponse429 | FinishNativeProviderLoginResponse500 | None:
    """ Finish a native sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        origin (str):
        body (FinishNativeProviderLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinishNativeProviderLoginResponse200 | FinishNativeProviderLoginResponse400 | FinishNativeProviderLoginResponse401 | FinishNativeProviderLoginResponse403 | FinishNativeProviderLoginResponse404 | FinishNativeProviderLoginResponse429 | FinishNativeProviderLoginResponse500
     """


    return sync_detailed(
        client=client,
body=body,
origin=origin,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FinishNativeProviderLoginBody,
    origin: str,

) -> Response[FinishNativeProviderLoginResponse200 | FinishNativeProviderLoginResponse400 | FinishNativeProviderLoginResponse401 | FinishNativeProviderLoginResponse403 | FinishNativeProviderLoginResponse404 | FinishNativeProviderLoginResponse429 | FinishNativeProviderLoginResponse500]:
    """ Finish a native sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        origin (str):
        body (FinishNativeProviderLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinishNativeProviderLoginResponse200 | FinishNativeProviderLoginResponse400 | FinishNativeProviderLoginResponse401 | FinishNativeProviderLoginResponse403 | FinishNativeProviderLoginResponse404 | FinishNativeProviderLoginResponse429 | FinishNativeProviderLoginResponse500]
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
    body: FinishNativeProviderLoginBody,
    origin: str,

) -> FinishNativeProviderLoginResponse200 | FinishNativeProviderLoginResponse400 | FinishNativeProviderLoginResponse401 | FinishNativeProviderLoginResponse403 | FinishNativeProviderLoginResponse404 | FinishNativeProviderLoginResponse429 | FinishNativeProviderLoginResponse500 | None:
    """ Finish a native sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        origin (str):
        body (FinishNativeProviderLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinishNativeProviderLoginResponse200 | FinishNativeProviderLoginResponse400 | FinishNativeProviderLoginResponse401 | FinishNativeProviderLoginResponse403 | FinishNativeProviderLoginResponse404 | FinishNativeProviderLoginResponse429 | FinishNativeProviderLoginResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,
origin=origin,

    )).parsed
