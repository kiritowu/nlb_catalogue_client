from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Media")


@_attrs_define
class Media:
    """Item Material Type. Please refer to code list C002.

    Attributes:
        code (str): Media Code Example: DV18.
        name (str): Media Name Example: Digital Video for M18.
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

        media = cls(
            code=code,
            name=name,
        )

        return media
