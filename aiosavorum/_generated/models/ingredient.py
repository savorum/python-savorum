from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ingredient_relation import IngredientRelation
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.normalization import Normalization
  from ..models.quantity import Quantity
  from ..models.recipe_dependency import RecipeDependency
  from ..models.simple_quantity import SimpleQuantity
  from ..models.temperature import Temperature





T = TypeVar("T", bound="Ingredient")



@_attrs_define
class Ingredient:
    """ 
        Attributes:
            id (str):
            alternatives (list[Ingredient] | None | Unset): Ordered complete authored branches; nested choices are refused
            name (str | Unset):
            normalization (Normalization | Unset):
            note (str | Unset):
            optional (bool | Unset): The author sanctioned leaving this occurrence out. It belongs to the occurrence, never
                to the ingredient: the same thing may be optional in a garnish section and required by the method
            package_size (SimpleQuantity | Unset):
            quantity (Quantity | Unset):
            recipe (RecipeDependency | Unset):
            relation (IngredientRelation | Unset):
            source_text (str | Unset):
            temperature (Temperature | Unset):
     """

    id: str
    alternatives: list[Ingredient] | None | Unset = UNSET
    name: str | Unset = UNSET
    normalization: Normalization | Unset = UNSET
    note: str | Unset = UNSET
    optional: bool | Unset = UNSET
    package_size: SimpleQuantity | Unset = UNSET
    quantity: Quantity | Unset = UNSET
    recipe: RecipeDependency | Unset = UNSET
    relation: IngredientRelation | Unset = UNSET
    source_text: str | Unset = UNSET
    temperature: Temperature | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.normalization import Normalization # noqa: PLC0415
        from ..models.quantity import Quantity # noqa: PLC0415
        from ..models.recipe_dependency import RecipeDependency # noqa: PLC0415
        from ..models.simple_quantity import SimpleQuantity # noqa: PLC0415
        from ..models.temperature import Temperature # noqa: PLC0415
        id = self.id

        alternatives: list[dict[str, Any]] | None | Unset
        if isinstance(self.alternatives, Unset):
            alternatives = UNSET
        elif isinstance(self.alternatives, list):
            alternatives = []
            for alternatives_type_0_item_data in self.alternatives:
                alternatives_type_0_item = alternatives_type_0_item_data.to_dict()
                alternatives.append(alternatives_type_0_item)


        else:
            alternatives = self.alternatives

        name = self.name

        normalization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.normalization, Unset):
            normalization = self.normalization.to_dict()

        note = self.note

        optional = self.optional

        package_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_size, Unset):
            package_size = self.package_size.to_dict()

        quantity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quantity, Unset):
            quantity = self.quantity.to_dict()

        recipe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recipe, Unset):
            recipe = self.recipe.to_dict()

        relation: str | Unset = UNSET
        if not isinstance(self.relation, Unset):
            relation = self.relation.value


        source_text = self.source_text

        temperature: dict[str, Any] | Unset = UNSET
        if not isinstance(self.temperature, Unset):
            temperature = self.temperature.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
        })
        if alternatives is not UNSET:
            field_dict["alternatives"] = alternatives
        if name is not UNSET:
            field_dict["name"] = name
        if normalization is not UNSET:
            field_dict["normalization"] = normalization
        if note is not UNSET:
            field_dict["note"] = note
        if optional is not UNSET:
            field_dict["optional"] = optional
        if package_size is not UNSET:
            field_dict["package_size"] = package_size
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if recipe is not UNSET:
            field_dict["recipe"] = recipe
        if relation is not UNSET:
            field_dict["relation"] = relation
        if source_text is not UNSET:
            field_dict["source_text"] = source_text
        if temperature is not UNSET:
            field_dict["temperature"] = temperature

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.normalization import Normalization # noqa: PLC0415
        from ..models.quantity import Quantity # noqa: PLC0415
        from ..models.recipe_dependency import RecipeDependency # noqa: PLC0415
        from ..models.simple_quantity import SimpleQuantity # noqa: PLC0415
        from ..models.temperature import Temperature # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_alternatives(data: object) -> list[Ingredient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alternatives_type_0 = []
                _alternatives_type_0 = data
                for alternatives_type_0_item_data in (_alternatives_type_0):
                    alternatives_type_0_item = Ingredient.from_dict(alternatives_type_0_item_data)



                    alternatives_type_0.append(alternatives_type_0_item)

                return alternatives_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ingredient] | None | Unset, data)

        alternatives = _parse_alternatives(d.pop("alternatives", UNSET))


        name = d.pop("name", UNSET)

        _normalization = d.pop("normalization", UNSET)
        normalization: Normalization | Unset
        if isinstance(_normalization,  Unset):
            normalization = UNSET
        else:
            normalization = Normalization.from_dict(_normalization)




        note = d.pop("note", UNSET)

        optional = d.pop("optional", UNSET)

        _package_size = d.pop("package_size", UNSET)
        package_size: SimpleQuantity | Unset
        if isinstance(_package_size,  Unset):
            package_size = UNSET
        else:
            package_size = SimpleQuantity.from_dict(_package_size)




        _quantity = d.pop("quantity", UNSET)
        quantity: Quantity | Unset
        if isinstance(_quantity,  Unset):
            quantity = UNSET
        else:
            quantity = Quantity.from_dict(_quantity)




        _recipe = d.pop("recipe", UNSET)
        recipe: RecipeDependency | Unset
        if isinstance(_recipe,  Unset):
            recipe = UNSET
        else:
            recipe = RecipeDependency.from_dict(_recipe)




        _relation = d.pop("relation", UNSET)
        relation: IngredientRelation | Unset
        if isinstance(_relation,  Unset):
            relation = UNSET
        else:
            relation = IngredientRelation(_relation)




        source_text = d.pop("source_text", UNSET)

        _temperature = d.pop("temperature", UNSET)
        temperature: Temperature | Unset
        if isinstance(_temperature,  Unset):
            temperature = UNSET
        else:
            temperature = Temperature.from_dict(_temperature)




        ingredient = cls(
            id=id,
            alternatives=alternatives,
            name=name,
            normalization=normalization,
            note=note,
            optional=optional,
            package_size=package_size,
            quantity=quantity,
            recipe=recipe,
            relation=relation,
            source_text=source_text,
            temperature=temperature,
        )

        return ingredient

