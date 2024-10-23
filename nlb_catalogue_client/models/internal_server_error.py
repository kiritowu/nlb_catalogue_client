from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalServerError")


@_attrs_define
class InternalServerError:
    """Error contents including the specific error

    Attributes:
        error (str): The type of the error. Example: Internal Server Error.
        message (str): The message of the error. Example: Internal server error.
        status_code (Union[Unset, int]): The status code of the error. Example: 500.
    """

    error: str
    message: str
    status_code: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        error = self.error

        message = self.message

        status_code = self.status_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "error": error,
                "message": message,
            }
        )
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error = d.pop("error")

        message = d.pop("message")

        status_code = d.pop("statusCode", UNSET)

        internal_server_error = cls(
            error=error,
            message=message,
            status_code=status_code,
        )

        return internal_server_error