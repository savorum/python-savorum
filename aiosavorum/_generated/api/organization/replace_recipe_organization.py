from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.organization_input import OrganizationInput
from ...models.recipe_organization import RecipeOrganization
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: OrganizationInput,
    if_match: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match



    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/recipes/{id}/organization".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | RecipeOrganization | None:
    if response.status_code == 200:
        response_200 = RecipeOrganization.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorModel.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = ErrorModel.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = ErrorModel.from_dict(response.json())



        return response_409

    if response.status_code == 412:
        response_412 = ErrorModel.from_dict(response.json())



        return response_412

    if response.status_code == 422:
        response_422 = ErrorModel.from_dict(response.json())



        return response_422

    if response.status_code == 428:
        response_428 = ErrorModel.from_dict(response.json())



        return response_428

    if response.status_code == 500:
        response_500 = ErrorModel.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | RecipeOrganization]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OrganizationInput,
    if_match: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | RecipeOrganization]:
    """ Replace recipe organization

     Replaces tags, categories, personal state, and provenance, and applies any named book membership
    changes in the same transaction.

    Args:
        id (str):
        if_match (str | Unset):
        body (OrganizationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | RecipeOrganization]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
if_match=if_match,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OrganizationInput,
    if_match: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | RecipeOrganization | None:
    """ Replace recipe organization

     Replaces tags, categories, personal state, and provenance, and applies any named book membership
    changes in the same transaction.

    Args:
        id (str):
        if_match (str | Unset):
        body (OrganizationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | RecipeOrganization
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
if_match=if_match,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OrganizationInput,
    if_match: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | RecipeOrganization]:
    """ Replace recipe organization

     Replaces tags, categories, personal state, and provenance, and applies any named book membership
    changes in the same transaction.

    Args:
        id (str):
        if_match (str | Unset):
        body (OrganizationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | RecipeOrganization]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
if_match=if_match,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OrganizationInput,
    if_match: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | RecipeOrganization | None:
    """ Replace recipe organization

     Replaces tags, categories, personal state, and provenance, and applies any named book membership
    changes in the same transaction.

    Args:
        id (str):
        if_match (str | Unset):
        body (OrganizationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | RecipeOrganization
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
if_match=if_match,

    )).parsed
