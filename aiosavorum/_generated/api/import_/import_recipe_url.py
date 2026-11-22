from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.import_output_body import ImportOutputBody
from ...models.import_url_input import ImportURLInput
from typing import cast



def _get_kwargs(
    *,
    body: ImportURLInput,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/recipes/import-url",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | ImportOutputBody | None:
    if response.status_code == 200:
        response_200 = ImportOutputBody.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 409:
        response_409 = ErrorModel.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = ErrorModel.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = ErrorModel.from_dict(response.json())



        return response_500

    if response.status_code == 502:
        response_502 = ErrorModel.from_dict(response.json())



        return response_502

    if response.status_code == 504:
        response_504 = ErrorModel.from_dict(response.json())



        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | ImportOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ImportURLInput,

) -> Response[AccountProblem | ErrorModel | ImportOutputBody]:
    """ Import a web page

     Fetches a public recipe page under Savorum's outbound policy and extracts its recipe. Structured
    data is read tolerantly: a page with one unreadable block and one good one still imports. A page
    that refused to answer, a page with no recipe on it, and a page whose recipe has no ingredients or
    method are reported as three different problems, because they are.

    Args:
        body (ImportURLInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ImportOutputBody]
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
    body: ImportURLInput,

) -> AccountProblem | ErrorModel | ImportOutputBody | None:
    """ Import a web page

     Fetches a public recipe page under Savorum's outbound policy and extracts its recipe. Structured
    data is read tolerantly: a page with one unreadable block and one good one still imports. A page
    that refused to answer, a page with no recipe on it, and a page whose recipe has no ingredients or
    method are reported as three different problems, because they are.

    Args:
        body (ImportURLInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ImportOutputBody
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ImportURLInput,

) -> Response[AccountProblem | ErrorModel | ImportOutputBody]:
    """ Import a web page

     Fetches a public recipe page under Savorum's outbound policy and extracts its recipe. Structured
    data is read tolerantly: a page with one unreadable block and one good one still imports. A page
    that refused to answer, a page with no recipe on it, and a page whose recipe has no ingredients or
    method are reported as three different problems, because they are.

    Args:
        body (ImportURLInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ImportOutputBody]
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
    body: ImportURLInput,

) -> AccountProblem | ErrorModel | ImportOutputBody | None:
    """ Import a web page

     Fetches a public recipe page under Savorum's outbound policy and extracts its recipe. Structured
    data is read tolerantly: a page with one unreadable block and one good one still imports. A page
    that refused to answer, a page with no recipe on it, and a page whose recipe has no ingredients or
    method are reported as three different problems, because they are.

    Args:
        body (ImportURLInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ImportOutputBody
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
