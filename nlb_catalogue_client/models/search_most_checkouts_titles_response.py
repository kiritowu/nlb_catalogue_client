from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkouts_trend import CheckoutsTrend


T = TypeVar("T", bound="SearchMostCheckoutsTitlesResponse")


@_attrs_define
class SearchMostCheckoutsTitlesResponse:
    """
    Attributes:
        checkouts_trends (Union[Unset, List['CheckoutsTrend']]):
    """

    checkouts_trends: Union[Unset, List["CheckoutsTrend"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        checkouts_trends: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.checkouts_trends, Unset):
            checkouts_trends = []
            for checkouts_trends_item_data in self.checkouts_trends:
                checkouts_trends_item = checkouts_trends_item_data.to_dict()
                checkouts_trends.append(checkouts_trends_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if checkouts_trends is not UNSET:
            field_dict["checkoutsTrends"] = checkouts_trends

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkouts_trend import CheckoutsTrend

        d = src_dict.copy()
        checkouts_trends = []
        _checkouts_trends = d.pop("checkoutsTrends", UNSET)
        for checkouts_trends_item_data in _checkouts_trends or []:
            checkouts_trends_item = CheckoutsTrend.from_dict(checkouts_trends_item_data)

            checkouts_trends.append(checkouts_trends_item)

        search_most_checkouts_titles_response = cls(
            checkouts_trends=checkouts_trends,
        )

        return search_most_checkouts_titles_response
