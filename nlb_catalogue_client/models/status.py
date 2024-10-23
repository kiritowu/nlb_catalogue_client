import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Status")


@_attrs_define
class Status:
    """Item Status.

    Attributes:
        name (str): Item status name Example: In Transist.
        code (Union[None, Unset, str]): Item status code. Example: I.
        set_date (Union[None, Unset, datetime.date]): status set date Example: 2019-07-21.
    """

    name: str
    code: Union[None, Unset, str] = UNSET
    set_date: Union[None, Unset, datetime.date] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        code: Union[None, Unset, str]
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        set_date: Union[None, Unset, str]
        if isinstance(self.set_date, Unset):
            set_date = UNSET
        elif isinstance(self.set_date, datetime.date):
            set_date = self.set_date.isoformat()
        else:
            set_date = self.set_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if set_date is not UNSET:
            field_dict["setDate"] = set_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        def _parse_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_set_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                set_date_type_0 = isoparse(data).date()

                return set_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        set_date = _parse_set_date(d.pop("setDate", UNSET))

        status = cls(
            name=name,
            code=code,
            set_date=set_date,
        )

        return status
