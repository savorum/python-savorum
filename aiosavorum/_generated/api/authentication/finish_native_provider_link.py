from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.finish_native_provider_link_body import FinishNativeProviderLinkBody
from ...models.finish_native_provider_link_response_200 import FinishNativeProviderLinkResponse200
from ...models.finish_native_provider_link_response_400 import FinishNativeProviderLinkResponse400
from ...models.finish_native_provider_link_response_401 import FinishNativeProviderLinkResponse401
from ...models.finish_native_provider_link_response_403 import FinishNativeProviderLinkResponse403
from ...models.finish_native_provider_link_response_404 import FinishNativeProviderLinkResponse404
from ...models.finish_native_provider_link_response_409 import FinishNativeProviderLinkResponse409
from ...models.finish_native_provider_link_response_429 import FinishNativeProviderLinkResponse429
from ...models.finish_native_provider_link_response_500 import FinishNativeProviderLinkResponse500
from typing import cast



def _get_kwargs(
    *,
    body: FinishNativeProviderLinkBody,
    origin: str,
    x_csrf_token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    headers["X-CSRF-Token"] = x_csrf_token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/auth/native-links",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> FinishNativeProviderLinkResponse200 | FinishNativeProviderLinkResponse400 | FinishNativeProviderLinkResponse401 | FinishNativeProviderLinkResponse403 | FinishNativeProviderLinkResponse404 | FinishNativeProviderLinkResponse409 | FinishNativeProviderLinkResponse429 | FinishNativeProviderLinkResponse500 | None:
    if response.status_code == 200:
        response_200 = FinishNativeProviderLinkResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = FinishNativeProviderLinkResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = FinishNativeProviderLinkResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = FinishNativeProviderLinkResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = FinishNativeProviderLinkResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = FinishNativeProviderLinkResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 429:
        response_429 = FinishNativeProviderLinkResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = FinishNativeProviderLinkResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[FinishNativeProviderLinkResponse200 | FinishNativeProviderLinkResponse400 | FinishNativeProviderLinkResponse401 | FinishNativeProviderLinkResponse403 | FinishNativeProviderLinkResponse404 | FinishNativeProviderLinkResponse409 | FinishNativeProviderLinkResponse429 | FinishNativeProviderLinkResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FinishNativeProviderLinkBody,
    origin: str,
    x_csrf_token: str,

) -> Response[FinishNativeProviderLinkResponse200 | FinishNativeProviderLinkResponse400 | FinishNativeProviderLinkResponse401 | FinishNativeProviderLinkResponse403 | FinishNativeProviderLinkResponse404 | FinishNativeProviderLinkResponse409 | FinishNativeProviderLinkResponse429 | FinishNativeProviderLinkResponse500]:
    """ Finish a native link

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        origin (str):
        x_csrf_token (str):
        body (FinishNativeProviderLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinishNativeProviderLinkResponse200 | FinishNativeProviderLinkResponse400 | FinishNativeProviderLinkResponse401 | FinishNativeProviderLinkResponse403 | FinishNativeProviderLinkResponse404 | FinishNativeProviderLinkResponse409 | FinishNativeProviderLinkResponse429 | FinishNativeProviderLinkResponse500]
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
    body: FinishNativeProviderLinkBody,
    origin: str,
    x_csrf_token: str,

) -> FinishNativeProviderLinkResponse200 | FinishNativeProviderLinkResponse400 | FinishNativeProviderLinkResponse401 | FinishNativeProviderLinkResponse403 | FinishNativeProviderLinkResponse404 | FinishNativeProviderLinkResponse409 | FinishNativeProviderLinkResponse429 | FinishNativeProviderLinkResponse500 | None:
    """ Finish a native link

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        origin (str):
        x_csrf_token (str):
        body (FinishNativeProviderLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinishNativeProviderLinkResponse200 | FinishNativeProviderLinkResponse400 | FinishNativeProviderLinkResponse401 | FinishNativeProviderLinkResponse403 | FinishNativeProviderLinkResponse404 | FinishNativeProviderLinkResponse409 | FinishNativeProviderLinkResponse429 | FinishNativeProviderLinkResponse500
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
    body: FinishNativeProviderLinkBody,
    origin: str,
    x_csrf_token: str,

) -> Response[FinishNativeProviderLinkResponse200 | FinishNativeProviderLinkResponse400 | FinishNativeProviderLinkResponse401 | FinishNativeProviderLinkResponse403 | FinishNativeProviderLinkResponse404 | FinishNativeProviderLinkResponse409 | FinishNativeProviderLinkResponse429 | FinishNativeProviderLinkResponse500]:
    """ Finish a native link

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        origin (str):
        x_csrf_token (str):
        body (FinishNativeProviderLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinishNativeProviderLinkResponse200 | FinishNativeProviderLinkResponse400 | FinishNativeProviderLinkResponse401 | FinishNativeProviderLinkResponse403 | FinishNativeProviderLinkResponse404 | FinishNativeProviderLinkResponse409 | FinishNativeProviderLinkResponse429 | FinishNativeProviderLinkResponse500]
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
    body: FinishNativeProviderLinkBody,
    origin: str,
    x_csrf_token: str,

) -> FinishNativeProviderLinkResponse200 | FinishNativeProviderLinkResponse400 | FinishNativeProviderLinkResponse401 | FinishNativeProviderLinkResponse403 | FinishNativeProviderLinkResponse404 | FinishNativeProviderLinkResponse409 | FinishNativeProviderLinkResponse429 | FinishNativeProviderLinkResponse500 | None:
    """ Finish a native link

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        origin (str):
        x_csrf_token (str):
        body (FinishNativeProviderLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinishNativeProviderLinkResponse200 | FinishNativeProviderLinkResponse400 | FinishNativeProviderLinkResponse401 | FinishNativeProviderLinkResponse403 | FinishNativeProviderLinkResponse404 | FinishNativeProviderLinkResponse409 | FinishNativeProviderLinkResponse429 | FinishNativeProviderLinkResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,
origin=origin,
x_csrf_token=x_csrf_token,

    )).parsed
