from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from typing import cast



def _get_kwargs(
    book_id: str,
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/api/v1/books/{book_id}/assets/{id}".format(book_id=quote(str(book_id), safe=""),id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | Any | ErrorModel | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
    book_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | Any | ErrorModel]:
    """ Head a book asset

    Args:
        book_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | Any | ErrorModel]
     """


    kwargs = _get_kwargs(
        book_id=book_id,
id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    book_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | Any | ErrorModel | None:
    """ Head a book asset

    Args:
        book_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | Any | ErrorModel
     """


    return sync_detailed(
        book_id=book_id,
id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    book_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | Any | ErrorModel]:
    """ Head a book asset

    Args:
        book_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | Any | ErrorModel]
     """


    kwargs = _get_kwargs(
        book_id=book_id,
id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    book_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | Any | ErrorModel | None:
    """ Head a book asset

    Args:
        book_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | Any | ErrorModel
     """


    return (await asyncio_detailed(
        book_id=book_id,
id=id,
client=client,

    )).parsed
