from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.export_bundle_input import ExportBundleInput
from typing import cast



def _get_kwargs(
    *,
    body: ExportBundleInput,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/exports/sref-bundle",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | None:
    if response.status_code == 400:
        response_400 = ErrorModel.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = ErrorModel.from_dict(response.json())



        return response_404

    if response.status_code == 413:
        response_413 = ErrorModel.from_dict(response.json())



        return response_413

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExportBundleInput,

) -> Response[AccountProblem | ErrorModel]:
    """ Export a selection bundle

     Writes a `.srefbundle`: an ordered ZIP container of complete `.sref` packages. Each member is byte
    for byte the artifact exporting that recipe on its own would produce, so any one recipe can be taken
    out and used without the bundle. A bundle is not a Savorum backup; it holds portable recipes and
    nothing about how this library is organised.

    Args:
        body (ExportBundleInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel]
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
    body: ExportBundleInput,

) -> AccountProblem | ErrorModel | None:
    """ Export a selection bundle

     Writes a `.srefbundle`: an ordered ZIP container of complete `.sref` packages. Each member is byte
    for byte the artifact exporting that recipe on its own would produce, so any one recipe can be taken
    out and used without the bundle. A bundle is not a Savorum backup; it holds portable recipes and
    nothing about how this library is organised.

    Args:
        body (ExportBundleInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExportBundleInput,

) -> Response[AccountProblem | ErrorModel]:
    """ Export a selection bundle

     Writes a `.srefbundle`: an ordered ZIP container of complete `.sref` packages. Each member is byte
    for byte the artifact exporting that recipe on its own would produce, so any one recipe can be taken
    out and used without the bundle. A bundle is not a Savorum backup; it holds portable recipes and
    nothing about how this library is organised.

    Args:
        body (ExportBundleInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel]
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
    body: ExportBundleInput,

) -> AccountProblem | ErrorModel | None:
    """ Export a selection bundle

     Writes a `.srefbundle`: an ordered ZIP container of complete `.sref` packages. Each member is byte
    for byte the artifact exporting that recipe on its own would produce, so any one recipe can be taken
    out and used without the bundle. A bundle is not a Savorum backup; it holds portable recipes and
    nothing about how this library is organised.

    Args:
        body (ExportBundleInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
