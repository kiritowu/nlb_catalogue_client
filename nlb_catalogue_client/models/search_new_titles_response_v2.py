from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_arrival_title import NewArrivalTitle


T = TypeVar("T", bound="SearchNewTitlesResponseV2")


@_attrs_define
class SearchNewTitlesResponseV2:
    """
    Attributes:
        total_records (Union[Unset, int]): Total number of records for this search(dataset). Example: 999.
        count (Union[Unset, int]): Number of records returned in the response. Example: 999.
        next_records_offset (Union[Unset, int]): Value to pass in Offset parameter to navigate to next page. Example:
            20.
        has_more_records (Union[Unset, bool]): Indicator - if dataset has more records or not for pagination. Default:
            False.
        titles (Union[Unset, List['NewArrivalTitle']]):
    """

    total_records: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET
    next_records_offset: Union[Unset, int] = UNSET
    has_more_records: Union[Unset, bool] = False
    titles: Union[Unset, List["NewArrivalTitle"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        total_records = self.total_records

        count = self.count

        next_records_offset = self.next_records_offset

        has_more_records = self.has_more_records

        titles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.titles, Unset):
            titles = []
            for titles_item_data in self.titles:
                titles_item = titles_item_data.to_dict()
                titles.append(titles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if total_records is not UNSET:
            field_dict["totalRecords"] = total_records
        if count is not UNSET:
            field_dict["count"] = count
        if next_records_offset is not UNSET:
            field_dict["nextRecordsOffset"] = next_records_offset
        if has_more_records is not UNSET:
            field_dict["hasMoreRecords"] = has_more_records
        if titles is not UNSET:
            field_dict["titles"] = titles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.new_arrival_title import NewArrivalTitle

        d = src_dict.copy()
        total_records = d.pop("totalRecords", UNSET)

        count = d.pop("count", UNSET)

        next_records_offset = d.pop("nextRecordsOffset", UNSET)

        has_more_records = d.pop("hasMoreRecords", UNSET)

        titles = []
        _titles = d.pop("titles", UNSET)
        for titles_item_data in _titles or []:
            titles_item = NewArrivalTitle.from_dict(titles_item_data)

            titles.append(titles_item)

        search_new_titles_response_v2 = cls(
            total_records=total_records,
            count=count,
            next_records_offset=next_records_offset,
            has_more_records=has_more_records,
            titles=titles,
        )

        return search_new_titles_response_v2
