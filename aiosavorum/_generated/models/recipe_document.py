from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.allergen_declaration import AllergenDeclaration
  from ..models.asset import Asset
  from ..models.author import Author
  from ..models.dietary_claim import DietaryClaim
  from ..models.equipment import Equipment
  from ..models.ingredient_section import IngredientSection
  from ..models.instruction_section import InstructionSection
  from ..models.nutrition_statement import NutritionStatement
  from ..models.recipe_document_extensions_raw import RecipeDocumentExtensionsRaw
  from ..models.recipe_document_sref_opaque_raw import RecipeDocumentSrefOpaqueRaw
  from ..models.source import Source
  from ..models.times import Times
  from ..models.translation import Translation
  from ..models.variant import Variant
  from ..models.yield_ import Yield





T = TypeVar("T", bound="RecipeDocument")



@_attrs_define
class RecipeDocument:
    """ 
        Attributes:
            id (str): Portable recipe document identifier
            ingredient_sections (list[IngredientSection] | None):
            instruction_sections (list[InstructionSection] | None):
            schema_version (int):
            title (str):
            allergen_declarations (list[AllergenDeclaration] | None | Unset): Allergen presence, precaution, and absence the
                source stated; an unmentioned substance is unknown
            assets (list[Asset] | None | Unset):
            authors (list[Author] | None | Unset):
            categories (list[str] | None | Unset): Ordered source-authored broad classifications
            cooking_methods (list[str] | None | Unset): Ordered source-authored cooking-method labels
            courses (list[str] | None | Unset): Ordered source-authored meal-role classifications
            cuisines (list[str] | None | Unset):
            description (str | Unset):
            dietary_claims (list[DietaryClaim] | None | Unset): Dietary suitability the source stated; never derived from
                ingredients
            equipment (list[Equipment] | None | Unset): Ordered equipment the recipe identifies as required or expected;
                recipe content, not kitchen inventory
            extensions_raw (RecipeDocumentExtensionsRaw | Unset):
            image_refs (list[str] | None | Unset):
            keywords (list[str] | None | Unset):
            language (str | Unset):
            modified (str | Unset): Authored recipe or source-work modification date or date-time
            notes (list[str] | None | Unset):
            nutrition (list[NutritionStatement] | None | Unset): Authored nutrition statements, each with its own basis.
                Savorum does not calculate nutrition
            primary_image (str | Unset):
            published (str | Unset): Authored recipe or source-work publication date or date-time
            source (Source | Unset):
            source_locale (str | Unset):
            sref_opaque_raw (RecipeDocumentSrefOpaqueRaw | Unset):
            times (Times | Unset):
            translations (list[Translation] | None | Unset): Declared relationships to other renditions of this recipe in
                other languages. Each rendition is its own recipe; a relationship shares no content
            variants (list[Variant] | None | Unset): Authored alternate realizations of this recipe, in source order.
                Preserved content, not a machine-applicable delta: identify one as a variant and show what it says rather than
                trying to apply it
            yields (list[Yield] | None | Unset): Independent authored yield assertions in source order. None is primary;
                which one a reader scales by is their own state
     """

    id: str
    ingredient_sections: list[IngredientSection] | None
    instruction_sections: list[InstructionSection] | None
    schema_version: int
    title: str
    allergen_declarations: list[AllergenDeclaration] | None | Unset = UNSET
    assets: list[Asset] | None | Unset = UNSET
    authors: list[Author] | None | Unset = UNSET
    categories: list[str] | None | Unset = UNSET
    cooking_methods: list[str] | None | Unset = UNSET
    courses: list[str] | None | Unset = UNSET
    cuisines: list[str] | None | Unset = UNSET
    description: str | Unset = UNSET
    dietary_claims: list[DietaryClaim] | None | Unset = UNSET
    equipment: list[Equipment] | None | Unset = UNSET
    extensions_raw: RecipeDocumentExtensionsRaw | Unset = UNSET
    image_refs: list[str] | None | Unset = UNSET
    keywords: list[str] | None | Unset = UNSET
    language: str | Unset = UNSET
    modified: str | Unset = UNSET
    notes: list[str] | None | Unset = UNSET
    nutrition: list[NutritionStatement] | None | Unset = UNSET
    primary_image: str | Unset = UNSET
    published: str | Unset = UNSET
    source: Source | Unset = UNSET
    source_locale: str | Unset = UNSET
    sref_opaque_raw: RecipeDocumentSrefOpaqueRaw | Unset = UNSET
    times: Times | Unset = UNSET
    translations: list[Translation] | None | Unset = UNSET
    variants: list[Variant] | None | Unset = UNSET
    yields: list[Yield] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.allergen_declaration import AllergenDeclaration # noqa: PLC0415
        from ..models.asset import Asset # noqa: PLC0415
        from ..models.author import Author # noqa: PLC0415
        from ..models.dietary_claim import DietaryClaim # noqa: PLC0415
        from ..models.equipment import Equipment # noqa: PLC0415
        from ..models.ingredient_section import IngredientSection # noqa: PLC0415
        from ..models.instruction_section import InstructionSection # noqa: PLC0415
        from ..models.nutrition_statement import NutritionStatement # noqa: PLC0415
        from ..models.recipe_document_extensions_raw import RecipeDocumentExtensionsRaw # noqa: PLC0415
        from ..models.recipe_document_sref_opaque_raw import RecipeDocumentSrefOpaqueRaw # noqa: PLC0415
        from ..models.source import Source # noqa: PLC0415
        from ..models.times import Times # noqa: PLC0415
        from ..models.translation import Translation # noqa: PLC0415
        from ..models.variant import Variant # noqa: PLC0415
        from ..models.yield_ import Yield # noqa: PLC0415
        id = self.id

        ingredient_sections: list[dict[str, Any]] | None
        if isinstance(self.ingredient_sections, list):
            ingredient_sections = []
            for ingredient_sections_type_0_item_data in self.ingredient_sections:
                ingredient_sections_type_0_item = ingredient_sections_type_0_item_data.to_dict()
                ingredient_sections.append(ingredient_sections_type_0_item)


        else:
            ingredient_sections = self.ingredient_sections

        instruction_sections: list[dict[str, Any]] | None
        if isinstance(self.instruction_sections, list):
            instruction_sections = []
            for instruction_sections_type_0_item_data in self.instruction_sections:
                instruction_sections_type_0_item = instruction_sections_type_0_item_data.to_dict()
                instruction_sections.append(instruction_sections_type_0_item)


        else:
            instruction_sections = self.instruction_sections

        schema_version = self.schema_version

        title = self.title

        allergen_declarations: list[dict[str, Any]] | None | Unset
        if isinstance(self.allergen_declarations, Unset):
            allergen_declarations = UNSET
        elif isinstance(self.allergen_declarations, list):
            allergen_declarations = []
            for allergen_declarations_type_0_item_data in self.allergen_declarations:
                allergen_declarations_type_0_item = allergen_declarations_type_0_item_data.to_dict()
                allergen_declarations.append(allergen_declarations_type_0_item)


        else:
            allergen_declarations = self.allergen_declarations

        assets: list[dict[str, Any]] | None | Unset
        if isinstance(self.assets, Unset):
            assets = UNSET
        elif isinstance(self.assets, list):
            assets = []
            for assets_type_0_item_data in self.assets:
                assets_type_0_item = assets_type_0_item_data.to_dict()
                assets.append(assets_type_0_item)


        else:
            assets = self.assets

        authors: list[dict[str, Any]] | None | Unset
        if isinstance(self.authors, Unset):
            authors = UNSET
        elif isinstance(self.authors, list):
            authors = []
            for authors_type_0_item_data in self.authors:
                authors_type_0_item = authors_type_0_item_data.to_dict()
                authors.append(authors_type_0_item)


        else:
            authors = self.authors

        categories: list[str] | None | Unset
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = self.categories


        else:
            categories = self.categories

        cooking_methods: list[str] | None | Unset
        if isinstance(self.cooking_methods, Unset):
            cooking_methods = UNSET
        elif isinstance(self.cooking_methods, list):
            cooking_methods = self.cooking_methods


        else:
            cooking_methods = self.cooking_methods

        courses: list[str] | None | Unset
        if isinstance(self.courses, Unset):
            courses = UNSET
        elif isinstance(self.courses, list):
            courses = self.courses


        else:
            courses = self.courses

        cuisines: list[str] | None | Unset
        if isinstance(self.cuisines, Unset):
            cuisines = UNSET
        elif isinstance(self.cuisines, list):
            cuisines = self.cuisines


        else:
            cuisines = self.cuisines

        description = self.description

        dietary_claims: list[dict[str, Any]] | None | Unset
        if isinstance(self.dietary_claims, Unset):
            dietary_claims = UNSET
        elif isinstance(self.dietary_claims, list):
            dietary_claims = []
            for dietary_claims_type_0_item_data in self.dietary_claims:
                dietary_claims_type_0_item = dietary_claims_type_0_item_data.to_dict()
                dietary_claims.append(dietary_claims_type_0_item)


        else:
            dietary_claims = self.dietary_claims

        equipment: list[dict[str, Any]] | None | Unset
        if isinstance(self.equipment, Unset):
            equipment = UNSET
        elif isinstance(self.equipment, list):
            equipment = []
            for equipment_type_0_item_data in self.equipment:
                equipment_type_0_item = equipment_type_0_item_data.to_dict()
                equipment.append(equipment_type_0_item)


        else:
            equipment = self.equipment

        extensions_raw: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions_raw, Unset):
            extensions_raw = self.extensions_raw.to_dict()

        image_refs: list[str] | None | Unset
        if isinstance(self.image_refs, Unset):
            image_refs = UNSET
        elif isinstance(self.image_refs, list):
            image_refs = self.image_refs


        else:
            image_refs = self.image_refs

        keywords: list[str] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, list):
            keywords = self.keywords


        else:
            keywords = self.keywords

        language = self.language

        modified = self.modified

        notes: list[str] | None | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        elif isinstance(self.notes, list):
            notes = self.notes


        else:
            notes = self.notes

        nutrition: list[dict[str, Any]] | None | Unset
        if isinstance(self.nutrition, Unset):
            nutrition = UNSET
        elif isinstance(self.nutrition, list):
            nutrition = []
            for nutrition_type_0_item_data in self.nutrition:
                nutrition_type_0_item = nutrition_type_0_item_data.to_dict()
                nutrition.append(nutrition_type_0_item)


        else:
            nutrition = self.nutrition

        primary_image = self.primary_image

        published = self.published

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        source_locale = self.source_locale

        sref_opaque_raw: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sref_opaque_raw, Unset):
            sref_opaque_raw = self.sref_opaque_raw.to_dict()

        times: dict[str, Any] | Unset = UNSET
        if not isinstance(self.times, Unset):
            times = self.times.to_dict()

        translations: list[dict[str, Any]] | None | Unset
        if isinstance(self.translations, Unset):
            translations = UNSET
        elif isinstance(self.translations, list):
            translations = []
            for translations_type_0_item_data in self.translations:
                translations_type_0_item = translations_type_0_item_data.to_dict()
                translations.append(translations_type_0_item)


        else:
            translations = self.translations

        variants: list[dict[str, Any]] | None | Unset
        if isinstance(self.variants, Unset):
            variants = UNSET
        elif isinstance(self.variants, list):
            variants = []
            for variants_type_0_item_data in self.variants:
                variants_type_0_item = variants_type_0_item_data.to_dict()
                variants.append(variants_type_0_item)


        else:
            variants = self.variants

        yields: list[dict[str, Any]] | None | Unset
        if isinstance(self.yields, Unset):
            yields = UNSET
        elif isinstance(self.yields, list):
            yields = []
            for yields_type_0_item_data in self.yields:
                yields_type_0_item = yields_type_0_item_data.to_dict()
                yields.append(yields_type_0_item)


        else:
            yields = self.yields


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ingredient_sections": ingredient_sections,
            "instruction_sections": instruction_sections,
            "schema_version": schema_version,
            "title": title,
        })
        if allergen_declarations is not UNSET:
            field_dict["allergen_declarations"] = allergen_declarations
        if assets is not UNSET:
            field_dict["assets"] = assets
        if authors is not UNSET:
            field_dict["authors"] = authors
        if categories is not UNSET:
            field_dict["categories"] = categories
        if cooking_methods is not UNSET:
            field_dict["cooking_methods"] = cooking_methods
        if courses is not UNSET:
            field_dict["courses"] = courses
        if cuisines is not UNSET:
            field_dict["cuisines"] = cuisines
        if description is not UNSET:
            field_dict["description"] = description
        if dietary_claims is not UNSET:
            field_dict["dietary_claims"] = dietary_claims
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if extensions_raw is not UNSET:
            field_dict["extensions_raw"] = extensions_raw
        if image_refs is not UNSET:
            field_dict["image_refs"] = image_refs
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if language is not UNSET:
            field_dict["language"] = language
        if modified is not UNSET:
            field_dict["modified"] = modified
        if notes is not UNSET:
            field_dict["notes"] = notes
        if nutrition is not UNSET:
            field_dict["nutrition"] = nutrition
        if primary_image is not UNSET:
            field_dict["primary_image"] = primary_image
        if published is not UNSET:
            field_dict["published"] = published
        if source is not UNSET:
            field_dict["source"] = source
        if source_locale is not UNSET:
            field_dict["source_locale"] = source_locale
        if sref_opaque_raw is not UNSET:
            field_dict["sref_opaque_raw"] = sref_opaque_raw
        if times is not UNSET:
            field_dict["times"] = times
        if translations is not UNSET:
            field_dict["translations"] = translations
        if variants is not UNSET:
            field_dict["variants"] = variants
        if yields is not UNSET:
            field_dict["yields"] = yields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allergen_declaration import AllergenDeclaration # noqa: PLC0415
        from ..models.asset import Asset # noqa: PLC0415
        from ..models.author import Author # noqa: PLC0415
        from ..models.dietary_claim import DietaryClaim # noqa: PLC0415
        from ..models.equipment import Equipment # noqa: PLC0415
        from ..models.ingredient_section import IngredientSection # noqa: PLC0415
        from ..models.instruction_section import InstructionSection # noqa: PLC0415
        from ..models.nutrition_statement import NutritionStatement # noqa: PLC0415
        from ..models.recipe_document_extensions_raw import RecipeDocumentExtensionsRaw # noqa: PLC0415
        from ..models.recipe_document_sref_opaque_raw import RecipeDocumentSrefOpaqueRaw # noqa: PLC0415
        from ..models.source import Source # noqa: PLC0415
        from ..models.times import Times # noqa: PLC0415
        from ..models.translation import Translation # noqa: PLC0415
        from ..models.variant import Variant # noqa: PLC0415
        from ..models.yield_ import Yield # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_ingredient_sections(data: object) -> list[IngredientSection] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ingredient_sections_type_0 = []
                _ingredient_sections_type_0 = data
                for ingredient_sections_type_0_item_data in (_ingredient_sections_type_0):
                    ingredient_sections_type_0_item = IngredientSection.from_dict(ingredient_sections_type_0_item_data)



                    ingredient_sections_type_0.append(ingredient_sections_type_0_item)

                return ingredient_sections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IngredientSection] | None, data)

        ingredient_sections = _parse_ingredient_sections(d.pop("ingredient_sections"))


        def _parse_instruction_sections(data: object) -> list[InstructionSection] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                instruction_sections_type_0 = []
                _instruction_sections_type_0 = data
                for instruction_sections_type_0_item_data in (_instruction_sections_type_0):
                    instruction_sections_type_0_item = InstructionSection.from_dict(instruction_sections_type_0_item_data)



                    instruction_sections_type_0.append(instruction_sections_type_0_item)

                return instruction_sections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InstructionSection] | None, data)

        instruction_sections = _parse_instruction_sections(d.pop("instruction_sections"))


        schema_version = d.pop("schema_version")

        title = d.pop("title")

        def _parse_allergen_declarations(data: object) -> list[AllergenDeclaration] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allergen_declarations_type_0 = []
                _allergen_declarations_type_0 = data
                for allergen_declarations_type_0_item_data in (_allergen_declarations_type_0):
                    allergen_declarations_type_0_item = AllergenDeclaration.from_dict(allergen_declarations_type_0_item_data)



                    allergen_declarations_type_0.append(allergen_declarations_type_0_item)

                return allergen_declarations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AllergenDeclaration] | None | Unset, data)

        allergen_declarations = _parse_allergen_declarations(d.pop("allergen_declarations", UNSET))


        def _parse_assets(data: object) -> list[Asset] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assets_type_0 = []
                _assets_type_0 = data
                for assets_type_0_item_data in (_assets_type_0):
                    assets_type_0_item = Asset.from_dict(assets_type_0_item_data)



                    assets_type_0.append(assets_type_0_item)

                return assets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Asset] | None | Unset, data)

        assets = _parse_assets(d.pop("assets", UNSET))


        def _parse_authors(data: object) -> list[Author] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                authors_type_0 = []
                _authors_type_0 = data
                for authors_type_0_item_data in (_authors_type_0):
                    authors_type_0_item = Author.from_dict(authors_type_0_item_data)



                    authors_type_0.append(authors_type_0_item)

                return authors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Author] | None | Unset, data)

        authors = _parse_authors(d.pop("authors", UNSET))


        def _parse_categories(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = cast(list[str], data)

                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        categories = _parse_categories(d.pop("categories", UNSET))


        def _parse_cooking_methods(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cooking_methods_type_0 = cast(list[str], data)

                return cooking_methods_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cooking_methods = _parse_cooking_methods(d.pop("cooking_methods", UNSET))


        def _parse_courses(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                courses_type_0 = cast(list[str], data)

                return courses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        courses = _parse_courses(d.pop("courses", UNSET))


        def _parse_cuisines(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cuisines_type_0 = cast(list[str], data)

                return cuisines_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cuisines = _parse_cuisines(d.pop("cuisines", UNSET))


        description = d.pop("description", UNSET)

        def _parse_dietary_claims(data: object) -> list[DietaryClaim] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dietary_claims_type_0 = []
                _dietary_claims_type_0 = data
                for dietary_claims_type_0_item_data in (_dietary_claims_type_0):
                    dietary_claims_type_0_item = DietaryClaim.from_dict(dietary_claims_type_0_item_data)



                    dietary_claims_type_0.append(dietary_claims_type_0_item)

                return dietary_claims_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DietaryClaim] | None | Unset, data)

        dietary_claims = _parse_dietary_claims(d.pop("dietary_claims", UNSET))


        def _parse_equipment(data: object) -> list[Equipment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                equipment_type_0 = []
                _equipment_type_0 = data
                for equipment_type_0_item_data in (_equipment_type_0):
                    equipment_type_0_item = Equipment.from_dict(equipment_type_0_item_data)



                    equipment_type_0.append(equipment_type_0_item)

                return equipment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Equipment] | None | Unset, data)

        equipment = _parse_equipment(d.pop("equipment", UNSET))


        _extensions_raw = d.pop("extensions_raw", UNSET)
        extensions_raw: RecipeDocumentExtensionsRaw | Unset
        if isinstance(_extensions_raw,  Unset):
            extensions_raw = UNSET
        else:
            extensions_raw = RecipeDocumentExtensionsRaw.from_dict(_extensions_raw)




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


        def _parse_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_type_0 = cast(list[str], data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))


        language = d.pop("language", UNSET)

        modified = d.pop("modified", UNSET)

        def _parse_notes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notes_type_0 = cast(list[str], data)

                return notes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_nutrition(data: object) -> list[NutritionStatement] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                nutrition_type_0 = []
                _nutrition_type_0 = data
                for nutrition_type_0_item_data in (_nutrition_type_0):
                    nutrition_type_0_item = NutritionStatement.from_dict(nutrition_type_0_item_data)



                    nutrition_type_0.append(nutrition_type_0_item)

                return nutrition_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NutritionStatement] | None | Unset, data)

        nutrition = _parse_nutrition(d.pop("nutrition", UNSET))


        primary_image = d.pop("primary_image", UNSET)

        published = d.pop("published", UNSET)

        _source = d.pop("source", UNSET)
        source: Source | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = Source.from_dict(_source)




        source_locale = d.pop("source_locale", UNSET)

        _sref_opaque_raw = d.pop("sref_opaque_raw", UNSET)
        sref_opaque_raw: RecipeDocumentSrefOpaqueRaw | Unset
        if isinstance(_sref_opaque_raw,  Unset):
            sref_opaque_raw = UNSET
        else:
            sref_opaque_raw = RecipeDocumentSrefOpaqueRaw.from_dict(_sref_opaque_raw)




        _times = d.pop("times", UNSET)
        times: Times | Unset
        if isinstance(_times,  Unset):
            times = UNSET
        else:
            times = Times.from_dict(_times)




        def _parse_translations(data: object) -> list[Translation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                translations_type_0 = []
                _translations_type_0 = data
                for translations_type_0_item_data in (_translations_type_0):
                    translations_type_0_item = Translation.from_dict(translations_type_0_item_data)



                    translations_type_0.append(translations_type_0_item)

                return translations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Translation] | None | Unset, data)

        translations = _parse_translations(d.pop("translations", UNSET))


        def _parse_variants(data: object) -> list[Variant] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                variants_type_0 = []
                _variants_type_0 = data
                for variants_type_0_item_data in (_variants_type_0):
                    variants_type_0_item = Variant.from_dict(variants_type_0_item_data)



                    variants_type_0.append(variants_type_0_item)

                return variants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Variant] | None | Unset, data)

        variants = _parse_variants(d.pop("variants", UNSET))


        def _parse_yields(data: object) -> list[Yield] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                yields_type_0 = []
                _yields_type_0 = data
                for yields_type_0_item_data in (_yields_type_0):
                    yields_type_0_item = Yield.from_dict(yields_type_0_item_data)



                    yields_type_0.append(yields_type_0_item)

                return yields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Yield] | None | Unset, data)

        yields = _parse_yields(d.pop("yields", UNSET))


        recipe_document = cls(
            id=id,
            ingredient_sections=ingredient_sections,
            instruction_sections=instruction_sections,
            schema_version=schema_version,
            title=title,
            allergen_declarations=allergen_declarations,
            assets=assets,
            authors=authors,
            categories=categories,
            cooking_methods=cooking_methods,
            courses=courses,
            cuisines=cuisines,
            description=description,
            dietary_claims=dietary_claims,
            equipment=equipment,
            extensions_raw=extensions_raw,
            image_refs=image_refs,
            keywords=keywords,
            language=language,
            modified=modified,
            notes=notes,
            nutrition=nutrition,
            primary_image=primary_image,
            published=published,
            source=source,
            source_locale=source_locale,
            sref_opaque_raw=sref_opaque_raw,
            times=times,
            translations=translations,
            variants=variants,
            yields=yields,
        )

        return recipe_document

