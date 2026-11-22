from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.facet import Facet
from ...models.facet_input import FacetInput
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: FacetInput,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/facets",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | Facet | None:
    if response.status_code == 201:
        response_201 = Facet.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = ErrorModel.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = ErrorModel.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = ErrorModel.from_dict(response.json())



        return response_422

    if response.status_code == 429:
        response_429 = ErrorModel.from_dict(response.json())



        return response_429

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | Facet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FacetInput,
    idempotency_key: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | Facet]:
    """ Create a facet

      Creation accepts Idempotency-Key; reuse it only with the same request. Receipts last at least 24
    hours.

    Args:
        idempotency_key (str | Unset):
        body (FacetInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | Facet]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: FacetInput,
    idempotency_key: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | Facet | None:
    """ Create a facet

      Creation accepts Idempotency-Key; reuse it only with the same request. Receipts last at least 24
    hours.

    Args:
        idempotency_key (str | Unset):
        body (FacetInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | Facet
     """


    return sync_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FacetInput,
    idempotency_key: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | Facet]:
    """ Create a facet

      Creation accepts Idempotency-Key; reuse it only with the same request. Receipts last at least 24
    hours.

    Args:
        idempotency_key (str | Unset):
        body (FacetInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | Facet]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FacetInput,
    idempotency_key: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | Facet | None:
    """ Create a facet

      Creation accepts Idempotency-Key; reuse it only with the same request. Receipts last at least 24
    hours.

    Args:
        idempotency_key (str | Unset):
        body (FacetInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | Facet
     """


    return (await asyncio_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
