from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.invitation_register_request import InvitationRegisterRequest
from ...models.login_response import LoginResponse
from typing import cast



def _get_kwargs(
    *,
    body: InvitationRegisterRequest,
    origin: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/account/invitations/register",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | LoginResponse:
    if response.status_code == 200:
        response_200 = LoginResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = AccountProblem.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | LoginResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InvitationRegisterRequest,
    origin: str,

) -> Response[AccountProblem | LoginResponse]:
    """ Register from an invitation

     Creates the account and consumes the invitation in one transaction. Browser session and CSRF
    protection are required for mutations, except invited local registration and bearer invitation
    previews. Invitation secrets are returned once and must never be logged.

    Args:
        origin (str):
        body (InvitationRegisterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | LoginResponse]
     """


    kwargs = _get_kwargs(
        body=body,
origin=origin,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: InvitationRegisterRequest,
    origin: str,

) -> AccountProblem | LoginResponse | None:
    """ Register from an invitation

     Creates the account and consumes the invitation in one transaction. Browser session and CSRF
    protection are required for mutations, except invited local registration and bearer invitation
    previews. Invitation secrets are returned once and must never be logged.

    Args:
        origin (str):
        body (InvitationRegisterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | LoginResponse
     """


    return sync_detailed(
        client=client,
body=body,
origin=origin,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InvitationRegisterRequest,
    origin: str,

) -> Response[AccountProblem | LoginResponse]:
    """ Register from an invitation

     Creates the account and consumes the invitation in one transaction. Browser session and CSRF
    protection are required for mutations, except invited local registration and bearer invitation
    previews. Invitation secrets are returned once and must never be logged.

    Args:
        origin (str):
        body (InvitationRegisterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | LoginResponse]
     """


    kwargs = _get_kwargs(
        body=body,
origin=origin,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: InvitationRegisterRequest,
    origin: str,

) -> AccountProblem | LoginResponse | None:
    """ Register from an invitation

     Creates the account and consumes the invitation in one transaction. Browser session and CSRF
    protection are required for mutations, except invited local registration and bearer invitation
    previews. Invitation secrets are returned once and must never be logged.

    Args:
        origin (str):
        body (InvitationRegisterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | LoginResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
origin=origin,

    )).parsed
