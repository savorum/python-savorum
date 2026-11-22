from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.complete_oidc_login_response_400 import CompleteOidcLoginResponse400
from ...models.complete_oidc_login_response_401 import CompleteOidcLoginResponse401
from ...models.complete_oidc_login_response_403 import CompleteOidcLoginResponse403
from ...models.complete_oidc_login_response_404 import CompleteOidcLoginResponse404
from ...models.complete_oidc_login_response_429 import CompleteOidcLoginResponse429
from ...models.complete_oidc_login_response_500 import CompleteOidcLoginResponse500
from typing import cast



def _get_kwargs(
    provider: str,
    *,
    state: str,
    code: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["state"] = state

    params["code"] = code


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/auth/{provider}/callback".format(provider=quote(str(provider), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | CompleteOidcLoginResponse400 | CompleteOidcLoginResponse401 | CompleteOidcLoginResponse403 | CompleteOidcLoginResponse404 | CompleteOidcLoginResponse429 | CompleteOidcLoginResponse500 | None:
    if response.status_code == 303:
        response_303 = cast(Any, None)
        return response_303

    if response.status_code == 400:
        response_400 = CompleteOidcLoginResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = CompleteOidcLoginResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = CompleteOidcLoginResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = CompleteOidcLoginResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = CompleteOidcLoginResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = CompleteOidcLoginResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any | CompleteOidcLoginResponse400 | CompleteOidcLoginResponse401 | CompleteOidcLoginResponse403 | CompleteOidcLoginResponse404 | CompleteOidcLoginResponse429 | CompleteOidcLoginResponse500]:
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
    state: str,
    code: str,

) -> Response[Any | CompleteOidcLoginResponse400 | CompleteOidcLoginResponse401 | CompleteOidcLoginResponse403 | CompleteOidcLoginResponse404 | CompleteOidcLoginResponse429 | CompleteOidcLoginResponse500]:
    """ Complete browser sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        state (str):
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompleteOidcLoginResponse400 | CompleteOidcLoginResponse401 | CompleteOidcLoginResponse403 | CompleteOidcLoginResponse404 | CompleteOidcLoginResponse429 | CompleteOidcLoginResponse500]
     """


    kwargs = _get_kwargs(
        provider=provider,
state=state,
code=code,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    state: str,
    code: str,

) -> Any | CompleteOidcLoginResponse400 | CompleteOidcLoginResponse401 | CompleteOidcLoginResponse403 | CompleteOidcLoginResponse404 | CompleteOidcLoginResponse429 | CompleteOidcLoginResponse500 | None:
    """ Complete browser sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        state (str):
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompleteOidcLoginResponse400 | CompleteOidcLoginResponse401 | CompleteOidcLoginResponse403 | CompleteOidcLoginResponse404 | CompleteOidcLoginResponse429 | CompleteOidcLoginResponse500
     """


    return sync_detailed(
        provider=provider,
client=client,
state=state,
code=code,

    ).parsed

async def asyncio_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    state: str,
    code: str,

) -> Response[Any | CompleteOidcLoginResponse400 | CompleteOidcLoginResponse401 | CompleteOidcLoginResponse403 | CompleteOidcLoginResponse404 | CompleteOidcLoginResponse429 | CompleteOidcLoginResponse500]:
    """ Complete browser sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        state (str):
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompleteOidcLoginResponse400 | CompleteOidcLoginResponse401 | CompleteOidcLoginResponse403 | CompleteOidcLoginResponse404 | CompleteOidcLoginResponse429 | CompleteOidcLoginResponse500]
     """


    kwargs = _get_kwargs(
        provider=provider,
state=state,
code=code,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    state: str,
    code: str,

) -> Any | CompleteOidcLoginResponse400 | CompleteOidcLoginResponse401 | CompleteOidcLoginResponse403 | CompleteOidcLoginResponse404 | CompleteOidcLoginResponse429 | CompleteOidcLoginResponse500 | None:
    """ Complete browser sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        state (str):
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompleteOidcLoginResponse400 | CompleteOidcLoginResponse401 | CompleteOidcLoginResponse403 | CompleteOidcLoginResponse404 | CompleteOidcLoginResponse429 | CompleteOidcLoginResponse500
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,
state=state,
code=code,

    )).parsed
