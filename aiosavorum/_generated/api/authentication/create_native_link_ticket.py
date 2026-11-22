from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_native_link_ticket_body import CreateNativeLinkTicketBody
from ...models.create_native_link_ticket_response_200 import CreateNativeLinkTicketResponse200
from ...models.create_native_link_ticket_response_400 import CreateNativeLinkTicketResponse400
from ...models.create_native_link_ticket_response_401 import CreateNativeLinkTicketResponse401
from ...models.create_native_link_ticket_response_403 import CreateNativeLinkTicketResponse403
from ...models.create_native_link_ticket_response_404 import CreateNativeLinkTicketResponse404
from ...models.create_native_link_ticket_response_429 import CreateNativeLinkTicketResponse429
from ...models.create_native_link_ticket_response_500 import CreateNativeLinkTicketResponse500
from typing import cast



def _get_kwargs(
    provider: str,
    *,
    body: CreateNativeLinkTicketBody,
    origin: str,
    x_csrf_token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    headers["X-CSRF-Token"] = x_csrf_token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/auth/{provider}/native-link-tickets".format(provider=quote(str(provider), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> CreateNativeLinkTicketResponse200 | CreateNativeLinkTicketResponse400 | CreateNativeLinkTicketResponse401 | CreateNativeLinkTicketResponse403 | CreateNativeLinkTicketResponse404 | CreateNativeLinkTicketResponse429 | CreateNativeLinkTicketResponse500 | None:
    if response.status_code == 200:
        response_200 = CreateNativeLinkTicketResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = CreateNativeLinkTicketResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = CreateNativeLinkTicketResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = CreateNativeLinkTicketResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = CreateNativeLinkTicketResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = CreateNativeLinkTicketResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = CreateNativeLinkTicketResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[CreateNativeLinkTicketResponse200 | CreateNativeLinkTicketResponse400 | CreateNativeLinkTicketResponse401 | CreateNativeLinkTicketResponse403 | CreateNativeLinkTicketResponse404 | CreateNativeLinkTicketResponse429 | CreateNativeLinkTicketResponse500]:
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
    body: CreateNativeLinkTicketBody,
    origin: str,
    x_csrf_token: str,

) -> Response[CreateNativeLinkTicketResponse200 | CreateNativeLinkTicketResponse400 | CreateNativeLinkTicketResponse401 | CreateNativeLinkTicketResponse403 | CreateNativeLinkTicketResponse404 | CreateNativeLinkTicketResponse429 | CreateNativeLinkTicketResponse500]:
    """ Start a native link

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        origin (str):
        x_csrf_token (str):
        body (CreateNativeLinkTicketBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateNativeLinkTicketResponse200 | CreateNativeLinkTicketResponse400 | CreateNativeLinkTicketResponse401 | CreateNativeLinkTicketResponse403 | CreateNativeLinkTicketResponse404 | CreateNativeLinkTicketResponse429 | CreateNativeLinkTicketResponse500]
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
    client: AuthenticatedClient | Client,
    body: CreateNativeLinkTicketBody,
    origin: str,
    x_csrf_token: str,

) -> CreateNativeLinkTicketResponse200 | CreateNativeLinkTicketResponse400 | CreateNativeLinkTicketResponse401 | CreateNativeLinkTicketResponse403 | CreateNativeLinkTicketResponse404 | CreateNativeLinkTicketResponse429 | CreateNativeLinkTicketResponse500 | None:
    """ Start a native link

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        origin (str):
        x_csrf_token (str):
        body (CreateNativeLinkTicketBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateNativeLinkTicketResponse200 | CreateNativeLinkTicketResponse400 | CreateNativeLinkTicketResponse401 | CreateNativeLinkTicketResponse403 | CreateNativeLinkTicketResponse404 | CreateNativeLinkTicketResponse429 | CreateNativeLinkTicketResponse500
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
    client: AuthenticatedClient | Client,
    body: CreateNativeLinkTicketBody,
    origin: str,
    x_csrf_token: str,

) -> Response[CreateNativeLinkTicketResponse200 | CreateNativeLinkTicketResponse400 | CreateNativeLinkTicketResponse401 | CreateNativeLinkTicketResponse403 | CreateNativeLinkTicketResponse404 | CreateNativeLinkTicketResponse429 | CreateNativeLinkTicketResponse500]:
    """ Start a native link

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        origin (str):
        x_csrf_token (str):
        body (CreateNativeLinkTicketBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateNativeLinkTicketResponse200 | CreateNativeLinkTicketResponse400 | CreateNativeLinkTicketResponse401 | CreateNativeLinkTicketResponse403 | CreateNativeLinkTicketResponse404 | CreateNativeLinkTicketResponse429 | CreateNativeLinkTicketResponse500]
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
    client: AuthenticatedClient | Client,
    body: CreateNativeLinkTicketBody,
    origin: str,
    x_csrf_token: str,

) -> CreateNativeLinkTicketResponse200 | CreateNativeLinkTicketResponse400 | CreateNativeLinkTicketResponse401 | CreateNativeLinkTicketResponse403 | CreateNativeLinkTicketResponse404 | CreateNativeLinkTicketResponse429 | CreateNativeLinkTicketResponse500 | None:
    """ Start a native link

     Available only when account authentication is enabled. Provider configuration is restart-bound.
    Local logout does not require an external provider. Responses must not be cached.

    Args:
        provider (str):
        origin (str):
        x_csrf_token (str):
        body (CreateNativeLinkTicketBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateNativeLinkTicketResponse200 | CreateNativeLinkTicketResponse400 | CreateNativeLinkTicketResponse401 | CreateNativeLinkTicketResponse403 | CreateNativeLinkTicketResponse404 | CreateNativeLinkTicketResponse429 | CreateNativeLinkTicketResponse500
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,
body=body,
origin=origin,
x_csrf_token=x_csrf_token,

    )).parsed
