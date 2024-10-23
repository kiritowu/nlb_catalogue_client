from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.book_cover import BookCover
    from ..models.title_record import TitleRecord


T = TypeVar("T", bound="TitleSummary")


@_attrs_define
class TitleSummary:
    """
    Attributes:
        title (Union[None, Unset, str]): Full title (with author info suffixed by /) of the bibliographic record.
        native_title (Union[None, Unset, str]): Full title (with author info suffixed by /) of the bibliographic
            record(native language).
        series_title (Union[List[str], None, Unset]): Series titles. Example: ['123 Zhima Jie'].
        native_series_title (Union[List[str], None, Unset]): Series title (native language). Example: ['123芝麻街'].
        author (Union[None, Unset, str]): Author name in english. Example: Song bing wu de yi xiang shi jie..
        native_author (Union[None, Unset, str]): Author name (native language). Example: 松饼屋的异想世界.
        cover_url (Union[Unset, BookCover]):
        records (Union[Unset, List['TitleRecord']]):
    """

    title: Union[None, Unset, str] = UNSET
    native_title: Union[None, Unset, str] = UNSET
    series_title: Union[List[str], None, Unset] = UNSET
    native_series_title: Union[List[str], None, Unset] = UNSET
    author: Union[None, Unset, str] = UNSET
    native_author: Union[None, Unset, str] = UNSET
    cover_url: Union[Unset, "BookCover"] = UNSET
    records: Union[Unset, List["TitleRecord"]] = UNSET

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

        series_title: Union[List[str], None, Unset]
        if isinstance(self.series_title, Unset):
            series_title = UNSET
        elif isinstance(self.series_title, list):
            series_title = self.series_title

        else:
            series_title = self.series_title

        native_series_title: Union[List[str], None, Unset]
        if isinstance(self.native_series_title, Unset):
            native_series_title = UNSET
        elif isinstance(self.native_series_title, list):
            native_series_title = self.native_series_title

        else:
            native_series_title = self.native_series_title

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

        cover_url: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cover_url, Unset):
            cover_url = self.cover_url.to_dict()

        records: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()
                records.append(records_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if native_title is not UNSET:
            field_dict["nativeTitle"] = native_title
        if series_title is not UNSET:
            field_dict["seriesTitle"] = series_title
        if native_series_title is not UNSET:
            field_dict["nativeSeriesTitle"] = native_series_title
        if author is not UNSET:
            field_dict["author"] = author
        if native_author is not UNSET:
            field_dict["nativeAuthor"] = native_author
        if cover_url is not UNSET:
            field_dict["coverUrl"] = cover_url
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.book_cover import BookCover
        from ..models.title_record import TitleRecord

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

        def _parse_series_title(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                series_title_type_0 = cast(List[str], data)

                return series_title_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        series_title = _parse_series_title(d.pop("seriesTitle", UNSET))

        def _parse_native_series_title(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                native_series_title_type_0 = cast(List[str], data)

                return native_series_title_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        native_series_title = _parse_native_series_title(d.pop("nativeSeriesTitle", UNSET))

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

        _cover_url = d.pop("coverUrl", UNSET)
        cover_url: Union[Unset, BookCover]
        if isinstance(_cover_url, Unset):
            cover_url = UNSET
        else:
            cover_url = BookCover.from_dict(_cover_url)

        records = []
        _records = d.pop("records", UNSET)
        for records_item_data in _records or []:
            records_item = TitleRecord.from_dict(records_item_data)

            records.append(records_item)

        title_summary = cls(
            title=title,
            native_title=native_title,
            series_title=series_title,
            native_series_title=native_series_title,
            author=author,
            native_author=native_author,
            cover_url=cover_url,
            records=records,
        )

        return title_summary
