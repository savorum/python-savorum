from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.import_job_resource import ImportJobResource
from typing import cast



def _get_kwargs(
    job_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/import-jobs/{job_id}/resume".format(job_id=quote(str(job_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | ImportJobResource | None:
    if response.status_code == 200:
        response_200 = ImportJobResource.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = ErrorModel.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = ErrorModel.from_dict(response.json())



        return response_409

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | ImportJobResource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | ErrorModel | ImportJobResource]:
    """ Resume an import job

     Runs the recipes an interrupted, cancelled, or partly failed import never finished, from what was
    written down for each of them. A recipe whose bytes only ever existed inside the uploaded file is
    reported as needing that file again rather than retried against nothing.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ImportJobResource]
     """


    kwargs = _get_kwargs(
        job_id=job_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | ErrorModel | ImportJobResource | None:
    """ Resume an import job

     Runs the recipes an interrupted, cancelled, or partly failed import never finished, from what was
    written down for each of them. A recipe whose bytes only ever existed inside the uploaded file is
    reported as needing that file again rather than retried against nothing.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ImportJobResource
     """


    return sync_detailed(
        job_id=job_id,
client=client,

    ).parsed

async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | ErrorModel | ImportJobResource]:
    """ Resume an import job

     Runs the recipes an interrupted, cancelled, or partly failed import never finished, from what was
    written down for each of them. A recipe whose bytes only ever existed inside the uploaded file is
    reported as needing that file again rather than retried against nothing.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ImportJobResource]
     """


    kwargs = _get_kwargs(
        job_id=job_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | ErrorModel | ImportJobResource | None:
    """ Resume an import job

     Runs the recipes an interrupted, cancelled, or partly failed import never finished, from what was
    written down for each of them. A recipe whose bytes only ever existed inside the uploaded file is
    reported as needing that file again rather than retried against nothing.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ImportJobResource
     """


    return (await asyncio_detailed(
        job_id=job_id,
client=client,

    )).parsed
