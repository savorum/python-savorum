from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.subscription import Subscription
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/webhooks",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | list[Subscription] | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> list[Subscription] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = []
                _response_200_type_0 = data
                for response_200_type_0_item_data in (_response_200_type_0):
                    response_200_type_0_item = Subscription.from_dict(response_200_type_0_item_data)



                    response_200_type_0.append(response_200_type_0_item)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Subscription] | None, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = ErrorModel.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | list[Subscription] | None]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | ErrorModel | list[Subscription] | None]:
    """ List library webhooks

     Library owners manage this library's subscriptions. Instance administrators manage instance
    security-event subscriptions through /instance-webhooks. Personal tokens cannot manage either.
    Destinations require HTTPS and public DNS addresses unless a deployment operator explicitly trusts a
    private CIDR. DNS is checked on each connection; up to three method-preserving HTTPS redirects are
    revalidated before following. Events contain IDs and minimal facts, never recipe bodies or
    credentials. Delivery is at least once. Receivers verify the exact body with HMAC-SHA256 over
    timestamp + '.' + body using Savorum-Signature: t=<Unix seconds>,v1=<hex>, reject timestamps outside
    five minutes, then persistently deduplicate delivery_id. Savorum-Delivery-ID and Savorum-Event-ID
    also occur inside the signed body. Secrets appear once on create or rotate. Rotation immediately
    invalidates the old key for future attempts, including queued retries. Keep signing-key files with
    private instance backups. Retries cover network failures, 408, 429, and 5xx: up to eight attempts
    per cycle within 24 hours, exponential delay from 15 seconds with jitter, capped at one hour,
    honoring bounded Retry-After. Other statuses end the cycle. History retains up to 1000 finished
    deliveries per subscription for 30 days and 32 attempts per delivery. Repeated final failures
    automatically pause delivery; fix the receiver before re-enabling. Paused subscriptions retain
    queued work but do not subscribe to new events.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | list[Subscription] | None]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | ErrorModel | list[Subscription] | None | None:
    """ List library webhooks

     Library owners manage this library's subscriptions. Instance administrators manage instance
    security-event subscriptions through /instance-webhooks. Personal tokens cannot manage either.
    Destinations require HTTPS and public DNS addresses unless a deployment operator explicitly trusts a
    private CIDR. DNS is checked on each connection; up to three method-preserving HTTPS redirects are
    revalidated before following. Events contain IDs and minimal facts, never recipe bodies or
    credentials. Delivery is at least once. Receivers verify the exact body with HMAC-SHA256 over
    timestamp + '.' + body using Savorum-Signature: t=<Unix seconds>,v1=<hex>, reject timestamps outside
    five minutes, then persistently deduplicate delivery_id. Savorum-Delivery-ID and Savorum-Event-ID
    also occur inside the signed body. Secrets appear once on create or rotate. Rotation immediately
    invalidates the old key for future attempts, including queued retries. Keep signing-key files with
    private instance backups. Retries cover network failures, 408, 429, and 5xx: up to eight attempts
    per cycle within 24 hours, exponential delay from 15 seconds with jitter, capped at one hour,
    honoring bounded Retry-After. Other statuses end the cycle. History retains up to 1000 finished
    deliveries per subscription for 30 days and 32 attempts per delivery. Repeated final failures
    automatically pause delivery; fix the receiver before re-enabling. Paused subscriptions retain
    queued work but do not subscribe to new events.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | list[Subscription] | None
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountProblem | ErrorModel | list[Subscription] | None]:
    """ List library webhooks

     Library owners manage this library's subscriptions. Instance administrators manage instance
    security-event subscriptions through /instance-webhooks. Personal tokens cannot manage either.
    Destinations require HTTPS and public DNS addresses unless a deployment operator explicitly trusts a
    private CIDR. DNS is checked on each connection; up to three method-preserving HTTPS redirects are
    revalidated before following. Events contain IDs and minimal facts, never recipe bodies or
    credentials. Delivery is at least once. Receivers verify the exact body with HMAC-SHA256 over
    timestamp + '.' + body using Savorum-Signature: t=<Unix seconds>,v1=<hex>, reject timestamps outside
    five minutes, then persistently deduplicate delivery_id. Savorum-Delivery-ID and Savorum-Event-ID
    also occur inside the signed body. Secrets appear once on create or rotate. Rotation immediately
    invalidates the old key for future attempts, including queued retries. Keep signing-key files with
    private instance backups. Retries cover network failures, 408, 429, and 5xx: up to eight attempts
    per cycle within 24 hours, exponential delay from 15 seconds with jitter, capped at one hour,
    honoring bounded Retry-After. Other statuses end the cycle. History retains up to 1000 finished
    deliveries per subscription for 30 days and 32 attempts per delivery. Repeated final failures
    automatically pause delivery; fix the receiver before re-enabling. Paused subscriptions retain
    queued work but do not subscribe to new events.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | list[Subscription] | None]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> AccountProblem | ErrorModel | list[Subscription] | None | None:
    """ List library webhooks

     Library owners manage this library's subscriptions. Instance administrators manage instance
    security-event subscriptions through /instance-webhooks. Personal tokens cannot manage either.
    Destinations require HTTPS and public DNS addresses unless a deployment operator explicitly trusts a
    private CIDR. DNS is checked on each connection; up to three method-preserving HTTPS redirects are
    revalidated before following. Events contain IDs and minimal facts, never recipe bodies or
    credentials. Delivery is at least once. Receivers verify the exact body with HMAC-SHA256 over
    timestamp + '.' + body using Savorum-Signature: t=<Unix seconds>,v1=<hex>, reject timestamps outside
    five minutes, then persistently deduplicate delivery_id. Savorum-Delivery-ID and Savorum-Event-ID
    also occur inside the signed body. Secrets appear once on create or rotate. Rotation immediately
    invalidates the old key for future attempts, including queued retries. Keep signing-key files with
    private instance backups. Retries cover network failures, 408, 429, and 5xx: up to eight attempts
    per cycle within 24 hours, exponential delay from 15 seconds with jitter, capped at one hour,
    honoring bounded Retry-After. Other statuses end the cycle. History retains up to 1000 finished
    deliveries per subscription for 30 days and 32 attempts per delivery. Repeated final failures
    automatically pause delivery; fix the receiver before re-enabling. Paused subscriptions retain
    queued work but do not subscribe to new events.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | list[Subscription] | None
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
