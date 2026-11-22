from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.import_preview_match_evidence import ImportPreviewMatchEvidence
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ImportPreviewMatch")



@_attrs_define
class ImportPreviewMatch:
    """ 
        Attributes:
            authors (list[str] | None):
            entry_id (str):
            evidence (ImportPreviewMatchEvidence):
            ingredient_count (int):
            recipe_id (str):
            revision (int):
            score (float):
            title (str):
            yield_ (str | Unset):
     """

    authors: list[str] | None
    entry_id: str
    evidence: ImportPreviewMatchEvidence
    ingredient_count: int
    recipe_id: str
    revision: int
    score: float
    title: str
    yield_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        authors: list[str] | None
        if isinstance(self.authors, list):
            authors = self.authors


        else:
            authors = self.authors

        entry_id = self.entry_id

        evidence = self.evidence.value

        ingredient_count = self.ingredient_count

        recipe_id = self.recipe_id

        revision = self.revision

        score = self.score

        title = self.title

        yield_ = self.yield_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "authors": authors,
            "entry_id": entry_id,
            "evidence": evidence,
            "ingredient_count": ingredient_count,
            "recipe_id": recipe_id,
            "revision": revision,
            "score": score,
            "title": title,
        })
        if yield_ is not UNSET:
            field_dict["yield"] = yield_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_authors(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                authors_type_0 = cast(list[str], data)

                return authors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        authors = _parse_authors(d.pop("authors"))


        entry_id = d.pop("entry_id")

        evidence = ImportPreviewMatchEvidence(d.pop("evidence"))




        ingredient_count = d.pop("ingredient_count")

        recipe_id = d.pop("recipe_id")

        revision = d.pop("revision")

        score = d.pop("score")

        title = d.pop("title")

        yield_ = d.pop("yield", UNSET)

        import_preview_match = cls(
            authors=authors,
            entry_id=entry_id,
            evidence=evidence,
            ingredient_count=ingredient_count,
            recipe_id=recipe_id,
            revision=revision,
            score=score,
            title=title,
            yield_=yield_,
        )


        import_preview_match.additional_properties = d
        return import_preview_match

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
