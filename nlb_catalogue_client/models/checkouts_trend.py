from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkouts_title import CheckoutsTitle


T = TypeVar("T", bound="CheckoutsTrend")


@_attrs_define
class CheckoutsTrend:
    """
    Attributes:
        language (Union[None, Unset, str]): Language are are English, Chinese, Malay, Tamil.. Example: 99999999.
        age_level (Union[None, Unset, str]): ageLevel  A - Adult ,* Y - Young, *J - Juni0r.
        fiction (Union[Unset, bool]): Fiction or not
        singapore_collection (Union[Unset, bool]): Singapore Collection or not
        checkouts_titles (Union[List['CheckoutsTitle'], None, Unset]): checkoutsTitles
    """

    language: Union[None, Unset, str] = UNSET
    age_level: Union[None, Unset, str] = UNSET
    fiction: Union[Unset, bool] = UNSET
    singapore_collection: Union[Unset, bool] = UNSET
    checkouts_titles: Union[List["CheckoutsTitle"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        language: Union[None, Unset, str]
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        age_level: Union[None, Unset, str]
        if isinstance(self.age_level, Unset):
            age_level = UNSET
        else:
            age_level = self.age_level

        fiction = self.fiction

        singapore_collection = self.singapore_collection

        checkouts_titles: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.checkouts_titles, Unset):
            checkouts_titles = UNSET
        elif isinstance(self.checkouts_titles, list):
            checkouts_titles = []
            for checkouts_titles_type_0_item_data in self.checkouts_titles:
                checkouts_titles_type_0_item = checkouts_titles_type_0_item_data.to_dict()
                checkouts_titles.append(checkouts_titles_type_0_item)

        else:
            checkouts_titles = self.checkouts_titles

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if language is not UNSET:
            field_dict["language"] = language
        if age_level is not UNSET:
            field_dict["ageLevel"] = age_level
        if fiction is not UNSET:
            field_dict["fiction"] = fiction
        if singapore_collection is not UNSET:
            field_dict["singaporeCollection"] = singapore_collection
        if checkouts_titles is not UNSET:
            field_dict["checkoutsTitles"] = checkouts_titles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkouts_title import CheckoutsTitle

        d = src_dict.copy()

        def _parse_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_age_level(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        age_level = _parse_age_level(d.pop("ageLevel", UNSET))

        fiction = d.pop("fiction", UNSET)

        singapore_collection = d.pop("singaporeCollection", UNSET)

        def _parse_checkouts_titles(data: object) -> Union[List["CheckoutsTitle"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                checkouts_titles_type_0 = []
                _checkouts_titles_type_0 = data
                for checkouts_titles_type_0_item_data in _checkouts_titles_type_0:
                    checkouts_titles_type_0_item = CheckoutsTitle.from_dict(checkouts_titles_type_0_item_data)

                    checkouts_titles_type_0.append(checkouts_titles_type_0_item)

                return checkouts_titles_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["CheckoutsTitle"], None, Unset], data)

        checkouts_titles = _parse_checkouts_titles(d.pop("checkoutsTitles", UNSET))

        checkouts_trend = cls(
            language=language,
            age_level=age_level,
            fiction=fiction,
            singapore_collection=singapore_collection,
            checkouts_titles=checkouts_titles,
        )

        return checkouts_trend
