from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.error_detail import ErrorDetail
  from ..models.error_model_params import ErrorModelParams
  from ..models.error_model_violations_item import ErrorModelViolationsItem





T = TypeVar("T", bound="ErrorModel")



@_attrs_define
class ErrorModel:
    """ 
        Attributes:
            code (str | Unset): Stable application error code; clients may also use the problem type suffix.
            detail (str | Unset): A human-readable explanation specific to this occurrence of the problem.
            errors (list[ErrorDetail] | None | Unset): Optional list of individual error details
            instance (str | Unset): A URI reference that identifies the specific occurrence of the problem.
            params (ErrorModelParams | Unset): Structured context for the stable error code.
            status (int | Unset): HTTP status code
            title (str | Unset): A short, human-readable summary of the problem type. This value should not change between
                occurrences of the error.
            type_ (str | Unset): A URI reference to human-readable documentation for the error. Default: 'about:blank'.
            violations (list[ErrorModelViolationsItem] | Unset):
     """

    code: str | Unset = UNSET
    detail: str | Unset = UNSET
    errors: list[ErrorDetail] | None | Unset = UNSET
    instance: str | Unset = UNSET
    params: ErrorModelParams | Unset = UNSET
    status: int | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = 'about:blank'
    violations: list[ErrorModelViolationsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.error_detail import ErrorDetail # noqa: PLC0415
        from ..models.error_model_params import ErrorModelParams # noqa: PLC0415
        from ..models.error_model_violations_item import ErrorModelViolationsItem # noqa: PLC0415
        code = self.code

        detail = self.detail

        errors: list[dict[str, Any]] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)


        else:
            errors = self.errors

        instance = self.instance

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        status = self.status

        title = self.title

        type_ = self.type_

        violations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.violations, Unset):
            violations = []
            for violations_item_data in self.violations:
                violations_item = violations_item_data.to_dict()
                violations.append(violations_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if detail is not UNSET:
            field_dict["detail"] = detail
        if errors is not UNSET:
            field_dict["errors"] = errors
        if instance is not UNSET:
            field_dict["instance"] = instance
        if params is not UNSET:
            field_dict["params"] = params
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if violations is not UNSET:
            field_dict["violations"] = violations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_detail import ErrorDetail # noqa: PLC0415
        from ..models.error_model_params import ErrorModelParams # noqa: PLC0415
        from ..models.error_model_violations_item import ErrorModelViolationsItem # noqa: PLC0415
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        detail = d.pop("detail", UNSET)

        def _parse_errors(data: object) -> list[ErrorDetail] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in (_errors_type_0):
                    errors_type_0_item = ErrorDetail.from_dict(errors_type_0_item_data)



                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ErrorDetail] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))


        instance = d.pop("instance", UNSET)

        _params = d.pop("params", UNSET)
        params: ErrorModelParams | Unset
        if isinstance(_params,  Unset):
            params = UNSET
        else:
            params = ErrorModelParams.from_dict(_params)




        status = d.pop("status", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        _violations = d.pop("violations", UNSET)
        violations: list[ErrorModelViolationsItem] | Unset = UNSET
        if _violations is not UNSET:
            violations = []
            for violations_item_data in _violations:
                violations_item = ErrorModelViolationsItem.from_dict(violations_item_data)



                violations.append(violations_item)


        error_model = cls(
            code=code,
            detail=detail,
            errors=errors,
            instance=instance,
            params=params,
            status=status,
            title=title,
            type_=type_,
            violations=violations,
        )


        error_model.additional_properties = d
        return error_model

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
