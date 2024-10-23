from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UsageLevel")


@_attrs_define
class UsageLevel:
    """Usage Level. Please refer to code list C004.

    Attributes:
        code (str): Usage Level ILS code. Example: 001.
        name (str): Usage Level code description Example: Junior Picture Adult Lending.
    """

    code: str
    name: str

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "code": code,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        name = d.pop("name")

        usage_level = cls(
            code=code,
            name=name,
        )

        return usage_level
