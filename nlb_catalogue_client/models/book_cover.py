from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookCover")


@_attrs_define
class BookCover:
    """
    Attributes:
        small (Union[None, Unset, str]): Small size image url
        medium (Union[None, Unset, str]): Medium size image url
        large (Union[None, Unset, str]): Large size image url
    """

    small: Union[None, Unset, str] = UNSET
    medium: Union[None, Unset, str] = UNSET
    large: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        small: Union[None, Unset, str]
        if isinstance(self.small, Unset):
            small = UNSET
        else:
            small = self.small

        medium: Union[None, Unset, str]
        if isinstance(self.medium, Unset):
            medium = UNSET
        else:
            medium = self.medium

        large: Union[None, Unset, str]
        if isinstance(self.large, Unset):
            large = UNSET
        else:
            large = self.large

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if small is not UNSET:
            field_dict["small"] = small
        if medium is not UNSET:
            field_dict["medium"] = medium
        if large is not UNSET:
            field_dict["large"] = large

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_small(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small = _parse_small(d.pop("small", UNSET))

        def _parse_medium(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        medium = _parse_medium(d.pop("medium", UNSET))

        def _parse_large(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        large = _parse_large(d.pop("large", UNSET))

        book_cover = cls(
            small=small,
            medium=medium,
            large=large,
        )

        return book_cover
