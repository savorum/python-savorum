from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from typing import cast



def _get_kwargs(
    *,
    from_: str,
    to: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/meals/calendar",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = ErrorModel.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = ErrorModel.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


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
    from_: str,
    to: str,

) -> Response[AccountProblem | ErrorModel | str]:
    """ Download the plan as iCalendar

     Writes the dated meals in a range as all-day events that any calendar application can import. An
    imported file is a copy: later changes to the plan reach a calendar only through a subscription
    feed.

    Args:
        from_ (str): First day to include
        to (str): Last day to include, at most 366 days after the first

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | str]
     """


    kwargs = _get_kwargs(
        from_=from_,
to=to,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    from_: str,
    to: str,

) -> AccountProblem | ErrorModel | str | None:
    """ Download the plan as iCalendar

     Writes the dated meals in a range as all-day events that any calendar application can import. An
    imported file is a copy: later changes to the plan reach a calendar only through a subscription
    feed.

    Args:
        from_ (str): First day to include
        to (str): Last day to include, at most 366 days after the first

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | str
     """


    return sync_detailed(
        client=client,
from_=from_,
to=to,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: str,
    to: str,

) -> Response[AccountProblem | ErrorModel | str]:
    """ Download the plan as iCalendar

     Writes the dated meals in a range as all-day events that any calendar application can import. An
    imported file is a copy: later changes to the plan reach a calendar only through a subscription
    feed.

    Args:
        from_ (str): First day to include
        to (str): Last day to include, at most 366 days after the first

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | str]
     """


    kwargs = _get_kwargs(
        from_=from_,
to=to,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: str,
    to: str,

) -> AccountProblem | ErrorModel | str | None:
    """ Download the plan as iCalendar

     Writes the dated meals in a range as all-day events that any calendar application can import. An
    imported file is a copy: later changes to the plan reach a calendar only through a subscription
    feed.

    Args:
        from_ (str): First day to include
        to (str): Last day to include, at most 366 days after the first

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | str
     """


    return (await asyncio_detailed(
        client=client,
from_=from_,
to=to,

    )).parsed
