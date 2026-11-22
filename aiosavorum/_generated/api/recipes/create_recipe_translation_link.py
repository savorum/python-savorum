from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.changed_entries_output_body import ChangedEntriesOutputBody
from ...models.error_model import ErrorModel
from ...models.link_translation_input_body import LinkTranslationInputBody
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: LinkTranslationInputBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/recipes/{id}/translations".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ChangedEntriesOutputBody | ErrorModel | None:
    if response.status_code == 200:
        response_200 = ChangedEntriesOutputBody.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = ErrorModel.from_dict(response.json())



        return response_404

    if response.status_code == 412:
        response_412 = ErrorModel.from_dict(response.json())



        return response_412

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ChangedEntriesOutputBody | ErrorModel]:
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
    body: LinkTranslationInputBody,

) -> Response[AccountProblem | ChangedEntriesOutputBody | ErrorModel]:
    """ Link a recipe as a translation

     Both recipes record the relationship in a new revision. Neither recipe's content changes.

    Args:
        id (str): Library entry identifier
        body (LinkTranslationInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ChangedEntriesOutputBody | ErrorModel]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: LinkTranslationInputBody,

) -> AccountProblem | ChangedEntriesOutputBody | ErrorModel | None:
    """ Link a recipe as a translation

     Both recipes record the relationship in a new revision. Neither recipe's content changes.

    Args:
        id (str): Library entry identifier
        body (LinkTranslationInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ChangedEntriesOutputBody | ErrorModel
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: LinkTranslationInputBody,

) -> Response[AccountProblem | ChangedEntriesOutputBody | ErrorModel]:
    """ Link a recipe as a translation

     Both recipes record the relationship in a new revision. Neither recipe's content changes.

    Args:
        id (str): Library entry identifier
        body (LinkTranslationInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ChangedEntriesOutputBody | ErrorModel]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: LinkTranslationInputBody,

) -> AccountProblem | ChangedEntriesOutputBody | ErrorModel | None:
    """ Link a recipe as a translation

     Both recipes record the relationship in a new revision. Neither recipe's content changes.

    Args:
        id (str): Library entry identifier
        body (LinkTranslationInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ChangedEntriesOutputBody | ErrorModel
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
