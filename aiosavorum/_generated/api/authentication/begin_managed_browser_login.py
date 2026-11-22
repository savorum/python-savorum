from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.begin_managed_browser_login_response_400 import BeginManagedBrowserLoginResponse400
from ...models.begin_managed_browser_login_response_401 import BeginManagedBrowserLoginResponse401
from ...models.begin_managed_browser_login_response_403 import BeginManagedBrowserLoginResponse403
from ...models.begin_managed_browser_login_response_404 import BeginManagedBrowserLoginResponse404
from ...models.begin_managed_browser_login_response_429 import BeginManagedBrowserLoginResponse429
from ...models.begin_managed_browser_login_response_500 import BeginManagedBrowserLoginResponse500
from typing import cast



def _get_kwargs(
    provider: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/auth/{provider}/start".format(provider=quote(str(provider), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | BeginManagedBrowserLoginResponse400 | BeginManagedBrowserLoginResponse401 | BeginManagedBrowserLoginResponse403 | BeginManagedBrowserLoginResponse404 | BeginManagedBrowserLoginResponse429 | BeginManagedBrowserLoginResponse500 | None:
    if response.status_code == 303:
        response_303 = cast(Any, None)
        return response_303

    if response.status_code == 400:
        response_400 = BeginManagedBrowserLoginResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = BeginManagedBrowserLoginResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = BeginManagedBrowserLoginResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = BeginManagedBrowserLoginResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = BeginManagedBrowserLoginResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = BeginManagedBrowserLoginResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any | BeginManagedBrowserLoginResponse400 | BeginManagedBrowserLoginResponse401 | BeginManagedBrowserLoginResponse403 | BeginManagedBrowserLoginResponse404 | BeginManagedBrowserLoginResponse429 | BeginManagedBrowserLoginResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | BeginManagedBrowserLoginResponse400 | BeginManagedBrowserLoginResponse401 | BeginManagedBrowserLoginResponse403 | BeginManagedBrowserLoginResponse404 | BeginManagedBrowserLoginResponse429 | BeginManagedBrowserLoginResponse500]:
    """ Open a managed library

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BeginManagedBrowserLoginResponse400 | BeginManagedBrowserLoginResponse401 | BeginManagedBrowserLoginResponse403 | BeginManagedBrowserLoginResponse404 | BeginManagedBrowserLoginResponse429 | BeginManagedBrowserLoginResponse500]
     """


    kwargs = _get_kwargs(
        provider=provider,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    provider: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | BeginManagedBrowserLoginResponse400 | BeginManagedBrowserLoginResponse401 | BeginManagedBrowserLoginResponse403 | BeginManagedBrowserLoginResponse404 | BeginManagedBrowserLoginResponse429 | BeginManagedBrowserLoginResponse500 | None:
    """ Open a managed library

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BeginManagedBrowserLoginResponse400 | BeginManagedBrowserLoginResponse401 | BeginManagedBrowserLoginResponse403 | BeginManagedBrowserLoginResponse404 | BeginManagedBrowserLoginResponse429 | BeginManagedBrowserLoginResponse500
     """


    return sync_detailed(
        provider=provider,
client=client,

    ).parsed

async def asyncio_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | BeginManagedBrowserLoginResponse400 | BeginManagedBrowserLoginResponse401 | BeginManagedBrowserLoginResponse403 | BeginManagedBrowserLoginResponse404 | BeginManagedBrowserLoginResponse429 | BeginManagedBrowserLoginResponse500]:
    """ Open a managed library

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BeginManagedBrowserLoginResponse400 | BeginManagedBrowserLoginResponse401 | BeginManagedBrowserLoginResponse403 | BeginManagedBrowserLoginResponse404 | BeginManagedBrowserLoginResponse429 | BeginManagedBrowserLoginResponse500]
     """


    kwargs = _get_kwargs(
        provider=provider,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    provider: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | BeginManagedBrowserLoginResponse400 | BeginManagedBrowserLoginResponse401 | BeginManagedBrowserLoginResponse403 | BeginManagedBrowserLoginResponse404 | BeginManagedBrowserLoginResponse429 | BeginManagedBrowserLoginResponse500 | None:
    """ Open a managed library

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BeginManagedBrowserLoginResponse400 | BeginManagedBrowserLoginResponse401 | BeginManagedBrowserLoginResponse403 | BeginManagedBrowserLoginResponse404 | BeginManagedBrowserLoginResponse429 | BeginManagedBrowserLoginResponse500
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,

    )).parsed
