from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_problem import AccountProblem
from ...models.capabilities import Capabilities
from ...models.error_model import ErrorModel
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/capabilities",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> AccountProblem | Capabilities | ErrorModel:
    if response.status_code == 200:
        response_200 = Capabilities.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountProblem.from_dict(response.json())



        return response_401

    response_default = ErrorModel.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[AccountProblem | Capabilities | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[AccountProblem | Capabilities | ErrorModel]:
    """ Discover capabilities

     Unauthenticated requests return product, API compatibility, interactive sign-in methods, and sign-in
    features only. `auth.native_browser_sign_in` means browser sign-in can return to a native app
    through `begin-native-browser-login`, `complete-native-browser-login`, and `finish-native-provider-
    login`. `auth.native_sign_in` means a native app can complete OIDC, SAML, and managed sign-in
    through `begin-native-provider-login` and `finish-native-provider-login`. `auth.native_link` means a
    signed-in native app can link an OIDC or SAML identity through `create-native-link-ticket`, `begin-
    native-provider-login`, and `finish-native-provider-link`. `auth.managed_session` means a managed
    provider is configured and its web and native sign-in use short-lived, tenant-audienced grants after
    PKCE code redemption. `auth.managed_native_session` means a native client can redeem a scoped
    hosting grant through `finish-managed-native-login` for an ordinary local session. Every response
    links to this instance's guide, OpenAPI description, and token page. Authenticated requests add
    registered formats, optional features, and enforced bounds, and a request made with a personal API
    token adds that token's scopes, libraries, and expiry. `recipes.search.ingredient` means ingredient:
    queries match indexed ingredient names, including optional and alternative names, with original-line
    fallback only when the name is absent. All words in one qualifier must match the same ingredient.
    Capabilities describe availability, not a grant of authorization. Schema version 1 permits additive
    optional fields and new IDs; clients ignore unknown IDs. Cache for the current session and refresh
    after reconnect or configuration changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | Capabilities | ErrorModel]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> AccountProblem | Capabilities | ErrorModel | None:
    """ Discover capabilities

     Unauthenticated requests return product, API compatibility, interactive sign-in methods, and sign-in
    features only. `auth.native_browser_sign_in` means browser sign-in can return to a native app
    through `begin-native-browser-login`, `complete-native-browser-login`, and `finish-native-provider-
    login`. `auth.native_sign_in` means a native app can complete OIDC, SAML, and managed sign-in
    through `begin-native-provider-login` and `finish-native-provider-login`. `auth.native_link` means a
    signed-in native app can link an OIDC or SAML identity through `create-native-link-ticket`, `begin-
    native-provider-login`, and `finish-native-provider-link`. `auth.managed_session` means a managed
    provider is configured and its web and native sign-in use short-lived, tenant-audienced grants after
    PKCE code redemption. `auth.managed_native_session` means a native client can redeem a scoped
    hosting grant through `finish-managed-native-login` for an ordinary local session. Every response
    links to this instance's guide, OpenAPI description, and token page. Authenticated requests add
    registered formats, optional features, and enforced bounds, and a request made with a personal API
    token adds that token's scopes, libraries, and expiry. `recipes.search.ingredient` means ingredient:
    queries match indexed ingredient names, including optional and alternative names, with original-line
    fallback only when the name is absent. All words in one qualifier must match the same ingredient.
    Capabilities describe availability, not a grant of authorization. Schema version 1 permits additive
    optional fields and new IDs; clients ignore unknown IDs. Cache for the current session and refresh
    after reconnect or configuration changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | Capabilities | ErrorModel
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[AccountProblem | Capabilities | ErrorModel]:
    """ Discover capabilities

     Unauthenticated requests return product, API compatibility, interactive sign-in methods, and sign-in
    features only. `auth.native_browser_sign_in` means browser sign-in can return to a native app
    through `begin-native-browser-login`, `complete-native-browser-login`, and `finish-native-provider-
    login`. `auth.native_sign_in` means a native app can complete OIDC, SAML, and managed sign-in
    through `begin-native-provider-login` and `finish-native-provider-login`. `auth.native_link` means a
    signed-in native app can link an OIDC or SAML identity through `create-native-link-ticket`, `begin-
    native-provider-login`, and `finish-native-provider-link`. `auth.managed_session` means a managed
    provider is configured and its web and native sign-in use short-lived, tenant-audienced grants after
    PKCE code redemption. `auth.managed_native_session` means a native client can redeem a scoped
    hosting grant through `finish-managed-native-login` for an ordinary local session. Every response
    links to this instance's guide, OpenAPI description, and token page. Authenticated requests add
    registered formats, optional features, and enforced bounds, and a request made with a personal API
    token adds that token's scopes, libraries, and expiry. `recipes.search.ingredient` means ingredient:
    queries match indexed ingredient names, including optional and alternative names, with original-line
    fallback only when the name is absent. All words in one qualifier must match the same ingredient.
    Capabilities describe availability, not a grant of authorization. Schema version 1 permits additive
    optional fields and new IDs; clients ignore unknown IDs. Cache for the current session and refresh
    after reconnect or configuration changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProblem | Capabilities | ErrorModel]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> AccountProblem | Capabilities | ErrorModel | None:
    """ Discover capabilities

     Unauthenticated requests return product, API compatibility, interactive sign-in methods, and sign-in
    features only. `auth.native_browser_sign_in` means browser sign-in can return to a native app
    through `begin-native-browser-login`, `complete-native-browser-login`, and `finish-native-provider-
    login`. `auth.native_sign_in` means a native app can complete OIDC, SAML, and managed sign-in
    through `begin-native-provider-login` and `finish-native-provider-login`. `auth.native_link` means a
    signed-in native app can link an OIDC or SAML identity through `create-native-link-ticket`, `begin-
    native-provider-login`, and `finish-native-provider-link`. `auth.managed_session` means a managed
    provider is configured and its web and native sign-in use short-lived, tenant-audienced grants after
    PKCE code redemption. `auth.managed_native_session` means a native client can redeem a scoped
    hosting grant through `finish-managed-native-login` for an ordinary local session. Every response
    links to this instance's guide, OpenAPI description, and token page. Authenticated requests add
    registered formats, optional features, and enforced bounds, and a request made with a personal API
    token adds that token's scopes, libraries, and expiry. `recipes.search.ingredient` means ingredient:
    queries match indexed ingredient names, including optional and alternative names, with original-line
    fallback only when the name is absent. All words in one qualifier must match the same ingredient.
    Capabilities describe availability, not a grant of authorization. Schema version 1 permits additive
    optional fields and new IDs; clients ignore unknown IDs. Cache for the current session and refresh
    after reconnect or configuration changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProblem | Capabilities | ErrorModel
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
