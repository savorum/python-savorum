from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.list_import_job_items_filter import ListImportJobItemsFilter
from ...models.list_import_job_items_output_body import ListImportJobItemsOutputBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    job_id: str,
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    filter_: ListImportJobItemsFilter | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_filter_: str | Unset = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.value

    params["filter"] = json_filter_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/import-jobs/{job_id}/items".format(job_id=quote(str(job_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | ListImportJobItemsOutputBody | None:
    if response.status_code == 200:
        response_200 = ListImportJobItemsOutputBody.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = ErrorModel.from_dict(response.json())



        return response_404

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | ListImportJobItemsOutputBody]:
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
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    filter_: ListImportJobItemsFilter | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | ListImportJobItemsOutputBody]:
    """ List import job items

     One row per recipe the import was asked to bring in, in the order they were selected. Filtering is
    by what a reader is looking for rather than by storage state.

    Args:
        job_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        filter_ (ListImportJobItemsFilter | Unset): Review-required and informational describe
            consequences rather than storage states

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ListImportJobItemsOutputBody]
     """


    kwargs = _get_kwargs(
        job_id=job_id,
limit=limit,
offset=offset,
filter_=filter_,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    filter_: ListImportJobItemsFilter | Unset = UNSET,

) -> AccountProblem | ErrorModel | ListImportJobItemsOutputBody | None:
    """ List import job items

     One row per recipe the import was asked to bring in, in the order they were selected. Filtering is
    by what a reader is looking for rather than by storage state.

    Args:
        job_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        filter_ (ListImportJobItemsFilter | Unset): Review-required and informational describe
            consequences rather than storage states

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ListImportJobItemsOutputBody
     """


    return sync_detailed(
        job_id=job_id,
client=client,
limit=limit,
offset=offset,
filter_=filter_,

    ).parsed

async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    filter_: ListImportJobItemsFilter | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | ListImportJobItemsOutputBody]:
    """ List import job items

     One row per recipe the import was asked to bring in, in the order they were selected. Filtering is
    by what a reader is looking for rather than by storage state.

    Args:
        job_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        filter_ (ListImportJobItemsFilter | Unset): Review-required and informational describe
            consequences rather than storage states

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ListImportJobItemsOutputBody]
     """


    kwargs = _get_kwargs(
        job_id=job_id,
limit=limit,
offset=offset,
filter_=filter_,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    filter_: ListImportJobItemsFilter | Unset = UNSET,

) -> AccountProblem | ErrorModel | ListImportJobItemsOutputBody | None:
    """ List import job items

     One row per recipe the import was asked to bring in, in the order they were selected. Filtering is
    by what a reader is looking for rather than by storage state.

    Args:
        job_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        filter_ (ListImportJobItemsFilter | Unset): Review-required and informational describe
            consequences rather than storage states

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ListImportJobItemsOutputBody
     """


    return (await asyncio_detailed(
        job_id=job_id,
client=client,
limit=limit,
offset=offset,
filter_=filter_,

    )).parsed
