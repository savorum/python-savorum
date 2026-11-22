from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.import_job_start_input import ImportJobStartInput
from ...models.import_job_start_response import ImportJobStartResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    preview_id: str,
    *,
    body: ImportJobStartInput,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/recipes/import-previews/{preview_id}/jobs".format(preview_id=quote(str(preview_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | ImportJobStartResponse | None:
    if response.status_code == 202:
        response_202 = ImportJobStartResponse.from_dict(response.json())



        return response_202

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = ErrorModel.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = ErrorModel.from_dict(response.json())



        return response_409

    if response.status_code == 413:
        response_413 = ErrorModel.from_dict(response.json())



        return response_413

    if response.status_code == 422:
        response_422 = ErrorModel.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = ErrorModel.from_dict(response.json())



        return response_500

    if response.status_code == 503:
        response_503 = ErrorModel.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | ImportJobStartResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    preview_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ImportJobStartInput,
    idempotency_key: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | ImportJobStartResponse]:
    """ Start an import job

     Takes the selected recipes out of the review session and imports them as durable work. The response
    is a job to watch rather than a result to wait for: closing the page, losing the connection, or
    restarting Savorum does not abandon the import. Recipes are committed in batches, so partial success
    is preserved and inspectable recipe by recipe.

    Args:
        preview_id (str):
        idempotency_key (str | Unset):
        body (ImportJobStartInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ImportJobStartResponse]
     """


    kwargs = _get_kwargs(
        preview_id=preview_id,
body=body,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    preview_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ImportJobStartInput,
    idempotency_key: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | ImportJobStartResponse | None:
    """ Start an import job

     Takes the selected recipes out of the review session and imports them as durable work. The response
    is a job to watch rather than a result to wait for: closing the page, losing the connection, or
    restarting Savorum does not abandon the import. Recipes are committed in batches, so partial success
    is preserved and inspectable recipe by recipe.

    Args:
        preview_id (str):
        idempotency_key (str | Unset):
        body (ImportJobStartInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ImportJobStartResponse
     """


    return sync_detailed(
        preview_id=preview_id,
client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    preview_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ImportJobStartInput,
    idempotency_key: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | ImportJobStartResponse]:
    """ Start an import job

     Takes the selected recipes out of the review session and imports them as durable work. The response
    is a job to watch rather than a result to wait for: closing the page, losing the connection, or
    restarting Savorum does not abandon the import. Recipes are committed in batches, so partial success
    is preserved and inspectable recipe by recipe.

    Args:
        preview_id (str):
        idempotency_key (str | Unset):
        body (ImportJobStartInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ImportJobStartResponse]
     """


    kwargs = _get_kwargs(
        preview_id=preview_id,
body=body,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    preview_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ImportJobStartInput,
    idempotency_key: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | ImportJobStartResponse | None:
    """ Start an import job

     Takes the selected recipes out of the review session and imports them as durable work. The response
    is a job to watch rather than a result to wait for: closing the page, losing the connection, or
    restarting Savorum does not abandon the import. Recipes are committed in batches, so partial success
    is preserved and inspectable recipe by recipe.

    Args:
        preview_id (str):
        idempotency_key (str | Unset):
        body (ImportJobStartInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ImportJobStartResponse
     """


    return (await asyncio_detailed(
        preview_id=preview_id,
client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
