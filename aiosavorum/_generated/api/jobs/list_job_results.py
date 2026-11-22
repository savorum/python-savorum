from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.job_results_output_body import JobResultsOutputBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 100,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/jobs/{id}/items".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | JobResultsOutputBody:
    if response.status_code == 200:
        response_200 = JobResultsOutputBody.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = ErrorModel.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | JobResultsOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,

) -> Response[AccountProblem | ErrorModel | JobResultsOutputBody]:
    """ Read job item results

     A common per-item lifecycle. Import-specific fidelity and source details are carried in import. Bulk
    results appear as items finish. Use next_offset for the next page; pages stop near 16 MiB of stored
    snapshots (one larger recipe is still returned). interrupted uncertain mutations explicitly report
    outcome-unknown and are never silently repeated.

    Args:
        id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | JobResultsOutputBody]
     """


    kwargs = _get_kwargs(
        id=id,
offset=offset,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,

) -> AccountProblem | ErrorModel | JobResultsOutputBody | None:
    """ Read job item results

     A common per-item lifecycle. Import-specific fidelity and source details are carried in import. Bulk
    results appear as items finish. Use next_offset for the next page; pages stop near 16 MiB of stored
    snapshots (one larger recipe is still returned). interrupted uncertain mutations explicitly report
    outcome-unknown and are never silently repeated.

    Args:
        id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | JobResultsOutputBody
     """


    return sync_detailed(
        id=id,
client=client,
offset=offset,
limit=limit,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,

) -> Response[AccountProblem | ErrorModel | JobResultsOutputBody]:
    """ Read job item results

     A common per-item lifecycle. Import-specific fidelity and source details are carried in import. Bulk
    results appear as items finish. Use next_offset for the next page; pages stop near 16 MiB of stored
    snapshots (one larger recipe is still returned). interrupted uncertain mutations explicitly report
    outcome-unknown and are never silently repeated.

    Args:
        id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | JobResultsOutputBody]
     """


    kwargs = _get_kwargs(
        id=id,
offset=offset,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,

) -> AccountProblem | ErrorModel | JobResultsOutputBody | None:
    """ Read job item results

     A common per-item lifecycle. Import-specific fidelity and source details are carried in import. Bulk
    results appear as items finish. Use next_offset for the next page; pages stop near 16 MiB of stored
    snapshots (one larger recipe is still returned). interrupted uncertain mutations explicitly report
    outcome-unknown and are never silently repeated.

    Args:
        id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | JobResultsOutputBody
     """


    return (await asyncio_detailed(
        id=id,
client=client,
offset=offset,
limit=limit,

    )).parsed
