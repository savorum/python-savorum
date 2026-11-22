from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.begin_native_provider_login_code_challenge_method import BeginNativeProviderLoginCodeChallengeMethod
from ...models.begin_native_provider_login_response_400 import BeginNativeProviderLoginResponse400
from ...models.begin_native_provider_login_response_401 import BeginNativeProviderLoginResponse401
from ...models.begin_native_provider_login_response_403 import BeginNativeProviderLoginResponse403
from ...models.begin_native_provider_login_response_404 import BeginNativeProviderLoginResponse404
from ...models.begin_native_provider_login_response_429 import BeginNativeProviderLoginResponse429
from ...models.begin_native_provider_login_response_500 import BeginNativeProviderLoginResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    provider: str,
    *,
    redirect_uri: str,
    state: str,
    code_challenge: str,
    code_challenge_method: BeginNativeProviderLoginCodeChallengeMethod,
    link_ticket: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["redirect_uri"] = redirect_uri

    params["state"] = state

    params["code_challenge"] = code_challenge

    json_code_challenge_method = code_challenge_method.value
    params["code_challenge_method"] = json_code_challenge_method

    params["link_ticket"] = link_ticket


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/auth/{provider}/native".format(provider=quote(str(provider), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | BeginNativeProviderLoginResponse400 | BeginNativeProviderLoginResponse401 | BeginNativeProviderLoginResponse403 | BeginNativeProviderLoginResponse404 | BeginNativeProviderLoginResponse429 | BeginNativeProviderLoginResponse500 | None:
    if response.status_code == 303:
        response_303 = cast(Any, None)
        return response_303

    if response.status_code == 400:
        response_400 = BeginNativeProviderLoginResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = BeginNativeProviderLoginResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = BeginNativeProviderLoginResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = BeginNativeProviderLoginResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = BeginNativeProviderLoginResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = BeginNativeProviderLoginResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any | BeginNativeProviderLoginResponse400 | BeginNativeProviderLoginResponse401 | BeginNativeProviderLoginResponse403 | BeginNativeProviderLoginResponse404 | BeginNativeProviderLoginResponse429 | BeginNativeProviderLoginResponse500]:
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
    redirect_uri: str,
    state: str,
    code_challenge: str,
    code_challenge_method: BeginNativeProviderLoginCodeChallengeMethod,
    link_ticket: str | Unset = UNSET,

) -> Response[Any | BeginNativeProviderLoginResponse400 | BeginNativeProviderLoginResponse401 | BeginNativeProviderLoginResponse403 | BeginNativeProviderLoginResponse404 | BeginNativeProviderLoginResponse429 | BeginNativeProviderLoginResponse500]:
    """ Begin a native sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        redirect_uri (str):
        state (str):
        code_challenge (str):
        code_challenge_method (BeginNativeProviderLoginCodeChallengeMethod):
        link_ticket (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BeginNativeProviderLoginResponse400 | BeginNativeProviderLoginResponse401 | BeginNativeProviderLoginResponse403 | BeginNativeProviderLoginResponse404 | BeginNativeProviderLoginResponse429 | BeginNativeProviderLoginResponse500]
     """


    kwargs = _get_kwargs(
        provider=provider,
redirect_uri=redirect_uri,
state=state,
code_challenge=code_challenge,
code_challenge_method=code_challenge_method,
link_ticket=link_ticket,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    redirect_uri: str,
    state: str,
    code_challenge: str,
    code_challenge_method: BeginNativeProviderLoginCodeChallengeMethod,
    link_ticket: str | Unset = UNSET,

) -> Any | BeginNativeProviderLoginResponse400 | BeginNativeProviderLoginResponse401 | BeginNativeProviderLoginResponse403 | BeginNativeProviderLoginResponse404 | BeginNativeProviderLoginResponse429 | BeginNativeProviderLoginResponse500 | None:
    """ Begin a native sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        redirect_uri (str):
        state (str):
        code_challenge (str):
        code_challenge_method (BeginNativeProviderLoginCodeChallengeMethod):
        link_ticket (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BeginNativeProviderLoginResponse400 | BeginNativeProviderLoginResponse401 | BeginNativeProviderLoginResponse403 | BeginNativeProviderLoginResponse404 | BeginNativeProviderLoginResponse429 | BeginNativeProviderLoginResponse500
     """


    return sync_detailed(
        provider=provider,
client=client,
redirect_uri=redirect_uri,
state=state,
code_challenge=code_challenge,
code_challenge_method=code_challenge_method,
link_ticket=link_ticket,

    ).parsed

async def asyncio_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    redirect_uri: str,
    state: str,
    code_challenge: str,
    code_challenge_method: BeginNativeProviderLoginCodeChallengeMethod,
    link_ticket: str | Unset = UNSET,

) -> Response[Any | BeginNativeProviderLoginResponse400 | BeginNativeProviderLoginResponse401 | BeginNativeProviderLoginResponse403 | BeginNativeProviderLoginResponse404 | BeginNativeProviderLoginResponse429 | BeginNativeProviderLoginResponse500]:
    """ Begin a native sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        redirect_uri (str):
        state (str):
        code_challenge (str):
        code_challenge_method (BeginNativeProviderLoginCodeChallengeMethod):
        link_ticket (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BeginNativeProviderLoginResponse400 | BeginNativeProviderLoginResponse401 | BeginNativeProviderLoginResponse403 | BeginNativeProviderLoginResponse404 | BeginNativeProviderLoginResponse429 | BeginNativeProviderLoginResponse500]
     """


    kwargs = _get_kwargs(
        provider=provider,
redirect_uri=redirect_uri,
state=state,
code_challenge=code_challenge,
code_challenge_method=code_challenge_method,
link_ticket=link_ticket,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    redirect_uri: str,
    state: str,
    code_challenge: str,
    code_challenge_method: BeginNativeProviderLoginCodeChallengeMethod,
    link_ticket: str | Unset = UNSET,

) -> Any | BeginNativeProviderLoginResponse400 | BeginNativeProviderLoginResponse401 | BeginNativeProviderLoginResponse403 | BeginNativeProviderLoginResponse404 | BeginNativeProviderLoginResponse429 | BeginNativeProviderLoginResponse500 | None:
    """ Begin a native sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        redirect_uri (str):
        state (str):
        code_challenge (str):
        code_challenge_method (BeginNativeProviderLoginCodeChallengeMethod):
        link_ticket (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BeginNativeProviderLoginResponse400 | BeginNativeProviderLoginResponse401 | BeginNativeProviderLoginResponse403 | BeginNativeProviderLoginResponse404 | BeginNativeProviderLoginResponse429 | BeginNativeProviderLoginResponse500
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,
redirect_uri=redirect_uri,
state=state,
code_challenge=code_challenge,
code_challenge_method=code_challenge_method,
link_ticket=link_ticket,

    )).parsed
