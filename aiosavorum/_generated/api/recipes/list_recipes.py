from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.list_recipes_output_body import ListRecipesOutputBody
from ...models.list_recipes_sort import ListRecipesSort
from ...models.list_recipes_state import ListRecipesState
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    q: str | Unset = UNSET,
    state: ListRecipesState | Unset = ListRecipesState.ACTIVE,
    sort: ListRecipesSort | Unset = ListRecipesSort.RELEVANCE,
    seed: int | Unset = 0,
    group_translations: bool | Unset = UNSET,
    languages: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["q"] = q

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["seed"] = seed

    params["group_translations"] = group_translations

    params["languages"] = languages


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/recipes",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | ListRecipesOutputBody | None:
    if response.status_code == 200:
        response_200 = ListRecipesOutputBody.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | ListRecipesOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    q: str | Unset = UNSET,
    state: ListRecipesState | Unset = ListRecipesState.ACTIVE,
    sort: ListRecipesSort | Unset = ListRecipesSort.RELEVANCE,
    seed: int | Unset = 0,
    group_translations: bool | Unset = UNSET,
    languages: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | ListRecipesOutputBody]:
    """ List recipes

    Args:
        limit (int | Unset): Maximum number of entries to return Default: 50.
        offset (int | Unset): Number of entries to skip Default: 0.
        q (str | Unset): Recipe text with bounded title/author typo matching and structured
            filters. author: requires full author-name membership with Unicode case, NFC, and
            whitespace normalization; accents and punctuation are preserved. ingredient: requires
            literal word-prefix matches within one ingredient name, including optional and alternative
            names, with original-line fallback only when that name is absent
        state (ListRecipesState | Unset): Library state to list Default: ListRecipesState.ACTIVE.
        sort (ListRecipesSort | Unset): Recipe list ordering Default: ListRecipesSort.RELEVANCE.
        seed (int | Unset): Shuffle seed for random ordering. Reuse it across pages; change it to
            reshuffle. Other sort modes ignore it Default: 0.
        group_translations (bool | Unset): Present each set of translated recipes once, as the
            rendition the preferred languages choose among those that match
        languages (str | Unset): Comma-separated BCP 47 content languages in order of preference,
            used when grouping translations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ListRecipesOutputBody]
     """


    kwargs = _get_kwargs(
        limit=limit,
offset=offset,
q=q,
state=state,
sort=sort,
seed=seed,
group_translations=group_translations,
languages=languages,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    q: str | Unset = UNSET,
    state: ListRecipesState | Unset = ListRecipesState.ACTIVE,
    sort: ListRecipesSort | Unset = ListRecipesSort.RELEVANCE,
    seed: int | Unset = 0,
    group_translations: bool | Unset = UNSET,
    languages: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | ListRecipesOutputBody | None:
    """ List recipes

    Args:
        limit (int | Unset): Maximum number of entries to return Default: 50.
        offset (int | Unset): Number of entries to skip Default: 0.
        q (str | Unset): Recipe text with bounded title/author typo matching and structured
            filters. author: requires full author-name membership with Unicode case, NFC, and
            whitespace normalization; accents and punctuation are preserved. ingredient: requires
            literal word-prefix matches within one ingredient name, including optional and alternative
            names, with original-line fallback only when that name is absent
        state (ListRecipesState | Unset): Library state to list Default: ListRecipesState.ACTIVE.
        sort (ListRecipesSort | Unset): Recipe list ordering Default: ListRecipesSort.RELEVANCE.
        seed (int | Unset): Shuffle seed for random ordering. Reuse it across pages; change it to
            reshuffle. Other sort modes ignore it Default: 0.
        group_translations (bool | Unset): Present each set of translated recipes once, as the
            rendition the preferred languages choose among those that match
        languages (str | Unset): Comma-separated BCP 47 content languages in order of preference,
            used when grouping translations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ListRecipesOutputBody
     """


    return sync_detailed(
        client=client,
limit=limit,
offset=offset,
q=q,
state=state,
sort=sort,
seed=seed,
group_translations=group_translations,
languages=languages,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    q: str | Unset = UNSET,
    state: ListRecipesState | Unset = ListRecipesState.ACTIVE,
    sort: ListRecipesSort | Unset = ListRecipesSort.RELEVANCE,
    seed: int | Unset = 0,
    group_translations: bool | Unset = UNSET,
    languages: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | ListRecipesOutputBody]:
    """ List recipes

    Args:
        limit (int | Unset): Maximum number of entries to return Default: 50.
        offset (int | Unset): Number of entries to skip Default: 0.
        q (str | Unset): Recipe text with bounded title/author typo matching and structured
            filters. author: requires full author-name membership with Unicode case, NFC, and
            whitespace normalization; accents and punctuation are preserved. ingredient: requires
            literal word-prefix matches within one ingredient name, including optional and alternative
            names, with original-line fallback only when that name is absent
        state (ListRecipesState | Unset): Library state to list Default: ListRecipesState.ACTIVE.
        sort (ListRecipesSort | Unset): Recipe list ordering Default: ListRecipesSort.RELEVANCE.
        seed (int | Unset): Shuffle seed for random ordering. Reuse it across pages; change it to
            reshuffle. Other sort modes ignore it Default: 0.
        group_translations (bool | Unset): Present each set of translated recipes once, as the
            rendition the preferred languages choose among those that match
        languages (str | Unset): Comma-separated BCP 47 content languages in order of preference,
            used when grouping translations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ListRecipesOutputBody]
     """


    kwargs = _get_kwargs(
        limit=limit,
offset=offset,
q=q,
state=state,
sort=sort,
seed=seed,
group_translations=group_translations,
languages=languages,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    q: str | Unset = UNSET,
    state: ListRecipesState | Unset = ListRecipesState.ACTIVE,
    sort: ListRecipesSort | Unset = ListRecipesSort.RELEVANCE,
    seed: int | Unset = 0,
    group_translations: bool | Unset = UNSET,
    languages: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | ListRecipesOutputBody | None:
    """ List recipes

    Args:
        limit (int | Unset): Maximum number of entries to return Default: 50.
        offset (int | Unset): Number of entries to skip Default: 0.
        q (str | Unset): Recipe text with bounded title/author typo matching and structured
            filters. author: requires full author-name membership with Unicode case, NFC, and
            whitespace normalization; accents and punctuation are preserved. ingredient: requires
            literal word-prefix matches within one ingredient name, including optional and alternative
            names, with original-line fallback only when that name is absent
        state (ListRecipesState | Unset): Library state to list Default: ListRecipesState.ACTIVE.
        sort (ListRecipesSort | Unset): Recipe list ordering Default: ListRecipesSort.RELEVANCE.
        seed (int | Unset): Shuffle seed for random ordering. Reuse it across pages; change it to
            reshuffle. Other sort modes ignore it Default: 0.
        group_translations (bool | Unset): Present each set of translated recipes once, as the
            rendition the preferred languages choose among those that match
        languages (str | Unset): Comma-separated BCP 47 content languages in order of preference,
            used when grouping translations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ListRecipesOutputBody
     """


    return (await asyncio_detailed(
        client=client,
limit=limit,
offset=offset,
q=q,
state=state,
sort=sort,
seed=seed,
group_translations=group_translations,
languages=languages,

    )).parsed
