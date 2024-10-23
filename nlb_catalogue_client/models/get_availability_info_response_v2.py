from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item import Item


T = TypeVar("T", bound="GetAvailabilityInfoResponseV2")


@_attrs_define
class GetAvailabilityInfoResponseV2:
    """
    Attributes:
        set_id (Union[Unset, int]): Search result dataset id.
        total_records (Union[Unset, int]): Total number of records for this search(dataset). Example: 999.
        count (Union[Unset, int]): Number of records returned in the response. Example: 999.
        has_more_records (Union[Unset, bool]): Indicator - if dataset has more records or not for pagination. Default:
            False.
        next_records_offset (Union[Unset, int]): Value to pass in Offset parameter to navigate to next page. Example:
            20.
        items (Union[Unset, List['Item']]):
    """

    set_id: Union[Unset, int] = UNSET
    total_records: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET
    has_more_records: Union[Unset, bool] = False
    next_records_offset: Union[Unset, int] = UNSET
    items: Union[Unset, List["Item"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        set_id = self.set_id

        total_records = self.total_records

        count = self.count

        has_more_records = self.has_more_records

        next_records_offset = self.next_records_offset

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if set_id is not UNSET:
            field_dict["setId"] = set_id
        if total_records is not UNSET:
            field_dict["totalRecords"] = total_records
        if count is not UNSET:
            field_dict["count"] = count
        if has_more_records is not UNSET:
            field_dict["hasMoreRecords"] = has_more_records
        if next_records_offset is not UNSET:
            field_dict["nextRecordsOffset"] = next_records_offset
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item import Item

        d = src_dict.copy()
        set_id = d.pop("setId", UNSET)

        total_records = d.pop("totalRecords", UNSET)

        count = d.pop("count", UNSET)

        has_more_records = d.pop("hasMoreRecords", UNSET)

        next_records_offset = d.pop("nextRecordsOffset", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = Item.from_dict(items_item_data)

            items.append(items_item)

        get_availability_info_response_v2 = cls(
            set_id=set_id,
            total_records=total_records,
            count=count,
            has_more_records=has_more_records,
            next_records_offset=next_records_offset,
            items=items,
        )

        return get_availability_info_response_v2
