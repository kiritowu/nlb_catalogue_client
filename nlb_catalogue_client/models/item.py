from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.course_code import CourseCode
    from ..models.location import Location
    from ..models.media import Media
    from ..models.status import Status
    from ..models.transaction_status import TransactionStatus
    from ..models.usage_level import UsageLevel


T = TypeVar("T", bound="Item")


@_attrs_define
class Item:
    """
    Attributes:
        media (Media): Item Material Type. Please refer to code list C002.
        usage_level (UsageLevel): Usage Level. Please refer to code list C004.
        location (Location): Library Location. Please refer to code list C005.
        transaction_status (TransactionStatus): Item Transactional Status. Please refer to code list C003.
        irn (Union[Unset, int]): Item Internal Identifier. Example: 99999999.
        item_id (Union[Unset, str]): Item Id. Example: BxxxxxxxJ.
        brn (Union[Unset, int]): Title record Book Reference Number. Example: 99999999.
        volume_name (Union[None, Unset, str]): Volume Identifier. Example: 2023 issue 1.
        call_number (Union[Unset, str]): Call Number. Example: 123.123 ART.
        formatted_call_number (Union[Unset, str]): Formatted Call Number. Example: English 123.123 -[ART].
        course_code (Union[Unset, CourseCode]): Course Code.
        language (Union[Unset, str]): Language. Example: English.
        suffix (Union[None, Unset, str]): Suffix. Example: -[ART].
        donor (Union[None, Unset, str]): Item donated by information. Example: Donated by abc.
        price (Union[None, Unset, float]): Item price. Example: 9999.99.
        status (Union[Unset, Status]): Item Status.
        min_age_limit (Union[Unset, int]): Title age limit. Example: 13.
    """

    media: "Media"
    usage_level: "UsageLevel"
    location: "Location"
    transaction_status: "TransactionStatus"
    irn: Union[Unset, int] = UNSET
    item_id: Union[Unset, str] = UNSET
    brn: Union[Unset, int] = UNSET
    volume_name: Union[None, Unset, str] = UNSET
    call_number: Union[Unset, str] = UNSET
    formatted_call_number: Union[Unset, str] = UNSET
    course_code: Union[Unset, "CourseCode"] = UNSET
    language: Union[Unset, str] = UNSET
    suffix: Union[None, Unset, str] = UNSET
    donor: Union[None, Unset, str] = UNSET
    price: Union[None, Unset, float] = UNSET
    status: Union[Unset, "Status"] = UNSET
    min_age_limit: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        media = self.media.to_dict()

        usage_level = self.usage_level.to_dict()

        location = self.location.to_dict()

        transaction_status = self.transaction_status.to_dict()

        irn = self.irn

        item_id = self.item_id

        brn = self.brn

        volume_name: Union[None, Unset, str]
        if isinstance(self.volume_name, Unset):
            volume_name = UNSET
        else:
            volume_name = self.volume_name

        call_number = self.call_number

        formatted_call_number = self.formatted_call_number

        course_code: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.course_code, Unset):
            course_code = self.course_code.to_dict()

        language = self.language

        suffix: Union[None, Unset, str]
        if isinstance(self.suffix, Unset):
            suffix = UNSET
        else:
            suffix = self.suffix

        donor: Union[None, Unset, str]
        if isinstance(self.donor, Unset):
            donor = UNSET
        else:
            donor = self.donor

        price: Union[None, Unset, float]
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        min_age_limit = self.min_age_limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "media": media,
                "usageLevel": usage_level,
                "location": location,
                "transactionStatus": transaction_status,
            }
        )
        if irn is not UNSET:
            field_dict["irn"] = irn
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if brn is not UNSET:
            field_dict["brn"] = brn
        if volume_name is not UNSET:
            field_dict["volumeName"] = volume_name
        if call_number is not UNSET:
            field_dict["callNumber"] = call_number
        if formatted_call_number is not UNSET:
            field_dict["formattedCallNumber"] = formatted_call_number
        if course_code is not UNSET:
            field_dict["courseCode"] = course_code
        if language is not UNSET:
            field_dict["language"] = language
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if donor is not UNSET:
            field_dict["donor"] = donor
        if price is not UNSET:
            field_dict["price"] = price
        if status is not UNSET:
            field_dict["status"] = status
        if min_age_limit is not UNSET:
            field_dict["minAgeLimit"] = min_age_limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.course_code import CourseCode
        from ..models.location import Location
        from ..models.media import Media
        from ..models.status import Status
        from ..models.transaction_status import TransactionStatus
        from ..models.usage_level import UsageLevel

        d = src_dict.copy()
        media = Media.from_dict(d.pop("media"))

        usage_level = UsageLevel.from_dict(d.pop("usageLevel"))

        location = Location.from_dict(d.pop("location"))

        transaction_status = TransactionStatus.from_dict(d.pop("transactionStatus"))

        irn = d.pop("irn", UNSET)

        item_id = d.pop("itemId", UNSET)

        brn = d.pop("brn", UNSET)

        def _parse_volume_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        volume_name = _parse_volume_name(d.pop("volumeName", UNSET))

        call_number = d.pop("callNumber", UNSET)

        formatted_call_number = d.pop("formattedCallNumber", UNSET)

        _course_code = d.pop("courseCode", UNSET)
        course_code: Union[Unset, CourseCode]
        if isinstance(_course_code, Unset):
            course_code = UNSET
        else:
            course_code = CourseCode.from_dict(_course_code)

        language = d.pop("language", UNSET)

        def _parse_suffix(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suffix = _parse_suffix(d.pop("suffix", UNSET))

        def _parse_donor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        donor = _parse_donor(d.pop("donor", UNSET))

        def _parse_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        price = _parse_price(d.pop("price", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Status.from_dict(_status)

        min_age_limit = d.pop("minAgeLimit", UNSET)

        item = cls(
            media=media,
            usage_level=usage_level,
            location=location,
            transaction_status=transaction_status,
            irn=irn,
            item_id=item_id,
            brn=brn,
            volume_name=volume_name,
            call_number=call_number,
            formatted_call_number=formatted_call_number,
            course_code=course_code,
            language=language,
            suffix=suffix,
            donor=donor,
            price=price,
            status=status,
            min_age_limit=min_age_limit,
        )

        return item
