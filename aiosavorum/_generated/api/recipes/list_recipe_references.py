from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.list_recipe_references_output_body import ListRecipeReferencesOutputBody
from ...models.list_recipe_references_state import ListRecipeReferencesState
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    state: ListRecipeReferencesState | Unset = ListRecipeReferencesState.ACTIVE,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/recipe-references",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | ListRecipeReferencesOutputBody | None:
    if response.status_code == 200:
        response_200 = ListRecipeReferencesOutputBody.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | ListRecipeReferencesOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    state: ListRecipeReferencesState | Unset = ListRecipeReferencesState.ACTIVE,

) -> Response[AccountProblem | ErrorModel | ListRecipeReferencesOutputBody]:
    """ List recipe references

    Args:
        state (ListRecipeReferencesState | Unset): Library state to list Default:
            ListRecipeReferencesState.ACTIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ListRecipeReferencesOutputBody]
     """


    kwargs = _get_kwargs(
        state=state,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    state: ListRecipeReferencesState | Unset = ListRecipeReferencesState.ACTIVE,

) -> AccountProblem | ErrorModel | ListRecipeReferencesOutputBody | None:
    """ List recipe references

    Args:
        state (ListRecipeReferencesState | Unset): Library state to list Default:
            ListRecipeReferencesState.ACTIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ListRecipeReferencesOutputBody
     """


    return sync_detailed(
        client=client,
state=state,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    state: ListRecipeReferencesState | Unset = ListRecipeReferencesState.ACTIVE,

) -> Response[AccountProblem | ErrorModel | ListRecipeReferencesOutputBody]:
    """ List recipe references

    Args:
        state (ListRecipeReferencesState | Unset): Library state to list Default:
            ListRecipeReferencesState.ACTIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | ListRecipeReferencesOutputBody]
     """


    kwargs = _get_kwargs(
        state=state,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    state: ListRecipeReferencesState | Unset = ListRecipeReferencesState.ACTIVE,

) -> AccountProblem | ErrorModel | ListRecipeReferencesOutputBody | None:
    """ List recipe references

    Args:
        state (ListRecipeReferencesState | Unset): Library state to list Default:
            ListRecipeReferencesState.ACTIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | ListRecipeReferencesOutputBody
     """


    return (await asyncio_detailed(
        client=client,
state=state,

    )).parsed
