from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.export_input import ExportInput
from ...models.job_resource import JobResource
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: ExportInput,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/export-jobs",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | JobResource | None:
    if response.status_code == 202:
        response_202 = JobResource.from_dict(response.json())



        return response_202

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ErrorModel.from_dict(response.json())



        return response_403

    if response.status_code == 409:
        response_409 = ErrorModel.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = ErrorModel.from_dict(response.json())



        return response_422

    if response.status_code == 429:
        response_429 = ErrorModel.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = ErrorModel.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | JobResource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExportInput,
    idempotency_key: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | JobResource]:
    """ Queue an export

     Uses the ordinary export service, with bounded background compression and an authenticated 24-hour
    artifact. Idempotency-Key retains the same job for 24 hours; reusing a key with different input
    returns 409.

    Args:
        idempotency_key (str | Unset):
        body (ExportInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | JobResource]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ExportInput,
    idempotency_key: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | JobResource | None:
    """ Queue an export

     Uses the ordinary export service, with bounded background compression and an authenticated 24-hour
    artifact. Idempotency-Key retains the same job for 24 hours; reusing a key with different input
    returns 409.

    Args:
        idempotency_key (str | Unset):
        body (ExportInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | JobResource
     """


    return sync_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExportInput,
    idempotency_key: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | JobResource]:
    """ Queue an export

     Uses the ordinary export service, with bounded background compression and an authenticated 24-hour
    artifact. Idempotency-Key retains the same job for 24 hours; reusing a key with different input
    returns 409.

    Args:
        idempotency_key (str | Unset):
        body (ExportInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | JobResource]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ExportInput,
    idempotency_key: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | JobResource | None:
    """ Queue an export

     Uses the ordinary export service, with bounded background compression and an authenticated 24-hour
    artifact. Idempotency-Key retains the same job for 24 hours; reusing a key with different input
    returns 409.

    Args:
        idempotency_key (str | Unset):
        body (ExportInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | JobResource
     """


    return (await asyncio_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
