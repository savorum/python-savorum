from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.audit_response import AuditResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    library: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    category: str | Unset = UNSET,
    target: str | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    before: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["library"] = library

    params["actor"] = actor

    params["category"] = category

    params["target"] = target

    params["since"] = since

    params["until"] = until

    params["before"] = before


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/account/audit",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | AuditResponse:
    if response.status_code == 200:
        response_200 = AuditResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = AccountProblem.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | AuditResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    library: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    category: str | Unset = UNSET,
    target: str | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    before: str | Unset = UNSET,

) -> Response[AccountProblem | AuditResponse]:
    """ List audit events

     Instance history for an administrator, or owned-library history for a library owner. Uses the
    persisted local-mode user when authentication is disabled. Otherwise an authenticated browser
    session is required, except for the current account and sign-in. Modifying authenticated requests
    require the current X-CSRF-Token. Credentials and responses must not be cached.

    Args:
        library (str | Unset):
        actor (str | Unset):
        category (str | Unset):
        target (str | Unset):
        since (str | Unset):
        until (str | Unset):
        before (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | AuditResponse]
     """


    kwargs = _get_kwargs(
        library=library,
actor=actor,
category=category,
target=target,
since=since,
until=until,
before=before,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    library: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    category: str | Unset = UNSET,
    target: str | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    before: str | Unset = UNSET,

) -> AccountProblem | AuditResponse | None:
    """ List audit events

     Instance history for an administrator, or owned-library history for a library owner. Uses the
    persisted local-mode user when authentication is disabled. Otherwise an authenticated browser
    session is required, except for the current account and sign-in. Modifying authenticated requests
    require the current X-CSRF-Token. Credentials and responses must not be cached.

    Args:
        library (str | Unset):
        actor (str | Unset):
        category (str | Unset):
        target (str | Unset):
        since (str | Unset):
        until (str | Unset):
        before (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | AuditResponse
     """


    return sync_detailed(
        client=client,
library=library,
actor=actor,
category=category,
target=target,
since=since,
until=until,
before=before,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    library: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    category: str | Unset = UNSET,
    target: str | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    before: str | Unset = UNSET,

) -> Response[AccountProblem | AuditResponse]:
    """ List audit events

     Instance history for an administrator, or owned-library history for a library owner. Uses the
    persisted local-mode user when authentication is disabled. Otherwise an authenticated browser
    session is required, except for the current account and sign-in. Modifying authenticated requests
    require the current X-CSRF-Token. Credentials and responses must not be cached.

    Args:
        library (str | Unset):
        actor (str | Unset):
        category (str | Unset):
        target (str | Unset):
        since (str | Unset):
        until (str | Unset):
        before (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | AuditResponse]
     """


    kwargs = _get_kwargs(
        library=library,
actor=actor,
category=category,
target=target,
since=since,
until=until,
before=before,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    library: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    category: str | Unset = UNSET,
    target: str | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    before: str | Unset = UNSET,

) -> AccountProblem | AuditResponse | None:
    """ List audit events

     Instance history for an administrator, or owned-library history for a library owner. Uses the
    persisted local-mode user when authentication is disabled. Otherwise an authenticated browser
    session is required, except for the current account and sign-in. Modifying authenticated requests
    require the current X-CSRF-Token. Credentials and responses must not be cached.

    Args:
        library (str | Unset):
        actor (str | Unset):
        category (str | Unset):
        target (str | Unset):
        since (str | Unset):
        until (str | Unset):
        before (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | AuditResponse
     """


    return (await asyncio_detailed(
        client=client,
library=library,
actor=actor,
category=category,
target=target,
since=since,
until=until,
before=before,

    )).parsed
