from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.begin_native_browser_login_code_challenge_method import BeginNativeBrowserLoginCodeChallengeMethod
from ...models.begin_native_browser_login_response_400 import BeginNativeBrowserLoginResponse400
from ...models.begin_native_browser_login_response_401 import BeginNativeBrowserLoginResponse401
from ...models.begin_native_browser_login_response_403 import BeginNativeBrowserLoginResponse403
from ...models.begin_native_browser_login_response_404 import BeginNativeBrowserLoginResponse404
from ...models.begin_native_browser_login_response_429 import BeginNativeBrowserLoginResponse429
from ...models.begin_native_browser_login_response_500 import BeginNativeBrowserLoginResponse500
from typing import cast



def _get_kwargs(
    *,
    redirect_uri: str,
    state: str,
    code_challenge: str,
    code_challenge_method: BeginNativeBrowserLoginCodeChallengeMethod,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["redirect_uri"] = redirect_uri

    params["state"] = state

    params["code_challenge"] = code_challenge

    json_code_challenge_method = code_challenge_method.value
    params["code_challenge_method"] = json_code_challenge_method


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/auth/native-browser",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | BeginNativeBrowserLoginResponse400 | BeginNativeBrowserLoginResponse401 | BeginNativeBrowserLoginResponse403 | BeginNativeBrowserLoginResponse404 | BeginNativeBrowserLoginResponse429 | BeginNativeBrowserLoginResponse500 | None:
    if response.status_code == 303:
        response_303 = cast(Any, None)
        return response_303

    if response.status_code == 400:
        response_400 = BeginNativeBrowserLoginResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = BeginNativeBrowserLoginResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = BeginNativeBrowserLoginResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = BeginNativeBrowserLoginResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = BeginNativeBrowserLoginResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = BeginNativeBrowserLoginResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any | BeginNativeBrowserLoginResponse400 | BeginNativeBrowserLoginResponse401 | BeginNativeBrowserLoginResponse403 | BeginNativeBrowserLoginResponse404 | BeginNativeBrowserLoginResponse429 | BeginNativeBrowserLoginResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    redirect_uri: str,
    state: str,
    code_challenge: str,
    code_challenge_method: BeginNativeBrowserLoginCodeChallengeMethod,

) -> Response[Any | BeginNativeBrowserLoginResponse400 | BeginNativeBrowserLoginResponse401 | BeginNativeBrowserLoginResponse403 | BeginNativeBrowserLoginResponse404 | BeginNativeBrowserLoginResponse429 | BeginNativeBrowserLoginResponse500]:
    """ Open browser sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        redirect_uri (str):
        state (str):
        code_challenge (str):
        code_challenge_method (BeginNativeBrowserLoginCodeChallengeMethod):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BeginNativeBrowserLoginResponse400 | BeginNativeBrowserLoginResponse401 | BeginNativeBrowserLoginResponse403 | BeginNativeBrowserLoginResponse404 | BeginNativeBrowserLoginResponse429 | BeginNativeBrowserLoginResponse500]
     """


    kwargs = _get_kwargs(
        redirect_uri=redirect_uri,
state=state,
code_challenge=code_challenge,
code_challenge_method=code_challenge_method,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    redirect_uri: str,
    state: str,
    code_challenge: str,
    code_challenge_method: BeginNativeBrowserLoginCodeChallengeMethod,

) -> Any | BeginNativeBrowserLoginResponse400 | BeginNativeBrowserLoginResponse401 | BeginNativeBrowserLoginResponse403 | BeginNativeBrowserLoginResponse404 | BeginNativeBrowserLoginResponse429 | BeginNativeBrowserLoginResponse500 | None:
    """ Open browser sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        redirect_uri (str):
        state (str):
        code_challenge (str):
        code_challenge_method (BeginNativeBrowserLoginCodeChallengeMethod):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BeginNativeBrowserLoginResponse400 | BeginNativeBrowserLoginResponse401 | BeginNativeBrowserLoginResponse403 | BeginNativeBrowserLoginResponse404 | BeginNativeBrowserLoginResponse429 | BeginNativeBrowserLoginResponse500
     """


    return sync_detailed(
        client=client,
redirect_uri=redirect_uri,
state=state,
code_challenge=code_challenge,
code_challenge_method=code_challenge_method,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    redirect_uri: str,
    state: str,
    code_challenge: str,
    code_challenge_method: BeginNativeBrowserLoginCodeChallengeMethod,

) -> Response[Any | BeginNativeBrowserLoginResponse400 | BeginNativeBrowserLoginResponse401 | BeginNativeBrowserLoginResponse403 | BeginNativeBrowserLoginResponse404 | BeginNativeBrowserLoginResponse429 | BeginNativeBrowserLoginResponse500]:
    """ Open browser sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        redirect_uri (str):
        state (str):
        code_challenge (str):
        code_challenge_method (BeginNativeBrowserLoginCodeChallengeMethod):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BeginNativeBrowserLoginResponse400 | BeginNativeBrowserLoginResponse401 | BeginNativeBrowserLoginResponse403 | BeginNativeBrowserLoginResponse404 | BeginNativeBrowserLoginResponse429 | BeginNativeBrowserLoginResponse500]
     """


    kwargs = _get_kwargs(
        redirect_uri=redirect_uri,
state=state,
code_challenge=code_challenge,
code_challenge_method=code_challenge_method,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    redirect_uri: str,
    state: str,
    code_challenge: str,
    code_challenge_method: BeginNativeBrowserLoginCodeChallengeMethod,

) -> Any | BeginNativeBrowserLoginResponse400 | BeginNativeBrowserLoginResponse401 | BeginNativeBrowserLoginResponse403 | BeginNativeBrowserLoginResponse404 | BeginNativeBrowserLoginResponse429 | BeginNativeBrowserLoginResponse500 | None:
    """ Open browser sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        redirect_uri (str):
        state (str):
        code_challenge (str):
        code_challenge_method (BeginNativeBrowserLoginCodeChallengeMethod):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BeginNativeBrowserLoginResponse400 | BeginNativeBrowserLoginResponse401 | BeginNativeBrowserLoginResponse403 | BeginNativeBrowserLoginResponse404 | BeginNativeBrowserLoginResponse429 | BeginNativeBrowserLoginResponse500
     """


    return (await asyncio_detailed(
        client=client,
redirect_uri=redirect_uri,
state=state,
code_challenge=code_challenge,
code_challenge_method=code_challenge_method,

    )).parsed
