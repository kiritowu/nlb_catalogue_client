from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BibFormat")


@_attrs_define
class BibFormat:
    """Bibliographic Formats. Please refer to code list C001.

    Attributes:
        code (str): Bibliographic Format code. Example: BK.
        name (str): Bibliographic Format desc. Example: BOOKS.
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

        bib_format = cls(
            code=code,
            name=name,
        )

        return bib_format
