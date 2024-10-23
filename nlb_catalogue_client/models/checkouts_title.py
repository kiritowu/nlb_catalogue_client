from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckoutsTitle")


@_attrs_define
class CheckoutsTitle:
    """
    Attributes:
        title (Union[None, Unset, str]): Bibliographic title in english
        native_title (Union[None, Unset, str]): Bibliographic title in native language
        author (Union[None, Unset, str]): Author name in english
        native_author (Union[None, Unset, str]): Author name in native language
        isbns (Union[List[str], None, Unset]): isbns
        checkouts_count (Union[Unset, int]): Checkouts count for the duration.
    """

    title: Union[None, Unset, str] = UNSET
    native_title: Union[None, Unset, str] = UNSET
    author: Union[None, Unset, str] = UNSET
    native_author: Union[None, Unset, str] = UNSET
    isbns: Union[List[str], None, Unset] = UNSET
    checkouts_count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        native_title: Union[None, Unset, str]
        if isinstance(self.native_title, Unset):
            native_title = UNSET
        else:
            native_title = self.native_title

        author: Union[None, Unset, str]
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        native_author: Union[None, Unset, str]
        if isinstance(self.native_author, Unset):
            native_author = UNSET
        else:
            native_author = self.native_author

        isbns: Union[List[str], None, Unset]
        if isinstance(self.isbns, Unset):
            isbns = UNSET
        elif isinstance(self.isbns, list):
            isbns = self.isbns

        else:
            isbns = self.isbns

        checkouts_count = self.checkouts_count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if native_title is not UNSET:
            field_dict["nativeTitle"] = native_title
        if author is not UNSET:
            field_dict["author"] = author
        if native_author is not UNSET:
            field_dict["nativeAuthor"] = native_author
        if isbns is not UNSET:
            field_dict["isbns"] = isbns
        if checkouts_count is not UNSET:
            field_dict["checkoutsCount"] = checkouts_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_native_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        native_title = _parse_native_title(d.pop("nativeTitle", UNSET))

        def _parse_author(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_native_author(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        native_author = _parse_native_author(d.pop("nativeAuthor", UNSET))

        def _parse_isbns(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                isbns_type_0 = cast(List[str], data)

                return isbns_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        isbns = _parse_isbns(d.pop("isbns", UNSET))

        checkouts_count = d.pop("checkoutsCount", UNSET)

        checkouts_title = cls(
            title=title,
            native_title=native_title,
            author=author,
            native_author=native_author,
            isbns=isbns,
            checkouts_count=checkouts_count,
        )

        return checkouts_title
