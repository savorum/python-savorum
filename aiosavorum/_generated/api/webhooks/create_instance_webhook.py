from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.error_model import ErrorModel
from ...models.grant import Grant
from ...models.input_ import Input
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: Input,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/instance-webhooks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | ErrorModel | Grant:
    if response.status_code == 201:
        response_201 = Grant.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    if response.status_code == 409:
        response_409 = ErrorModel.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = ErrorModel.from_dict(response.json())



        return response_422

    if response.status_code == 429:
        response_429 = ErrorModel.from_dict(response.json())



        return response_429

    if response.status_code == 503:
        response_503 = ErrorModel.from_dict(response.json())



        return response_503

    response_default = ErrorModel.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | ErrorModel | Grant]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: Input,
    idempotency_key: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | Grant]:
    """ Create instance webhook

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
    queued work but do not subscribe to new events. Creation accepts Idempotency-Key; reuse it only with
    the same request. Receipts last at least 24 hours.

    Args:
        idempotency_key (str | Unset):
        body (Input):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | Grant]
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
    body: Input,
    idempotency_key: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | Grant | None:
    """ Create instance webhook

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
    queued work but do not subscribe to new events. Creation accepts Idempotency-Key; reuse it only with
    the same request. Receipts last at least 24 hours.

    Args:
        idempotency_key (str | Unset):
        body (Input):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | Grant
     """


    return sync_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: Input,
    idempotency_key: str | Unset = UNSET,

) -> Response[AccountProblem | ErrorModel | Grant]:
    """ Create instance webhook

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
    queued work but do not subscribe to new events. Creation accepts Idempotency-Key; reuse it only with
    the same request. Receipts last at least 24 hours.

    Args:
        idempotency_key (str | Unset):
        body (Input):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | ErrorModel | Grant]
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
    body: Input,
    idempotency_key: str | Unset = UNSET,

) -> AccountProblem | ErrorModel | Grant | None:
    """ Create instance webhook

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
    queued work but do not subscribe to new events. Creation accepts Idempotency-Key; reuse it only with
    the same request. Receipts last at least 24 hours.

    Args:
        idempotency_key (str | Unset):
        body (Input):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | ErrorModel | Grant
     """


    return (await asyncio_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
