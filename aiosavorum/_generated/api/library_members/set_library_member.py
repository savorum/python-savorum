from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.set_library_member_response_200 import SetLibraryMemberResponse200
from ...models.set_member_request import SetMemberRequest
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    user: str,
    *,
    body: SetMemberRequest,
    x_csrf_token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_csrf_token, Unset):
        headers["X-CSRF-Token"] = x_csrf_token



    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/libraries/{id}/members/{user}".format(id=quote(str(id), safe=""),user=quote(str(user), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | SetLibraryMemberResponse200:
    if response.status_code == 200:
        response_200 = SetLibraryMemberResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = AccountProblem.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | SetLibraryMemberResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    user: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetMemberRequest,
    x_csrf_token: str | Unset = UNSET,

) -> Response[AccountProblem | SetLibraryMemberResponse200]:
    """ Set a library member

     Assigns a manual membership role. Library ownership required. Uses the persisted local-mode user
    when authentication is disabled. Otherwise an authenticated browser session is required, except for
    the current account and sign-in. Modifying authenticated requests require the current X-CSRF-Token.
    Credentials and responses must not be cached.

    Args:
        id (str):
        user (str):
        x_csrf_token (str | Unset):
        body (SetMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | SetLibraryMemberResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
user=user,
body=body,
x_csrf_token=x_csrf_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    user: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetMemberRequest,
    x_csrf_token: str | Unset = UNSET,

) -> AccountProblem | SetLibraryMemberResponse200 | None:
    """ Set a library member

     Assigns a manual membership role. Library ownership required. Uses the persisted local-mode user
    when authentication is disabled. Otherwise an authenticated browser session is required, except for
    the current account and sign-in. Modifying authenticated requests require the current X-CSRF-Token.
    Credentials and responses must not be cached.

    Args:
        id (str):
        user (str):
        x_csrf_token (str | Unset):
        body (SetMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | SetLibraryMemberResponse200
     """


    return sync_detailed(
        id=id,
user=user,
client=client,
body=body,
x_csrf_token=x_csrf_token,

    ).parsed

async def asyncio_detailed(
    id: str,
    user: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetMemberRequest,
    x_csrf_token: str | Unset = UNSET,

) -> Response[AccountProblem | SetLibraryMemberResponse200]:
    """ Set a library member

     Assigns a manual membership role. Library ownership required. Uses the persisted local-mode user
    when authentication is disabled. Otherwise an authenticated browser session is required, except for
    the current account and sign-in. Modifying authenticated requests require the current X-CSRF-Token.
    Credentials and responses must not be cached.

    Args:
        id (str):
        user (str):
        x_csrf_token (str | Unset):
        body (SetMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | SetLibraryMemberResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
user=user,
body=body,
x_csrf_token=x_csrf_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    user: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetMemberRequest,
    x_csrf_token: str | Unset = UNSET,

) -> AccountProblem | SetLibraryMemberResponse200 | None:
    """ Set a library member

     Assigns a manual membership role. Library ownership required. Uses the persisted local-mode user
    when authentication is disabled. Otherwise an authenticated browser session is required, except for
    the current account and sign-in. Modifying authenticated requests require the current X-CSRF-Token.
    Credentials and responses must not be cached.

    Args:
        id (str):
        user (str):
        x_csrf_token (str | Unset):
        body (SetMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | SetLibraryMemberResponse200
     """


    return (await asyncio_detailed(
        id=id,
user=user,
client=client,
body=body,
x_csrf_token=x_csrf_token,

    )).parsed
