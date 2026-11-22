from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    recipe_id: str,
    id: str,
    preset: str,
    *,
    if_none_match: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/recipes/{recipe_id}/assets/{id}/derivatives/{preset}".format(recipe_id=quote(str(recipe_id), safe=""),id=quote(str(id), safe=""),preset=quote(str(preset), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | Any | ErrorModel | None:
    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ErrorModel.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorModel.from_dict(response.json())



        return response_404

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | Any | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    recipe_id: str,
    id: str,
    preset: str,
    *,
    client: AuthenticatedClient | Client,
    if_none_match: str | Unset = UNSET,

) -> Response[AccountProblem | Any | ErrorModel]:
    """ Get a recipe asset derivative

    Args:
        recipe_id (str):
        id (str):
        preset (str):
        if_none_match (str | Unset): Revalidate a cached image after checking current access

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | Any | ErrorModel]
     """


    kwargs = _get_kwargs(
        recipe_id=recipe_id,
id=id,
preset=preset,
if_none_match=if_none_match,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    recipe_id: str,
    id: str,
    preset: str,
    *,
    client: AuthenticatedClient | Client,
    if_none_match: str | Unset = UNSET,

) -> AccountProblem | Any | ErrorModel | None:
    """ Get a recipe asset derivative

    Args:
        recipe_id (str):
        id (str):
        preset (str):
        if_none_match (str | Unset): Revalidate a cached image after checking current access

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | Any | ErrorModel
     """


    return sync_detailed(
        recipe_id=recipe_id,
id=id,
preset=preset,
client=client,
if_none_match=if_none_match,

    ).parsed

async def asyncio_detailed(
    recipe_id: str,
    id: str,
    preset: str,
    *,
    client: AuthenticatedClient | Client,
    if_none_match: str | Unset = UNSET,

) -> Response[AccountProblem | Any | ErrorModel]:
    """ Get a recipe asset derivative

    Args:
        recipe_id (str):
        id (str):
        preset (str):
        if_none_match (str | Unset): Revalidate a cached image after checking current access

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | Any | ErrorModel]
     """


    kwargs = _get_kwargs(
        recipe_id=recipe_id,
id=id,
preset=preset,
if_none_match=if_none_match,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    recipe_id: str,
    id: str,
    preset: str,
    *,
    client: AuthenticatedClient | Client,
    if_none_match: str | Unset = UNSET,

) -> AccountProblem | Any | ErrorModel | None:
    """ Get a recipe asset derivative

    Args:
        recipe_id (str):
        id (str):
        preset (str):
        if_none_match (str | Unset): Revalidate a cached image after checking current access

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | Any | ErrorModel
     """


    return (await asyncio_detailed(
        recipe_id=recipe_id,
id=id,
preset=preset,
client=client,
if_none_match=if_none_match,

    )).parsed
