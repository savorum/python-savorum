from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.finish_managed_native_login_body import FinishManagedNativeLoginBody
from ...models.finish_managed_native_login_response_200 import FinishManagedNativeLoginResponse200
from ...models.finish_managed_native_login_response_400 import FinishManagedNativeLoginResponse400
from ...models.finish_managed_native_login_response_401 import FinishManagedNativeLoginResponse401
from ...models.finish_managed_native_login_response_403 import FinishManagedNativeLoginResponse403
from ...models.finish_managed_native_login_response_404 import FinishManagedNativeLoginResponse404
from ...models.finish_managed_native_login_response_429 import FinishManagedNativeLoginResponse429
from ...models.finish_managed_native_login_response_500 import FinishManagedNativeLoginResponse500
from typing import cast



def _get_kwargs(
    provider: str,
    *,
    body: FinishManagedNativeLoginBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/auth/{provider}/managed-sessions".format(provider=quote(str(provider), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> FinishManagedNativeLoginResponse200 | FinishManagedNativeLoginResponse400 | FinishManagedNativeLoginResponse401 | FinishManagedNativeLoginResponse403 | FinishManagedNativeLoginResponse404 | FinishManagedNativeLoginResponse429 | FinishManagedNativeLoginResponse500 | None:
    if response.status_code == 200:
        response_200 = FinishManagedNativeLoginResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = FinishManagedNativeLoginResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = FinishManagedNativeLoginResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = FinishManagedNativeLoginResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = FinishManagedNativeLoginResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = FinishManagedNativeLoginResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = FinishManagedNativeLoginResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[FinishManagedNativeLoginResponse200 | FinishManagedNativeLoginResponse400 | FinishManagedNativeLoginResponse401 | FinishManagedNativeLoginResponse403 | FinishManagedNativeLoginResponse404 | FinishManagedNativeLoginResponse429 | FinishManagedNativeLoginResponse500]:
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
    body: FinishManagedNativeLoginBody,

) -> Response[FinishManagedNativeLoginResponse200 | FinishManagedNativeLoginResponse400 | FinishManagedNativeLoginResponse401 | FinishManagedNativeLoginResponse403 | FinishManagedNativeLoginResponse404 | FinishManagedNativeLoginResponse429 | FinishManagedNativeLoginResponse500]:
    """ Redeem a managed session grant

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        body (FinishManagedNativeLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinishManagedNativeLoginResponse200 | FinishManagedNativeLoginResponse400 | FinishManagedNativeLoginResponse401 | FinishManagedNativeLoginResponse403 | FinishManagedNativeLoginResponse404 | FinishManagedNativeLoginResponse429 | FinishManagedNativeLoginResponse500]
     """


    kwargs = _get_kwargs(
        provider=provider,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: FinishManagedNativeLoginBody,

) -> FinishManagedNativeLoginResponse200 | FinishManagedNativeLoginResponse400 | FinishManagedNativeLoginResponse401 | FinishManagedNativeLoginResponse403 | FinishManagedNativeLoginResponse404 | FinishManagedNativeLoginResponse429 | FinishManagedNativeLoginResponse500 | None:
    """ Redeem a managed session grant

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        body (FinishManagedNativeLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinishManagedNativeLoginResponse200 | FinishManagedNativeLoginResponse400 | FinishManagedNativeLoginResponse401 | FinishManagedNativeLoginResponse403 | FinishManagedNativeLoginResponse404 | FinishManagedNativeLoginResponse429 | FinishManagedNativeLoginResponse500
     """


    return sync_detailed(
        provider=provider,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: FinishManagedNativeLoginBody,

) -> Response[FinishManagedNativeLoginResponse200 | FinishManagedNativeLoginResponse400 | FinishManagedNativeLoginResponse401 | FinishManagedNativeLoginResponse403 | FinishManagedNativeLoginResponse404 | FinishManagedNativeLoginResponse429 | FinishManagedNativeLoginResponse500]:
    """ Redeem a managed session grant

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        body (FinishManagedNativeLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinishManagedNativeLoginResponse200 | FinishManagedNativeLoginResponse400 | FinishManagedNativeLoginResponse401 | FinishManagedNativeLoginResponse403 | FinishManagedNativeLoginResponse404 | FinishManagedNativeLoginResponse429 | FinishManagedNativeLoginResponse500]
     """


    kwargs = _get_kwargs(
        provider=provider,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: FinishManagedNativeLoginBody,

) -> FinishManagedNativeLoginResponse200 | FinishManagedNativeLoginResponse400 | FinishManagedNativeLoginResponse401 | FinishManagedNativeLoginResponse403 | FinishManagedNativeLoginResponse404 | FinishManagedNativeLoginResponse429 | FinishManagedNativeLoginResponse500 | None:
    """ Redeem a managed session grant

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        body (FinishManagedNativeLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinishManagedNativeLoginResponse200 | FinishManagedNativeLoginResponse400 | FinishManagedNativeLoginResponse401 | FinishManagedNativeLoginResponse403 | FinishManagedNativeLoginResponse404 | FinishManagedNativeLoginResponse429 | FinishManagedNativeLoginResponse500
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,
body=body,

    )).parsed
