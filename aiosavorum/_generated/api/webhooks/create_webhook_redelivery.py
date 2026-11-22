from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.create_webhook_redelivery_response import CreateWebhookRedeliveryResponse
from ...models.error_model import ErrorModel
from typing import cast



def _get_kwargs(
    id: str,
    delivery_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/webhooks/{id}/deliveries/{delivery_id}/redeliver".format(id=quote(str(id), safe=""),delivery_id=quote(str(delivery_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | CreateWebhookRedeliveryResponse | ErrorModel:
    if response.status_code == 202:
        response_202 = CreateWebhookRedeliveryResponse.from_dict(response.json())



        return response_202

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = ErrorModel.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | CreateWebhookRedeliveryResponse | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | CreateWebhookRedeliveryResponse | ErrorModel]:
    """ Retry library delivery

    Args:
        id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | CreateWebhookRedeliveryResponse | ErrorModel]
     """


    kwargs = _get_kwargs(
        id=id,
delivery_id=delivery_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | CreateWebhookRedeliveryResponse | ErrorModel | None:
    """ Retry library delivery

    Args:
        id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | CreateWebhookRedeliveryResponse | ErrorModel
     """


    return sync_detailed(
        id=id,
delivery_id=delivery_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | CreateWebhookRedeliveryResponse | ErrorModel]:
    """ Retry library delivery

    Args:
        id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | CreateWebhookRedeliveryResponse | ErrorModel]
     """


    kwargs = _get_kwargs(
        id=id,
delivery_id=delivery_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | CreateWebhookRedeliveryResponse | ErrorModel | None:
    """ Retry library delivery

    Args:
        id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | CreateWebhookRedeliveryResponse | ErrorModel
     """


    return (await asyncio_detailed(
        id=id,
delivery_id=delivery_id,
client=client,

    )).parsed
