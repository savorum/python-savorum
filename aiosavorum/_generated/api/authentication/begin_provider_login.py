from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.begin_provider_login_body import BeginProviderLoginBody
from ...models.begin_provider_login_response_200_type_0 import BeginProviderLoginResponse200Type0
from ...models.begin_provider_login_response_200_type_1 import BeginProviderLoginResponse200Type1
from ...models.begin_provider_login_response_400 import BeginProviderLoginResponse400
from ...models.begin_provider_login_response_401 import BeginProviderLoginResponse401
from ...models.begin_provider_login_response_403 import BeginProviderLoginResponse403
from ...models.begin_provider_login_response_404 import BeginProviderLoginResponse404
from ...models.begin_provider_login_response_429 import BeginProviderLoginResponse429
from ...models.begin_provider_login_response_500 import BeginProviderLoginResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    provider: str,
    *,
    body: BeginProviderLoginBody,
    origin: str,
    x_csrf_token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    if not isinstance(x_csrf_token, Unset):
        headers["X-CSRF-Token"] = x_csrf_token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/auth/{provider}/login".format(provider=quote(str(provider), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> BeginProviderLoginResponse200Type0 | BeginProviderLoginResponse200Type1 | BeginProviderLoginResponse400 | BeginProviderLoginResponse401 | BeginProviderLoginResponse403 | BeginProviderLoginResponse404 | BeginProviderLoginResponse429 | BeginProviderLoginResponse500 | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> BeginProviderLoginResponse200Type0 | BeginProviderLoginResponse200Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = BeginProviderLoginResponse200Type0.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = BeginProviderLoginResponse200Type1.from_dict(data)



            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BeginProviderLoginResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = BeginProviderLoginResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = BeginProviderLoginResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = BeginProviderLoginResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = BeginProviderLoginResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = BeginProviderLoginResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[BeginProviderLoginResponse200Type0 | BeginProviderLoginResponse200Type1 | BeginProviderLoginResponse400 | BeginProviderLoginResponse401 | BeginProviderLoginResponse403 | BeginProviderLoginResponse404 | BeginProviderLoginResponse429 | BeginProviderLoginResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider: str,
    *,
    client: AuthenticatedClient,
    body: BeginProviderLoginBody,
    origin: str,
    x_csrf_token: str | Unset = UNSET,

) -> Response[BeginProviderLoginResponse200Type0 | BeginProviderLoginResponse200Type1 | BeginProviderLoginResponse400 | BeginProviderLoginResponse401 | BeginProviderLoginResponse403 | BeginProviderLoginResponse404 | BeginProviderLoginResponse429 | BeginProviderLoginResponse500]:
    """ Begin a provider sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        origin (str):
        x_csrf_token (str | Unset):
        body (BeginProviderLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BeginProviderLoginResponse200Type0 | BeginProviderLoginResponse200Type1 | BeginProviderLoginResponse400 | BeginProviderLoginResponse401 | BeginProviderLoginResponse403 | BeginProviderLoginResponse404 | BeginProviderLoginResponse429 | BeginProviderLoginResponse500]
     """


    kwargs = _get_kwargs(
        provider=provider,
body=body,
origin=origin,
x_csrf_token=x_csrf_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    provider: str,
    *,
    client: AuthenticatedClient,
    body: BeginProviderLoginBody,
    origin: str,
    x_csrf_token: str | Unset = UNSET,

) -> BeginProviderLoginResponse200Type0 | BeginProviderLoginResponse200Type1 | BeginProviderLoginResponse400 | BeginProviderLoginResponse401 | BeginProviderLoginResponse403 | BeginProviderLoginResponse404 | BeginProviderLoginResponse429 | BeginProviderLoginResponse500 | None:
    """ Begin a provider sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        origin (str):
        x_csrf_token (str | Unset):
        body (BeginProviderLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BeginProviderLoginResponse200Type0 | BeginProviderLoginResponse200Type1 | BeginProviderLoginResponse400 | BeginProviderLoginResponse401 | BeginProviderLoginResponse403 | BeginProviderLoginResponse404 | BeginProviderLoginResponse429 | BeginProviderLoginResponse500
     """


    return sync_detailed(
        provider=provider,
client=client,
body=body,
origin=origin,
x_csrf_token=x_csrf_token,

    ).parsed

async def asyncio_detailed(
    provider: str,
    *,
    client: AuthenticatedClient,
    body: BeginProviderLoginBody,
    origin: str,
    x_csrf_token: str | Unset = UNSET,

) -> Response[BeginProviderLoginResponse200Type0 | BeginProviderLoginResponse200Type1 | BeginProviderLoginResponse400 | BeginProviderLoginResponse401 | BeginProviderLoginResponse403 | BeginProviderLoginResponse404 | BeginProviderLoginResponse429 | BeginProviderLoginResponse500]:
    """ Begin a provider sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        origin (str):
        x_csrf_token (str | Unset):
        body (BeginProviderLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BeginProviderLoginResponse200Type0 | BeginProviderLoginResponse200Type1 | BeginProviderLoginResponse400 | BeginProviderLoginResponse401 | BeginProviderLoginResponse403 | BeginProviderLoginResponse404 | BeginProviderLoginResponse429 | BeginProviderLoginResponse500]
     """


    kwargs = _get_kwargs(
        provider=provider,
body=body,
origin=origin,
x_csrf_token=x_csrf_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    provider: str,
    *,
    client: AuthenticatedClient,
    body: BeginProviderLoginBody,
    origin: str,
    x_csrf_token: str | Unset = UNSET,

) -> BeginProviderLoginResponse200Type0 | BeginProviderLoginResponse200Type1 | BeginProviderLoginResponse400 | BeginProviderLoginResponse401 | BeginProviderLoginResponse403 | BeginProviderLoginResponse404 | BeginProviderLoginResponse429 | BeginProviderLoginResponse500 | None:
    """ Begin a provider sign-in

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        origin (str):
        x_csrf_token (str | Unset):
        body (BeginProviderLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BeginProviderLoginResponse200Type0 | BeginProviderLoginResponse200Type1 | BeginProviderLoginResponse400 | BeginProviderLoginResponse401 | BeginProviderLoginResponse403 | BeginProviderLoginResponse404 | BeginProviderLoginResponse429 | BeginProviderLoginResponse500
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,
body=body,
origin=origin,
x_csrf_token=x_csrf_token,

    )).parsed
