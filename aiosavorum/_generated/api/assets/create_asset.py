from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.asset_blob import AssetBlob
from ...models.error_model import ErrorModel
from ...types import File, FileTypes
from ...types import UNSET, Unset
from io import BytesIO
from typing import cast



def _get_kwargs(
    *,
    body: File,
    x_asset_media_type: str,
    x_asset_sha256: str | Unset = UNSET,
    x_asset_size: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Asset-Media-Type"] = x_asset_media_type

    if not isinstance(x_asset_sha256, Unset):
        headers["X-Asset-SHA256"] = x_asset_sha256

    if not isinstance(x_asset_size, Unset):
        headers["X-Asset-Size"] = x_asset_size



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/assets",
    }

    _kwargs["content"] = body.payload
    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | AssetBlob | ErrorModel | None:
    if response.status_code == 201:
        response_201 = AssetBlob.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = ErrorModel.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ErrorModel.from_dict(response.json())



        return response_403

    if response.status_code == 413:
        response_413 = ErrorModel.from_dict(response.json())



        return response_413

    if response.status_code == 415:
        response_415 = ErrorModel.from_dict(response.json())



        return response_415

    if response.status_code == 422:
        response_422 = ErrorModel.from_dict(response.json())



        return response_422

    if response.status_code == 429:
        response_429 = ErrorModel.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = ErrorModel.from_dict(response.json())



        return response_500

    if response.status_code == 507:
        response_507 = ErrorModel.from_dict(response.json())



        return response_507

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | AssetBlob | ErrorModel]:
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
    x_asset_media_type: str,
    x_asset_sha256: str | Unset = UNSET,
    x_asset_size: str | Unset = UNSET,

) -> Response[AccountProblem | AssetBlob | ErrorModel]:
    """ Upload an asset

    Args:
        x_asset_media_type (str): Declared media type; verified against the bytes
        x_asset_sha256 (str | Unset): Optional expected lowercase SHA-256 digest
        x_asset_size (str | Unset): Optional expected byte count
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | AssetBlob | ErrorModel]
     """


    kwargs = _get_kwargs(
        body=body,
x_asset_media_type=x_asset_media_type,
x_asset_sha256=x_asset_sha256,
x_asset_size=x_asset_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    x_asset_media_type: str,
    x_asset_sha256: str | Unset = UNSET,
    x_asset_size: str | Unset = UNSET,

) -> AccountProblem | AssetBlob | ErrorModel | None:
    """ Upload an asset

    Args:
        x_asset_media_type (str): Declared media type; verified against the bytes
        x_asset_sha256 (str | Unset): Optional expected lowercase SHA-256 digest
        x_asset_size (str | Unset): Optional expected byte count
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | AssetBlob | ErrorModel
     """


    return sync_detailed(
        client=client,
body=body,
x_asset_media_type=x_asset_media_type,
x_asset_sha256=x_asset_sha256,
x_asset_size=x_asset_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    x_asset_media_type: str,
    x_asset_sha256: str | Unset = UNSET,
    x_asset_size: str | Unset = UNSET,

) -> Response[AccountProblem | AssetBlob | ErrorModel]:
    """ Upload an asset

    Args:
        x_asset_media_type (str): Declared media type; verified against the bytes
        x_asset_sha256 (str | Unset): Optional expected lowercase SHA-256 digest
        x_asset_size (str | Unset): Optional expected byte count
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | AssetBlob | ErrorModel]
     """


    kwargs = _get_kwargs(
        body=body,
x_asset_media_type=x_asset_media_type,
x_asset_sha256=x_asset_sha256,
x_asset_size=x_asset_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    x_asset_media_type: str,
    x_asset_sha256: str | Unset = UNSET,
    x_asset_size: str | Unset = UNSET,

) -> AccountProblem | AssetBlob | ErrorModel | None:
    """ Upload an asset

    Args:
        x_asset_media_type (str): Declared media type; verified against the bytes
        x_asset_sha256 (str | Unset): Optional expected lowercase SHA-256 digest
        x_asset_size (str | Unset): Optional expected byte count
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | AssetBlob | ErrorModel
     """


    return (await asyncio_detailed(
        client=client,
body=body,
x_asset_media_type=x_asset_media_type,
x_asset_sha256=x_asset_sha256,
x_asset_size=x_asset_size,

    )).parsed
