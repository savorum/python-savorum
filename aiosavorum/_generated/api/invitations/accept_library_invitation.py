from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.accepted_response import AcceptedResponse
from ...models.account_problem import AccountProblem
from ...models.invitation_accept_request import InvitationAcceptRequest
from typing import cast



def _get_kwargs(
    *,
    body: InvitationAcceptRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/account/invitations/accept",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AcceptedResponse | AccountProblem:
    if response.status_code == 200:
        response_200 = AcceptedResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = AccountProblem.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AcceptedResponse | AccountProblem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InvitationAcceptRequest,

) -> Response[AcceptedResponse | AccountProblem]:
    """ Accept an invitation

     Grants only the invited library role, never instance administration. Browser session and CSRF
    protection are required for mutations, except invited local registration and bearer invitation
    previews. Invitation secrets are returned once and must never be logged.

    Args:
        body (InvitationAcceptRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AcceptedResponse | AccountProblem]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: InvitationAcceptRequest,

) -> AcceptedResponse | AccountProblem | None:
    """ Accept an invitation

     Grants only the invited library role, never instance administration. Browser session and CSRF
    protection are required for mutations, except invited local registration and bearer invitation
    previews. Invitation secrets are returned once and must never be logged.

    Args:
        body (InvitationAcceptRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AcceptedResponse | AccountProblem
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InvitationAcceptRequest,

) -> Response[AcceptedResponse | AccountProblem]:
    """ Accept an invitation

     Grants only the invited library role, never instance administration. Browser session and CSRF
    protection are required for mutations, except invited local registration and bearer invitation
    previews. Invitation secrets are returned once and must never be logged.

    Args:
        body (InvitationAcceptRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AcceptedResponse | AccountProblem]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: InvitationAcceptRequest,

) -> AcceptedResponse | AccountProblem | None:
    """ Accept an invitation

     Grants only the invited library role, never instance administration. Browser session and CSRF
    protection are required for mutations, except invited local registration and bearer invitation
    previews. Invitation secrets are returned once and must never be logged.

    Args:
        body (InvitationAcceptRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AcceptedResponse | AccountProblem
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
