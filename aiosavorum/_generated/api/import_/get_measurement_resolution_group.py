from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.measurement_resolution_group_detail import MeasurementResolutionGroupDetail
from typing import cast



def _get_kwargs(
    preview_id: str,
    group_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/recipes/import-previews/{preview_id}/measurement-resolution-groups/{group_id}".format(preview_id=quote(str(preview_id), safe=""),group_id=quote(str(group_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | MeasurementResolutionGroupDetail | None:
    if response.status_code == 200:
        response_200 = MeasurementResolutionGroupDetail.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | MeasurementResolutionGroupDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    preview_id: str,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | ErrorModel | MeasurementResolutionGroupDetail]:
    """ Get a measurement group

    Args:
        preview_id (str):
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | MeasurementResolutionGroupDetail]
     """


    kwargs = _get_kwargs(
        preview_id=preview_id,
group_id=group_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    preview_id: str,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | ErrorModel | MeasurementResolutionGroupDetail | None:
    """ Get a measurement group

    Args:
        preview_id (str):
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | MeasurementResolutionGroupDetail
     """


    return sync_detailed(
        preview_id=preview_id,
group_id=group_id,
client=client,

    ).parsed

async def asyncio_detailed(
    preview_id: str,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | ErrorModel | MeasurementResolutionGroupDetail]:
    """ Get a measurement group

    Args:
        preview_id (str):
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | MeasurementResolutionGroupDetail]
     """


    kwargs = _get_kwargs(
        preview_id=preview_id,
group_id=group_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    preview_id: str,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | ErrorModel | MeasurementResolutionGroupDetail | None:
    """ Get a measurement group

    Args:
        preview_id (str):
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | MeasurementResolutionGroupDetail
     """


    return (await asyncio_detailed(
        preview_id=preview_id,
group_id=group_id,
client=client,

    )).parsed
