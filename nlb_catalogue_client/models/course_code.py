from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CourseCode")


@_attrs_define
class CourseCode:
    """Course Code.

    Attributes:
        code (str): Course Code. Example: N1001.
        cluster_name (str): Cluster Name. Example: Lifestyle Design.
        category_name (Union[None, Unset, str]): Category Name. Example: Culture & Society.
    """

    code: str
    cluster_name: str
    category_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        cluster_name = self.cluster_name

        category_name: Union[None, Unset, str]
        if isinstance(self.category_name, Unset):
            category_name = UNSET
        else:
            category_name = self.category_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "code": code,
                "clusterName": cluster_name,
            }
        )
        if category_name is not UNSET:
            field_dict["categoryName"] = category_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        cluster_name = d.pop("clusterName")

        def _parse_category_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        category_name = _parse_category_name(d.pop("categoryName", UNSET))

        course_code = cls(
            code=code,
            cluster_name=cluster_name,
            category_name=category_name,
        )

        return course_code
