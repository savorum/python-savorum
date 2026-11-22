from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    after: str | Unset = UNSET,
    last_event_id: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(last_event_id, Unset):
        headers["Last-Event-Id"] = last_event_id



    

    params: dict[str, Any] = {}

    params["after"] = after


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/events",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | str:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = ErrorModel.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    after: str | Unset = UNSET,
    last_event_id: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | str]:
    """ Follow library changes

     Authorized server-sent events use the versioned domain envelope. Send Last-Event-ID (or after) to
    resume up to seven days of retained history. A resync event requires a normal API refresh; cursor
    events advance past irrelevant facts. Authorization is rechecked every second. There are at most
    four streams per account, 1024 per instance, 100 events per page, 15-second heartbeats, and five-
    minute connections. Reconnect with backoff; correctness never depends on this connection. Tokens are
    accepted only in Authorization, never query parameters.

    Args:
        after (str | Unset):
        last_event_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | str]
     """


    kwargs = _get_kwargs(
        after=after,
last_event_id=last_event_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    after: str | Unset = UNSET,
    last_event_id: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | str | None:
    """ Follow library changes

     Authorized server-sent events use the versioned domain envelope. Send Last-Event-ID (or after) to
    resume up to seven days of retained history. A resync event requires a normal API refresh; cursor
    events advance past irrelevant facts. Authorization is rechecked every second. There are at most
    four streams per account, 1024 per instance, 100 events per page, 15-second heartbeats, and five-
    minute connections. Reconnect with backoff; correctness never depends on this connection. Tokens are
    accepted only in Authorization, never query parameters.

    Args:
        after (str | Unset):
        last_event_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | str
     """


    return sync_detailed(
        client=client,
after=after,
last_event_id=last_event_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    after: str | Unset = UNSET,
    last_event_id: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | str]:
    """ Follow library changes

     Authorized server-sent events use the versioned domain envelope. Send Last-Event-ID (or after) to
    resume up to seven days of retained history. A resync event requires a normal API refresh; cursor
    events advance past irrelevant facts. Authorization is rechecked every second. There are at most
    four streams per account, 1024 per instance, 100 events per page, 15-second heartbeats, and five-
    minute connections. Reconnect with backoff; correctness never depends on this connection. Tokens are
    accepted only in Authorization, never query parameters.

    Args:
        after (str | Unset):
        last_event_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | str]
     """


    kwargs = _get_kwargs(
        after=after,
last_event_id=last_event_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    after: str | Unset = UNSET,
    last_event_id: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | str | None:
    """ Follow library changes

     Authorized server-sent events use the versioned domain envelope. Send Last-Event-ID (or after) to
    resume up to seven days of retained history. A resync event requires a normal API refresh; cursor
    events advance past irrelevant facts. Authorization is rechecked every second. There are at most
    four streams per account, 1024 per instance, 100 events per page, 15-second heartbeats, and five-
    minute connections. Reconnect with backoff; correctness never depends on this connection. Tokens are
    accepted only in Authorization, never query parameters.

    Args:
        after (str | Unset):
        last_event_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | str
     """


    return (await asyncio_detailed(
        client=client,
after=after,
last_event_id=last_event_id,

    )).parsed
