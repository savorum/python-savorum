from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.list_recipe_authors_output_body import ListRecipeAuthorsOutputBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    q: str,
    limit: int | Unset = 20,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/recipe-authors",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | ListRecipeAuthorsOutputBody | None:
    if response.status_code == 200:
        response_200 = ListRecipeAuthorsOutputBody.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ErrorModel.from_dict(response.json())



        return response_403

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | ListRecipeAuthorsOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    limit: int | Unset = 20,

) -> Response[AccountProblem | ErrorModel | ListRecipeAuthorsOutputBody]:
    """ Find recipe authors

     Resolve a complete author name from active recipes in the selected library. Returns only the best
    available tier: Unicode case-folded NFC and whitespace equality, then Latin accent variants, then
    one edit or adjacent transposition for 5 to 64 rune names with at least four letters. Punctuation is
    literal in exact matching. Non-Latin marks are preserved; scripts are not transliterated. Names are
    ordered by their original Unicode spelling. Exact and accent matches have no candidate cap; typo
    comparisons evaluate at most 128 indexed candidate names. Choose a returned name before applying the
    exact author: recipe filter, and ask for a choice when suggestions are ambiguous.

    Args:
        q (str): Complete author name to resolve; only recipe author fields are searched
        limit (int | Unset): Maximum number of author names to return Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ListRecipeAuthorsOutputBody]
     """


    kwargs = _get_kwargs(
        q=q,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    limit: int | Unset = 20,

) -> AccountProblem | ErrorModel | ListRecipeAuthorsOutputBody | None:
    """ Find recipe authors

     Resolve a complete author name from active recipes in the selected library. Returns only the best
    available tier: Unicode case-folded NFC and whitespace equality, then Latin accent variants, then
    one edit or adjacent transposition for 5 to 64 rune names with at least four letters. Punctuation is
    literal in exact matching. Non-Latin marks are preserved; scripts are not transliterated. Names are
    ordered by their original Unicode spelling. Exact and accent matches have no candidate cap; typo
    comparisons evaluate at most 128 indexed candidate names. Choose a returned name before applying the
    exact author: recipe filter, and ask for a choice when suggestions are ambiguous.

    Args:
        q (str): Complete author name to resolve; only recipe author fields are searched
        limit (int | Unset): Maximum number of author names to return Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ListRecipeAuthorsOutputBody
     """


    return sync_detailed(
        client=client,
q=q,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    limit: int | Unset = 20,

) -> Response[AccountProblem | ErrorModel | ListRecipeAuthorsOutputBody]:
    """ Find recipe authors

     Resolve a complete author name from active recipes in the selected library. Returns only the best
    available tier: Unicode case-folded NFC and whitespace equality, then Latin accent variants, then
    one edit or adjacent transposition for 5 to 64 rune names with at least four letters. Punctuation is
    literal in exact matching. Non-Latin marks are preserved; scripts are not transliterated. Names are
    ordered by their original Unicode spelling. Exact and accent matches have no candidate cap; typo
    comparisons evaluate at most 128 indexed candidate names. Choose a returned name before applying the
    exact author: recipe filter, and ask for a choice when suggestions are ambiguous.

    Args:
        q (str): Complete author name to resolve; only recipe author fields are searched
        limit (int | Unset): Maximum number of author names to return Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ListRecipeAuthorsOutputBody]
     """


    kwargs = _get_kwargs(
        q=q,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    limit: int | Unset = 20,

) -> AccountProblem | ErrorModel | ListRecipeAuthorsOutputBody | None:
    """ Find recipe authors

     Resolve a complete author name from active recipes in the selected library. Returns only the best
    available tier: Unicode case-folded NFC and whitespace equality, then Latin accent variants, then
    one edit or adjacent transposition for 5 to 64 rune names with at least four letters. Punctuation is
    literal in exact matching. Non-Latin marks are preserved; scripts are not transliterated. Names are
    ordered by their original Unicode spelling. Exact and accent matches have no candidate cap; typo
    comparisons evaluate at most 128 indexed candidate names. Choose a returned name before applying the
    exact author: recipe filter, and ask for a choice when suggestions are ambiguous.

    Args:
        q (str): Complete author name to resolve; only recipe author fields are searched
        limit (int | Unset): Maximum number of author names to return Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ListRecipeAuthorsOutputBody
     """


    return (await asyncio_detailed(
        client=client,
q=q,
limit=limit,

    )).parsed
