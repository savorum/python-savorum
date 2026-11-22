from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.parse_ingredient_line_input_body import ParseIngredientLineInputBody
from ...models.parse_ingredient_line_output_body import ParseIngredientLineOutputBody
from typing import cast



def _get_kwargs(
    *,
    body: ParseIngredientLineInputBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/ingredient-lines/parse",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | ParseIngredientLineOutputBody:
    if response.status_code == 200:
        response_200 = ParseIngredientLineOutputBody.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = ErrorModel.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | ParseIngredientLineOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ParseIngredientLineInputBody,

) -> Response[AccountProblem | ErrorModel | ParseIngredientLineOutputBody]:
    """ Read an ingredient line

     Reads one typed ingredient line into an amount, unit, name, and note using the unit words of the
    line's language. Nothing is stored. The result is the reading an import would make, so a line typed
    in the editor and the same line imported are read alike.

    Args:
        body (ParseIngredientLineInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ParseIngredientLineOutputBody]
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
    body: ParseIngredientLineInputBody,

) -> AccountProblem | ErrorModel | ParseIngredientLineOutputBody | None:
    """ Read an ingredient line

     Reads one typed ingredient line into an amount, unit, name, and note using the unit words of the
    line's language. Nothing is stored. The result is the reading an import would make, so a line typed
    in the editor and the same line imported are read alike.

    Args:
        body (ParseIngredientLineInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ParseIngredientLineOutputBody
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ParseIngredientLineInputBody,

) -> Response[AccountProblem | ErrorModel | ParseIngredientLineOutputBody]:
    """ Read an ingredient line

     Reads one typed ingredient line into an amount, unit, name, and note using the unit words of the
    line's language. Nothing is stored. The result is the reading an import would make, so a line typed
    in the editor and the same line imported are read alike.

    Args:
        body (ParseIngredientLineInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ParseIngredientLineOutputBody]
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
    body: ParseIngredientLineInputBody,

) -> AccountProblem | ErrorModel | ParseIngredientLineOutputBody | None:
    """ Read an ingredient line

     Reads one typed ingredient line into an amount, unit, name, and note using the unit words of the
    line's language. Nothing is stored. The result is the reading an import would make, so a line typed
    in the editor and the same line imported are read alike.

    Args:
        body (ParseIngredientLineInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ParseIngredientLineOutputBody
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
