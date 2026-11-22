from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.personal_token import PersonalToken
  from ..models.token_policy import TokenPolicy





T = TypeVar("T", bound="TokenListResponse")



@_attrs_define
class TokenListResponse:
    """ 
        Attributes:
            policy (TokenPolicy):
            tokens (list[PersonalToken] | None):
     """

    policy: TokenPolicy
    tokens: list[PersonalToken] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.personal_token import PersonalToken # noqa: PLC0415
        from ..models.token_policy import TokenPolicy # noqa: PLC0415
        policy = self.policy.to_dict()

        tokens: list[dict[str, Any]] | None
        if isinstance(self.tokens, list):
            tokens = []
            for tokens_type_0_item_data in self.tokens:
                tokens_type_0_item = tokens_type_0_item_data.to_dict()
                tokens.append(tokens_type_0_item)


        else:
            tokens = self.tokens


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "policy": policy,
            "tokens": tokens,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.personal_token import PersonalToken # noqa: PLC0415
        from ..models.token_policy import TokenPolicy # noqa: PLC0415
        d = dict(src_dict)
        policy = TokenPolicy.from_dict(d.pop("policy"))




        def _parse_tokens(data: object) -> list[PersonalToken] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tokens_type_0 = []
                _tokens_type_0 = data
                for tokens_type_0_item_data in (_tokens_type_0):
                    tokens_type_0_item = PersonalToken.from_dict(tokens_type_0_item_data)



                    tokens_type_0.append(tokens_type_0_item)

                return tokens_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PersonalToken] | None, data)

        tokens = _parse_tokens(d.pop("tokens"))


        token_list_response = cls(
            policy=policy,
            tokens=tokens,
        )


        token_list_response.additional_properties = d
        return token_list_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
