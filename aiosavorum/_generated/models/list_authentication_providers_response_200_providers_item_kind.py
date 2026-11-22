from enum import StrEnum

class ListAuthenticationProvidersResponse200ProvidersItemKind(StrEnum):
    LDAP = "ldap"
    MANAGED = "managed"
    OIDC = "oidc"
    PROXY = "proxy"
    SAML = "saml"

    def __str__(self) -> str:
        return str(self.value)
