import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location import Location


T = TypeVar("T", bound="TransactionStatus")


@_attrs_define
class TransactionStatus:
    """Item Transactional Status. Please refer to code list C003.

    Attributes:
        code (str): Item transaction status code. Example: I.
        name (str): Item transaction status name Example: In Transist.
        date (Union[Unset, datetime.datetime]): Item transaction status date Example: 2019-07-21T14:32:45.
        in_transit_from (Union[Unset, Location]): Library Location. Please refer to code list C005.
        in_transit_to (Union[Unset, Location]): Library Location. Please refer to code list C005.
    """

    code: str
    name: str
    date: Union[Unset, datetime.datetime] = UNSET
    in_transit_from: Union[Unset, "Location"] = UNSET
    in_transit_to: Union[Unset, "Location"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        name = self.name

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        in_transit_from: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.in_transit_from, Unset):
            in_transit_from = self.in_transit_from.to_dict()

        in_transit_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.in_transit_to, Unset):
            in_transit_to = self.in_transit_to.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "code": code,
                "name": name,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if in_transit_from is not UNSET:
            field_dict["inTransitFrom"] = in_transit_from
        if in_transit_to is not UNSET:
            field_dict["inTransitTo"] = in_transit_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location import Location

        d = src_dict.copy()
        code = d.pop("code")

        name = d.pop("name")

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _in_transit_from = d.pop("inTransitFrom", UNSET)
        in_transit_from: Union[Unset, Location]
        if isinstance(_in_transit_from, Unset):
            in_transit_from = UNSET
        else:
            in_transit_from = Location.from_dict(_in_transit_from)

        _in_transit_to = d.pop("inTransitTo", UNSET)
        in_transit_to: Union[Unset, Location]
        if isinstance(_in_transit_to, Unset):
            in_transit_to = UNSET
        else:
            in_transit_to = Location.from_dict(_in_transit_to)

        transaction_status = cls(
            code=code,
            name=name,
            date=date,
            in_transit_from=in_transit_from,
            in_transit_to=in_transit_to,
        )

        return transaction_status
