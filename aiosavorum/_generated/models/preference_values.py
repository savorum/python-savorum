from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.preference_values_appearance import PreferenceValuesAppearance
from ..models.preference_values_measurement import PreferenceValuesMeasurement
from ..models.preference_values_print_image import PreferenceValuesPrintImage
from ..models.preference_values_print_page_size import PreferenceValuesPrintPageSize
from ..models.preference_values_recipe_view import PreferenceValuesRecipeView
from ..models.preference_values_reduced_motion import PreferenceValuesReducedMotion
from ..models.preference_values_temperature import PreferenceValuesTemperature
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PreferenceValues")



@_attrs_define
class PreferenceValues:
    """ 
        Attributes:
            appearance (PreferenceValuesAppearance | Unset):
            content_languages (list[str] | None | Unset):
            measurement (PreferenceValuesMeasurement | Unset):
            microwave_output_watts (int | Unset):
            print_image (PreferenceValuesPrintImage | Unset):
            print_page_size (PreferenceValuesPrintPageSize | Unset):
            recipe_view (PreferenceValuesRecipeView | Unset):
            reduced_motion (PreferenceValuesReducedMotion | Unset):
            temperature (PreferenceValuesTemperature | Unset):
            timezone (str | Unset):
            ui_locale (str | Unset):
     """

    appearance: PreferenceValuesAppearance | Unset = UNSET
    content_languages: list[str] | None | Unset = UNSET
    measurement: PreferenceValuesMeasurement | Unset = UNSET
    microwave_output_watts: int | Unset = UNSET
    print_image: PreferenceValuesPrintImage | Unset = UNSET
    print_page_size: PreferenceValuesPrintPageSize | Unset = UNSET
    recipe_view: PreferenceValuesRecipeView | Unset = UNSET
    reduced_motion: PreferenceValuesReducedMotion | Unset = UNSET
    temperature: PreferenceValuesTemperature | Unset = UNSET
    timezone: str | Unset = UNSET
    ui_locale: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        appearance: str | Unset = UNSET
        if not isinstance(self.appearance, Unset):
            appearance = self.appearance.value


        content_languages: list[str] | None | Unset
        if isinstance(self.content_languages, Unset):
            content_languages = UNSET
        elif isinstance(self.content_languages, list):
            content_languages = self.content_languages


        else:
            content_languages = self.content_languages

        measurement: str | Unset = UNSET
        if not isinstance(self.measurement, Unset):
            measurement = self.measurement.value


        microwave_output_watts = self.microwave_output_watts

        print_image: str | Unset = UNSET
        if not isinstance(self.print_image, Unset):
            print_image = self.print_image.value


        print_page_size: str | Unset = UNSET
        if not isinstance(self.print_page_size, Unset):
            print_page_size = self.print_page_size.value


        recipe_view: str | Unset = UNSET
        if not isinstance(self.recipe_view, Unset):
            recipe_view = self.recipe_view.value


        reduced_motion: str | Unset = UNSET
        if not isinstance(self.reduced_motion, Unset):
            reduced_motion = self.reduced_motion.value


        temperature: str | Unset = UNSET
        if not isinstance(self.temperature, Unset):
            temperature = self.temperature.value


        timezone = self.timezone

        ui_locale = self.ui_locale


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if appearance is not UNSET:
            field_dict["appearance"] = appearance
        if content_languages is not UNSET:
            field_dict["content_languages"] = content_languages
        if measurement is not UNSET:
            field_dict["measurement"] = measurement
        if microwave_output_watts is not UNSET:
            field_dict["microwave_output_watts"] = microwave_output_watts
        if print_image is not UNSET:
            field_dict["print_image"] = print_image
        if print_page_size is not UNSET:
            field_dict["print_page_size"] = print_page_size
        if recipe_view is not UNSET:
            field_dict["recipe_view"] = recipe_view
        if reduced_motion is not UNSET:
            field_dict["reduced_motion"] = reduced_motion
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if ui_locale is not UNSET:
            field_dict["ui_locale"] = ui_locale

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _appearance = d.pop("appearance", UNSET)
        appearance: PreferenceValuesAppearance | Unset
        if isinstance(_appearance,  Unset):
            appearance = UNSET
        else:
            appearance = PreferenceValuesAppearance(_appearance)




        def _parse_content_languages(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                content_languages_type_0 = cast(list[str], data)

                return content_languages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        content_languages = _parse_content_languages(d.pop("content_languages", UNSET))


        _measurement = d.pop("measurement", UNSET)
        measurement: PreferenceValuesMeasurement | Unset
        if isinstance(_measurement,  Unset):
            measurement = UNSET
        else:
            measurement = PreferenceValuesMeasurement(_measurement)




        microwave_output_watts = d.pop("microwave_output_watts", UNSET)

        _print_image = d.pop("print_image", UNSET)
        print_image: PreferenceValuesPrintImage | Unset
        if isinstance(_print_image,  Unset):
            print_image = UNSET
        else:
            print_image = PreferenceValuesPrintImage(_print_image)




        _print_page_size = d.pop("print_page_size", UNSET)
        print_page_size: PreferenceValuesPrintPageSize | Unset
        if isinstance(_print_page_size,  Unset):
            print_page_size = UNSET
        else:
            print_page_size = PreferenceValuesPrintPageSize(_print_page_size)




        _recipe_view = d.pop("recipe_view", UNSET)
        recipe_view: PreferenceValuesRecipeView | Unset
        if isinstance(_recipe_view,  Unset):
            recipe_view = UNSET
        else:
            recipe_view = PreferenceValuesRecipeView(_recipe_view)




        _reduced_motion = d.pop("reduced_motion", UNSET)
        reduced_motion: PreferenceValuesReducedMotion | Unset
        if isinstance(_reduced_motion,  Unset):
            reduced_motion = UNSET
        else:
            reduced_motion = PreferenceValuesReducedMotion(_reduced_motion)




        _temperature = d.pop("temperature", UNSET)
        temperature: PreferenceValuesTemperature | Unset
        if isinstance(_temperature,  Unset):
            temperature = UNSET
        else:
            temperature = PreferenceValuesTemperature(_temperature)




        timezone = d.pop("timezone", UNSET)

        ui_locale = d.pop("ui_locale", UNSET)

        preference_values = cls(
            appearance=appearance,
            content_languages=content_languages,
            measurement=measurement,
            microwave_output_watts=microwave_output_watts,
            print_image=print_image,
            print_page_size=print_page_size,
            recipe_view=recipe_view,
            reduced_motion=reduced_motion,
            temperature=temperature,
            timezone=timezone,
            ui_locale=ui_locale,
        )

        return preference_values

