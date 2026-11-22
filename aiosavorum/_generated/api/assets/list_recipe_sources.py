from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.source_attachment_list_output_body import SourceAttachmentListOutputBody
from typing import cast



def _get_kwargs(
    recipe_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/recipes/{recipe_id}/sources".format(recipe_id=quote(str(recipe_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | SourceAttachmentListOutputBody | None:
    if response.status_code == 200:
        response_200 = SourceAttachmentListOutputBody.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | SourceAttachmentListOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    recipe_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | ErrorModel | SourceAttachmentListOutputBody]:
    """ List retained recipe sources

    Args:
        recipe_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | SourceAttachmentListOutputBody]
     """


    kwargs = _get_kwargs(
        recipe_id=recipe_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    recipe_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | ErrorModel | SourceAttachmentListOutputBody | None:
    """ List retained recipe sources

    Args:
        recipe_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | SourceAttachmentListOutputBody
     """


    return sync_detailed(
        recipe_id=recipe_id,
client=client,

    ).parsed

async def asyncio_detailed(
    recipe_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | ErrorModel | SourceAttachmentListOutputBody]:
    """ List retained recipe sources

    Args:
        recipe_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | SourceAttachmentListOutputBody]
     """


    kwargs = _get_kwargs(
        recipe_id=recipe_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    recipe_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | ErrorModel | SourceAttachmentListOutputBody | None:
    """ List retained recipe sources

    Args:
        recipe_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | SourceAttachmentListOutputBody
     """


    return (await asyncio_detailed(
        recipe_id=recipe_id,
client=client,

    )).parsed
