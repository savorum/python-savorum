from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_native_link_ticket_body_code_challenge_method import CreateNativeLinkTicketBodyCodeChallengeMethod






T = TypeVar("T", bound="CreateNativeLinkTicketBody")



@_attrs_define
class CreateNativeLinkTicketBody:
    """ 
        Attributes:
            code_challenge (str): Base64url SHA-256 of the app's code verifier, without padding. The native entry must
                present the same challenge.
            code_challenge_method (CreateNativeLinkTicketBodyCodeChallengeMethod):
     """

    code_challenge: str
    code_challenge_method: CreateNativeLinkTicketBodyCodeChallengeMethod





    def to_dict(self) -> dict[str, Any]:
        code_challenge = self.code_challenge

        code_challenge_method = self.code_challenge_method.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "code_challenge": code_challenge,
            "code_challenge_method": code_challenge_method,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code_challenge = d.pop("code_challenge")

        code_challenge_method = CreateNativeLinkTicketBodyCodeChallengeMethod(d.pop("code_challenge_method"))




        create_native_link_ticket_body = cls(
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
        )

        return create_native_link_ticket_body

