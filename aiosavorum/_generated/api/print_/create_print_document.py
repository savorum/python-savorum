from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.print_document_info import PrintDocumentInfo
from ...models.print_request_body import PrintRequestBody
from typing import cast



def _get_kwargs(
    *,
    body: PrintRequestBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/print/documents",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | PrintDocumentInfo | None:
    if response.status_code == 201:
        response_201 = PrintDocumentInfo.from_dict(response.json())



        return response_201

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

    if response.status_code == 503:
        response_503 = ErrorModel.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | PrintDocumentInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PrintRequestBody,

) -> Response[AccountProblem | ErrorModel | PrintDocumentInfo]:
    """ Create a print document

     Freezes the revision of every named recipe, resolves the batch and measures asked for, and typesets
    the result. The document is generated on demand and is not stored as part of any recipe.

    Args:
        body (PrintRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | PrintDocumentInfo]
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
    body: PrintRequestBody,

) -> AccountProblem | ErrorModel | PrintDocumentInfo | None:
    """ Create a print document

     Freezes the revision of every named recipe, resolves the batch and measures asked for, and typesets
    the result. The document is generated on demand and is not stored as part of any recipe.

    Args:
        body (PrintRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | PrintDocumentInfo
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PrintRequestBody,

) -> Response[AccountProblem | ErrorModel | PrintDocumentInfo]:
    """ Create a print document

     Freezes the revision of every named recipe, resolves the batch and measures asked for, and typesets
    the result. The document is generated on demand and is not stored as part of any recipe.

    Args:
        body (PrintRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | PrintDocumentInfo]
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
    body: PrintRequestBody,

) -> AccountProblem | ErrorModel | PrintDocumentInfo | None:
    """ Create a print document

     Freezes the revision of every named recipe, resolves the batch and measures asked for, and typesets
    the result. The document is generated on demand and is not stored as part of any recipe.

    Args:
        body (PrintRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | PrintDocumentInfo
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
