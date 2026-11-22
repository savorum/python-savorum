from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.normalization_method import NormalizationMethod
from ..models.normalization_review import NormalizationReview
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Normalization")



@_attrs_define
class Normalization:
    """ 
        Attributes:
            method (NormalizationMethod):
            review (NormalizationReview | Unset):
            warnings (list[str] | None | Unset):
     """

    method: NormalizationMethod
    review: NormalizationReview | Unset = UNSET
    warnings: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        review: str | Unset = UNSET
        if not isinstance(self.review, Unset):
            review = self.review.value


        warnings: list[str] | None | Unset
        if isinstance(self.warnings, Unset):
            warnings = UNSET
        elif isinstance(self.warnings, list):
            warnings = self.warnings


        else:
            warnings = self.warnings


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "method": method,
        })
        if review is not UNSET:
            field_dict["review"] = review
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = NormalizationMethod(d.pop("method"))




        _review = d.pop("review", UNSET)
        review: NormalizationReview | Unset
        if isinstance(_review,  Unset):
            review = UNSET
        else:
            review = NormalizationReview(_review)




        def _parse_warnings(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = cast(list[str], data)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))


        normalization = cls(
            method=method,
            review=review,
            warnings=warnings,
        )

        return normalization

