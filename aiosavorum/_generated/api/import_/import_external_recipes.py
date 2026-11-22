from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.import_external_recipes_body import ImportExternalRecipesBody
from ...models.import_external_recipes_on_duplicate import ImportExternalRecipesOnDuplicate
from ...models.import_external_recipes_response_200 import ImportExternalRecipesResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: ImportExternalRecipesBody,
    on_duplicate: ImportExternalRecipesOnDuplicate | Unset = ImportExternalRecipesOnDuplicate.SKIP,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_on_duplicate: str | Unset = UNSET
    if not isinstance(on_duplicate, Unset):
        json_on_duplicate = on_duplicate.value

    params["on_duplicate"] = json_on_duplicate


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/recipes/import-external",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | ImportExternalRecipesResponse200 | None:
    if response.status_code == 200:
        response_200 = ImportExternalRecipesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorModel.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ErrorModel.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorModel.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = ErrorModel.from_dict(response.json())



        return response_409

    if response.status_code == 413:
        response_413 = ErrorModel.from_dict(response.json())



        return response_413

    if response.status_code == 415:
        response_415 = ErrorModel.from_dict(response.json())



        return response_415

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | ImportExternalRecipesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ImportExternalRecipesBody,
    on_duplicate: ImportExternalRecipesOnDuplicate | Unset = ImportExternalRecipesOnDuplicate.SKIP,

) -> Response[AccountProblem | ErrorModel | ImportExternalRecipesResponse200]:
    """ Import third-party exports

     A multipart upload of exports from other applications. Every file part is read; the field names
    carry no meaning.

    Args:
        on_duplicate (ImportExternalRecipesOnDuplicate | Unset):  Default:
            ImportExternalRecipesOnDuplicate.SKIP.
        body (ImportExternalRecipesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ImportExternalRecipesResponse200]
     """


    kwargs = _get_kwargs(
        body=body,
on_duplicate=on_duplicate,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ImportExternalRecipesBody,
    on_duplicate: ImportExternalRecipesOnDuplicate | Unset = ImportExternalRecipesOnDuplicate.SKIP,

) -> AccountProblem | ErrorModel | ImportExternalRecipesResponse200 | None:
    """ Import third-party exports

     A multipart upload of exports from other applications. Every file part is read; the field names
    carry no meaning.

    Args:
        on_duplicate (ImportExternalRecipesOnDuplicate | Unset):  Default:
            ImportExternalRecipesOnDuplicate.SKIP.
        body (ImportExternalRecipesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ImportExternalRecipesResponse200
     """


    return sync_detailed(
        client=client,
body=body,
on_duplicate=on_duplicate,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ImportExternalRecipesBody,
    on_duplicate: ImportExternalRecipesOnDuplicate | Unset = ImportExternalRecipesOnDuplicate.SKIP,

) -> Response[AccountProblem | ErrorModel | ImportExternalRecipesResponse200]:
    """ Import third-party exports

     A multipart upload of exports from other applications. Every file part is read; the field names
    carry no meaning.

    Args:
        on_duplicate (ImportExternalRecipesOnDuplicate | Unset):  Default:
            ImportExternalRecipesOnDuplicate.SKIP.
        body (ImportExternalRecipesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ImportExternalRecipesResponse200]
     """


    kwargs = _get_kwargs(
        body=body,
on_duplicate=on_duplicate,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ImportExternalRecipesBody,
    on_duplicate: ImportExternalRecipesOnDuplicate | Unset = ImportExternalRecipesOnDuplicate.SKIP,

) -> AccountProblem | ErrorModel | ImportExternalRecipesResponse200 | None:
    """ Import third-party exports

     A multipart upload of exports from other applications. Every file part is read; the field names
    carry no meaning.

    Args:
        on_duplicate (ImportExternalRecipesOnDuplicate | Unset):  Default:
            ImportExternalRecipesOnDuplicate.SKIP.
        body (ImportExternalRecipesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ImportExternalRecipesResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,
on_duplicate=on_duplicate,

    )).parsed
