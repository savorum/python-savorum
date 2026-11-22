from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.complete_saml_login_body import CompleteSamlLoginBody
from ...models.complete_saml_login_response_400 import CompleteSamlLoginResponse400
from ...models.complete_saml_login_response_401 import CompleteSamlLoginResponse401
from ...models.complete_saml_login_response_403 import CompleteSamlLoginResponse403
from ...models.complete_saml_login_response_404 import CompleteSamlLoginResponse404
from ...models.complete_saml_login_response_429 import CompleteSamlLoginResponse429
from ...models.complete_saml_login_response_500 import CompleteSamlLoginResponse500
from typing import cast



def _get_kwargs(
    provider: str,
    *,
    body: CompleteSamlLoginBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/auth/{provider}/acs".format(provider=quote(str(provider), safe=""),),
    }

    _kwargs["data"] = body.to_dict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | CompleteSamlLoginResponse400 | CompleteSamlLoginResponse401 | CompleteSamlLoginResponse403 | CompleteSamlLoginResponse404 | CompleteSamlLoginResponse429 | CompleteSamlLoginResponse500 | None:
    if response.status_code == 303:
        response_303 = cast(Any, None)
        return response_303

    if response.status_code == 400:
        response_400 = CompleteSamlLoginResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = CompleteSamlLoginResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = CompleteSamlLoginResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = CompleteSamlLoginResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = CompleteSamlLoginResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = CompleteSamlLoginResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any | CompleteSamlLoginResponse400 | CompleteSamlLoginResponse401 | CompleteSamlLoginResponse403 | CompleteSamlLoginResponse404 | CompleteSamlLoginResponse429 | CompleteSamlLoginResponse500]:
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
    body: CompleteSamlLoginBody,

) -> Response[Any | CompleteSamlLoginResponse400 | CompleteSamlLoginResponse401 | CompleteSamlLoginResponse403 | CompleteSamlLoginResponse404 | CompleteSamlLoginResponse429 | CompleteSamlLoginResponse500]:
    """ Complete a SAML sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        body (CompleteSamlLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompleteSamlLoginResponse400 | CompleteSamlLoginResponse401 | CompleteSamlLoginResponse403 | CompleteSamlLoginResponse404 | CompleteSamlLoginResponse429 | CompleteSamlLoginResponse500]
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
    body: CompleteSamlLoginBody,

) -> Any | CompleteSamlLoginResponse400 | CompleteSamlLoginResponse401 | CompleteSamlLoginResponse403 | CompleteSamlLoginResponse404 | CompleteSamlLoginResponse429 | CompleteSamlLoginResponse500 | None:
    """ Complete a SAML sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        body (CompleteSamlLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompleteSamlLoginResponse400 | CompleteSamlLoginResponse401 | CompleteSamlLoginResponse403 | CompleteSamlLoginResponse404 | CompleteSamlLoginResponse429 | CompleteSamlLoginResponse500
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
    body: CompleteSamlLoginBody,

) -> Response[Any | CompleteSamlLoginResponse400 | CompleteSamlLoginResponse401 | CompleteSamlLoginResponse403 | CompleteSamlLoginResponse404 | CompleteSamlLoginResponse429 | CompleteSamlLoginResponse500]:
    """ Complete a SAML sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        body (CompleteSamlLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompleteSamlLoginResponse400 | CompleteSamlLoginResponse401 | CompleteSamlLoginResponse403 | CompleteSamlLoginResponse404 | CompleteSamlLoginResponse429 | CompleteSamlLoginResponse500]
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
    body: CompleteSamlLoginBody,

) -> Any | CompleteSamlLoginResponse400 | CompleteSamlLoginResponse401 | CompleteSamlLoginResponse403 | CompleteSamlLoginResponse404 | CompleteSamlLoginResponse429 | CompleteSamlLoginResponse500 | None:
    """ Complete a SAML sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        body (CompleteSamlLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompleteSamlLoginResponse400 | CompleteSamlLoginResponse401 | CompleteSamlLoginResponse403 | CompleteSamlLoginResponse404 | CompleteSamlLoginResponse429 | CompleteSamlLoginResponse500
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,
body=body,

    )).parsed
