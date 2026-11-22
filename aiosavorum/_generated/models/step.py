from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ingredient_use import IngredientUse
  from ..models.temperature import Temperature





T = TypeVar("T", bound="Step")



@_attrs_define
class Step:
    """ 
        Attributes:
            id (str):
            image_refs (list[str] | None | Unset):
            ingredient_uses (list[IngredientUse] | None | Unset):
            temperatures (list[Temperature] | None | Unset):
            text (str | Unset): Instruction prose; a step requires a title or text
            timing_refs (list[str] | None | Unset): Canonical timing assertions this step is associated with
            title (str | Unset): Optional authored heading for this instruction
     """

    id: str
    image_refs: list[str] | None | Unset = UNSET
    ingredient_uses: list[IngredientUse] | None | Unset = UNSET
    temperatures: list[Temperature] | None | Unset = UNSET
    text: str | Unset = UNSET
    timing_refs: list[str] | None | Unset = UNSET
    title: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.ingredient_use import IngredientUse # noqa: PLC0415
        from ..models.temperature import Temperature # noqa: PLC0415
        id = self.id

        image_refs: list[str] | None | Unset
        if isinstance(self.image_refs, Unset):
            image_refs = UNSET
        elif isinstance(self.image_refs, list):
            image_refs = self.image_refs


        else:
            image_refs = self.image_refs

        ingredient_uses: list[dict[str, Any]] | None | Unset
        if isinstance(self.ingredient_uses, Unset):
            ingredient_uses = UNSET
        elif isinstance(self.ingredient_uses, list):
            ingredient_uses = []
            for ingredient_uses_type_0_item_data in self.ingredient_uses:
                ingredient_uses_type_0_item = ingredient_uses_type_0_item_data.to_dict()
                ingredient_uses.append(ingredient_uses_type_0_item)


        else:
            ingredient_uses = self.ingredient_uses

        temperatures: list[dict[str, Any]] | None | Unset
        if isinstance(self.temperatures, Unset):
            temperatures = UNSET
        elif isinstance(self.temperatures, list):
            temperatures = []
            for temperatures_type_0_item_data in self.temperatures:
                temperatures_type_0_item = temperatures_type_0_item_data.to_dict()
                temperatures.append(temperatures_type_0_item)


        else:
            temperatures = self.temperatures

        text = self.text

        timing_refs: list[str] | None | Unset
        if isinstance(self.timing_refs, Unset):
            timing_refs = UNSET
        elif isinstance(self.timing_refs, list):
            timing_refs = self.timing_refs


        else:
            timing_refs = self.timing_refs

        title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
        })
        if image_refs is not UNSET:
            field_dict["image_refs"] = image_refs
        if ingredient_uses is not UNSET:
            field_dict["ingredient_uses"] = ingredient_uses
        if temperatures is not UNSET:
            field_dict["temperatures"] = temperatures
        if text is not UNSET:
            field_dict["text"] = text
        if timing_refs is not UNSET:
            field_dict["timing_refs"] = timing_refs
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ingredient_use import IngredientUse # noqa: PLC0415
        from ..models.temperature import Temperature # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_image_refs(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_refs_type_0 = cast(list[str], data)

                return image_refs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        image_refs = _parse_image_refs(d.pop("image_refs", UNSET))


        def _parse_ingredient_uses(data: object) -> list[IngredientUse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ingredient_uses_type_0 = []
                _ingredient_uses_type_0 = data
                for ingredient_uses_type_0_item_data in (_ingredient_uses_type_0):
                    ingredient_uses_type_0_item = IngredientUse.from_dict(ingredient_uses_type_0_item_data)



                    ingredient_uses_type_0.append(ingredient_uses_type_0_item)

                return ingredient_uses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IngredientUse] | None | Unset, data)

        ingredient_uses = _parse_ingredient_uses(d.pop("ingredient_uses", UNSET))


        def _parse_temperatures(data: object) -> list[Temperature] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                temperatures_type_0 = []
                _temperatures_type_0 = data
                for temperatures_type_0_item_data in (_temperatures_type_0):
                    temperatures_type_0_item = Temperature.from_dict(temperatures_type_0_item_data)



                    temperatures_type_0.append(temperatures_type_0_item)

                return temperatures_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Temperature] | None | Unset, data)

        temperatures = _parse_temperatures(d.pop("temperatures", UNSET))


        text = d.pop("text", UNSET)

        def _parse_timing_refs(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                timing_refs_type_0 = cast(list[str], data)

                return timing_refs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        timing_refs = _parse_timing_refs(d.pop("timing_refs", UNSET))


        title = d.pop("title", UNSET)

        step = cls(
            id=id,
            image_refs=image_refs,
            ingredient_uses=ingredient_uses,
            temperatures=temperatures,
            text=text,
            timing_refs=timing_refs,
            title=title,
        )

        return step

