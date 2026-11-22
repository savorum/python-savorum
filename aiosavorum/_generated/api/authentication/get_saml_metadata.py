from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_saml_metadata_response_400 import GetSamlMetadataResponse400
from ...models.get_saml_metadata_response_401 import GetSamlMetadataResponse401
from ...models.get_saml_metadata_response_403 import GetSamlMetadataResponse403
from ...models.get_saml_metadata_response_404 import GetSamlMetadataResponse404
from ...models.get_saml_metadata_response_429 import GetSamlMetadataResponse429
from ...models.get_saml_metadata_response_500 import GetSamlMetadataResponse500
from typing import cast



def _get_kwargs(
    provider: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/auth/{provider}/metadata".format(provider=quote(str(provider), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> GetSamlMetadataResponse400 | GetSamlMetadataResponse401 | GetSamlMetadataResponse403 | GetSamlMetadataResponse404 | GetSamlMetadataResponse429 | GetSamlMetadataResponse500 | None:
    if response.status_code == 400:
        response_400 = GetSamlMetadataResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetSamlMetadataResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetSamlMetadataResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetSamlMetadataResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = GetSamlMetadataResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = GetSamlMetadataResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[GetSamlMetadataResponse400 | GetSamlMetadataResponse401 | GetSamlMetadataResponse403 | GetSamlMetadataResponse404 | GetSamlMetadataResponse429 | GetSamlMetadataResponse500]:
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

) -> Response[GetSamlMetadataResponse400 | GetSamlMetadataResponse401 | GetSamlMetadataResponse403 | GetSamlMetadataResponse404 | GetSamlMetadataResponse429 | GetSamlMetadataResponse500]:
    """ Get SAML metadata

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSamlMetadataResponse400 | GetSamlMetadataResponse401 | GetSamlMetadataResponse403 | GetSamlMetadataResponse404 | GetSamlMetadataResponse429 | GetSamlMetadataResponse500]
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

) -> GetSamlMetadataResponse400 | GetSamlMetadataResponse401 | GetSamlMetadataResponse403 | GetSamlMetadataResponse404 | GetSamlMetadataResponse429 | GetSamlMetadataResponse500 | None:
    """ Get SAML metadata

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSamlMetadataResponse400 | GetSamlMetadataResponse401 | GetSamlMetadataResponse403 | GetSamlMetadataResponse404 | GetSamlMetadataResponse429 | GetSamlMetadataResponse500
     """


    return sync_detailed(
        provider=provider,
client=client,

    ).parsed

async def asyncio_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetSamlMetadataResponse400 | GetSamlMetadataResponse401 | GetSamlMetadataResponse403 | GetSamlMetadataResponse404 | GetSamlMetadataResponse429 | GetSamlMetadataResponse500]:
    """ Get SAML metadata

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSamlMetadataResponse400 | GetSamlMetadataResponse401 | GetSamlMetadataResponse403 | GetSamlMetadataResponse404 | GetSamlMetadataResponse429 | GetSamlMetadataResponse500]
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

) -> GetSamlMetadataResponse400 | GetSamlMetadataResponse401 | GetSamlMetadataResponse403 | GetSamlMetadataResponse404 | GetSamlMetadataResponse429 | GetSamlMetadataResponse500 | None:
    """ Get SAML metadata

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSamlMetadataResponse400 | GetSamlMetadataResponse401 | GetSamlMetadataResponse403 | GetSamlMetadataResponse404 | GetSamlMetadataResponse429 | GetSamlMetadataResponse500
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,

    )).parsed
