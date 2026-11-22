from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.print_options_image import PrintOptionsImage
from ..models.print_options_layout import PrintOptionsLayout
from ..models.print_options_measurement import PrintOptionsMeasurement
from ..models.print_options_output import PrintOptionsOutput
from ..models.print_options_scale import PrintOptionsScale
from ..models.print_options_size import PrintOptionsSize
from ..types import UNSET, Unset






T = TypeVar("T", bound="PrintOptions")



@_attrs_define
class PrintOptions:
    """ 
        Attributes:
            claims (bool | Unset): Print the dietary and allergen statements the recipe's source makes
            custom_scale (str | Unset): Exact batch factor, required when scale is custom
            description (bool | Unset): Print the recipe's headnote
            image (PrintOptionsImage | Unset): Whether the recipe photograph is printed
            layout (PrintOptionsLayout | Unset): Full-page composition
            locale (str | Unset): Language tag the document is presented in
            measurement (PrintOptionsMeasurement | Unset): Measures the recipe is written in for this print
            microwave_output_watts (int | Unset): Explicit cooking-output basis for an adjusted print; omitted prints
                authored timings
            notes (bool | Unset): Print the recipe's notes
            nutrition (bool | Unset): Print the nutrition the recipe's source states; off by default
            output (PrintOptionsOutput | Unset): Whether cards become pages of their own size or are arranged on sheets for
                trimming
            scale (PrintOptionsScale | Unset): Which batch to print
            size (PrintOptionsSize | Unset): Physical output size
            source (bool | Unset): Print where the recipe came from
     """

    claims: bool | Unset = UNSET
    custom_scale: str | Unset = UNSET
    description: bool | Unset = UNSET
    image: PrintOptionsImage | Unset = UNSET
    layout: PrintOptionsLayout | Unset = UNSET
    locale: str | Unset = UNSET
    measurement: PrintOptionsMeasurement | Unset = UNSET
    microwave_output_watts: int | Unset = UNSET
    notes: bool | Unset = UNSET
    nutrition: bool | Unset = UNSET
    output: PrintOptionsOutput | Unset = UNSET
    scale: PrintOptionsScale | Unset = UNSET
    size: PrintOptionsSize | Unset = UNSET
    source: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        claims = self.claims

        custom_scale = self.custom_scale

        description = self.description

        image: str | Unset = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.value


        layout: str | Unset = UNSET
        if not isinstance(self.layout, Unset):
            layout = self.layout.value


        locale = self.locale

        measurement: str | Unset = UNSET
        if not isinstance(self.measurement, Unset):
            measurement = self.measurement.value


        microwave_output_watts = self.microwave_output_watts

        notes = self.notes

        nutrition = self.nutrition

        output: str | Unset = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.value


        scale: str | Unset = UNSET
        if not isinstance(self.scale, Unset):
            scale = self.scale.value


        size: str | Unset = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.value


        source = self.source


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if claims is not UNSET:
            field_dict["claims"] = claims
        if custom_scale is not UNSET:
            field_dict["custom_scale"] = custom_scale
        if description is not UNSET:
            field_dict["description"] = description
        if image is not UNSET:
            field_dict["image"] = image
        if layout is not UNSET:
            field_dict["layout"] = layout
        if locale is not UNSET:
            field_dict["locale"] = locale
        if measurement is not UNSET:
            field_dict["measurement"] = measurement
        if microwave_output_watts is not UNSET:
            field_dict["microwave_output_watts"] = microwave_output_watts
        if notes is not UNSET:
            field_dict["notes"] = notes
        if nutrition is not UNSET:
            field_dict["nutrition"] = nutrition
        if output is not UNSET:
            field_dict["output"] = output
        if scale is not UNSET:
            field_dict["scale"] = scale
        if size is not UNSET:
            field_dict["size"] = size
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        claims = d.pop("claims", UNSET)

        custom_scale = d.pop("custom_scale", UNSET)

        description = d.pop("description", UNSET)

        _image = d.pop("image", UNSET)
        image: PrintOptionsImage | Unset
        if isinstance(_image,  Unset):
            image = UNSET
        else:
            image = PrintOptionsImage(_image)




        _layout = d.pop("layout", UNSET)
        layout: PrintOptionsLayout | Unset
        if isinstance(_layout,  Unset):
            layout = UNSET
        else:
            layout = PrintOptionsLayout(_layout)




        locale = d.pop("locale", UNSET)

        _measurement = d.pop("measurement", UNSET)
        measurement: PrintOptionsMeasurement | Unset
        if isinstance(_measurement,  Unset):
            measurement = UNSET
        else:
            measurement = PrintOptionsMeasurement(_measurement)




        microwave_output_watts = d.pop("microwave_output_watts", UNSET)

        notes = d.pop("notes", UNSET)

        nutrition = d.pop("nutrition", UNSET)

        _output = d.pop("output", UNSET)
        output: PrintOptionsOutput | Unset
        if isinstance(_output,  Unset):
            output = UNSET
        else:
            output = PrintOptionsOutput(_output)




        _scale = d.pop("scale", UNSET)
        scale: PrintOptionsScale | Unset
        if isinstance(_scale,  Unset):
            scale = UNSET
        else:
            scale = PrintOptionsScale(_scale)




        _size = d.pop("size", UNSET)
        size: PrintOptionsSize | Unset
        if isinstance(_size,  Unset):
            size = UNSET
        else:
            size = PrintOptionsSize(_size)




        source = d.pop("source", UNSET)

        print_options = cls(
            claims=claims,
            custom_scale=custom_scale,
            description=description,
            image=image,
            layout=layout,
            locale=locale,
            measurement=measurement,
            microwave_output_watts=microwave_output_watts,
            notes=notes,
            nutrition=nutrition,
            output=output,
            scale=scale,
            size=size,
            source=source,
        )

        return print_options

