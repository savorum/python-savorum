from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.bulk_item_result_status import BulkItemResultStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.import_job_item_resource import ImportJobItemResource
  from ..models.library_entry import LibraryEntry





T = TypeVar("T", bound="BulkItemResult")



@_attrs_define
class BulkItemResult:
    """ 
        Attributes:
            id (str):
            status (BulkItemResultStatus):
            book_revision (int | Unset):
            code (str | Unset):
            current_revision (int | Unset):
            import_ (ImportJobItemResource | Unset):
            recipe (LibraryEntry | Unset):
            revision (int | Unset):
     """

    id: str
    status: BulkItemResultStatus
    book_revision: int | Unset = UNSET
    code: str | Unset = UNSET
    current_revision: int | Unset = UNSET
    import_: ImportJobItemResource | Unset = UNSET
    recipe: LibraryEntry | Unset = UNSET
    revision: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.import_job_item_resource import ImportJobItemResource # noqa: PLC0415
        from ..models.library_entry import LibraryEntry # noqa: PLC0415
        id = self.id

        status = self.status.value

        book_revision = self.book_revision

        code = self.code

        current_revision = self.current_revision

        import_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.import_, Unset):
            import_ = self.import_.to_dict()

        recipe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recipe, Unset):
            recipe = self.recipe.to_dict()

        revision = self.revision


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "status": status,
        })
        if book_revision is not UNSET:
            field_dict["book_revision"] = book_revision
        if code is not UNSET:
            field_dict["code"] = code
        if current_revision is not UNSET:
            field_dict["current_revision"] = current_revision
        if import_ is not UNSET:
            field_dict["import"] = import_
        if recipe is not UNSET:
            field_dict["recipe"] = recipe
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_job_item_resource import ImportJobItemResource # noqa: PLC0415
        from ..models.library_entry import LibraryEntry # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        status = BulkItemResultStatus(d.pop("status"))




        book_revision = d.pop("book_revision", UNSET)

        code = d.pop("code", UNSET)

        current_revision = d.pop("current_revision", UNSET)

        _import_ = d.pop("import", UNSET)
        import_: ImportJobItemResource | Unset
        if isinstance(_import_,  Unset):
            import_ = UNSET
        else:
            import_ = ImportJobItemResource.from_dict(_import_)




        _recipe = d.pop("recipe", UNSET)
        recipe: LibraryEntry | Unset
        if isinstance(_recipe,  Unset):
            recipe = UNSET
        else:
            recipe = LibraryEntry.from_dict(_recipe)




        revision = d.pop("revision", UNSET)

        bulk_item_result = cls(
            id=id,
            status=status,
            book_revision=book_revision,
            code=code,
            current_revision=current_revision,
            import_=import_,
            recipe=recipe,
            revision=revision,
        )


        bulk_item_result.additional_properties = d
        return bulk_item_result

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
