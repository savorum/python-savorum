from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.import_recipe_package_on_duplicate import ImportRecipePackageOnDuplicate
from ...models.import_recipe_package_response_200 import ImportRecipePackageResponse200
from ...types import File, FileTypes
from ...types import UNSET, Unset
from io import BytesIO
from typing import cast



def _get_kwargs(
    *,
    body: File,
    on_duplicate: ImportRecipePackageOnDuplicate | Unset = ImportRecipePackageOnDuplicate.REJECT,

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
        "url": "/api/v1/recipes/import-package",
        "params": params,
    }

    _kwargs["content"] = body.payload
    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | ImportRecipePackageResponse200 | None:
    if response.status_code == 200:
        response_200 = ImportRecipePackageResponse200.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | ImportRecipePackageResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    on_duplicate: ImportRecipePackageOnDuplicate | Unset = ImportRecipePackageOnDuplicate.REJECT,

) -> Response[AccountProblem | ErrorModel | ImportRecipePackageResponse200]:
    """ Import an SREF package

     The request body is the archive itself. `on_duplicate` chooses what happens to a recipe the library
    already holds.

    Args:
        on_duplicate (ImportRecipePackageOnDuplicate | Unset):  Default:
            ImportRecipePackageOnDuplicate.REJECT.
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ImportRecipePackageResponse200]
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
    body: File,
    on_duplicate: ImportRecipePackageOnDuplicate | Unset = ImportRecipePackageOnDuplicate.REJECT,

) -> AccountProblem | ErrorModel | ImportRecipePackageResponse200 | None:
    """ Import an SREF package

     The request body is the archive itself. `on_duplicate` chooses what happens to a recipe the library
    already holds.

    Args:
        on_duplicate (ImportRecipePackageOnDuplicate | Unset):  Default:
            ImportRecipePackageOnDuplicate.REJECT.
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ImportRecipePackageResponse200
     """


    return sync_detailed(
        client=client,
body=body,
on_duplicate=on_duplicate,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    on_duplicate: ImportRecipePackageOnDuplicate | Unset = ImportRecipePackageOnDuplicate.REJECT,

) -> Response[AccountProblem | ErrorModel | ImportRecipePackageResponse200]:
    """ Import an SREF package

     The request body is the archive itself. `on_duplicate` chooses what happens to a recipe the library
    already holds.

    Args:
        on_duplicate (ImportRecipePackageOnDuplicate | Unset):  Default:
            ImportRecipePackageOnDuplicate.REJECT.
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ImportRecipePackageResponse200]
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
    body: File,
    on_duplicate: ImportRecipePackageOnDuplicate | Unset = ImportRecipePackageOnDuplicate.REJECT,

) -> AccountProblem | ErrorModel | ImportRecipePackageResponse200 | None:
    """ Import an SREF package

     The request body is the archive itself. `on_duplicate` chooses what happens to a recipe the library
    already holds.

    Args:
        on_duplicate (ImportRecipePackageOnDuplicate | Unset):  Default:
            ImportRecipePackageOnDuplicate.REJECT.
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ImportRecipePackageResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,
on_duplicate=on_duplicate,

    )).parsed
