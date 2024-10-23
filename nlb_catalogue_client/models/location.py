from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Location")


@_attrs_define
class Location:
    """Library Location. Please refer to code list C005.

    Attributes:
        code (str): Library code Example: AMKPL.
        name (str): Library Name Example: Ang Mo Kio Public Library.
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

        location = cls(
            code=code,
            name=name,
        )

        return location
