import pytest

from nlb_catalogue_client.models.facet_data import FacetData
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def facet_data() -> tuple[FacetData, dict]:
    return FacetData(id="audioBook", data="Audio Book", count=17), {
        "id": "audioBook",
        "data": "Audio Book",
        "count": 17,
    }


@pytest.fixture()
def facet_data_required_only():
    return FacetData(), {}


@pytest.fixture()
def facet_data_with_none():
    return FacetData(id=None, data=None), {"id": None, "data": None}


class TestFacetData:
    @pytest.mark.parametrize(
        "id,data,count", [("audioBook", "Audio Book", 17), (None, None, None), (UNSET, UNSET, UNSET)]
    )
    def test_basic_initialization(self, id, data, count):
        facet = FacetData(id=id, data=data, count=count)
        assert facet.id == id
        assert facet.data == data
        assert facet.count == count

    def test_to_dict_full(self, facet_data):
        assert facet_data[0].to_dict() == facet_data[1]

    def test_to_dict_required_only(self, facet_data_required_only):
        assert facet_data_required_only[0].to_dict() == facet_data_required_only[1]

    def test_to_dict_with_none(self, facet_data_with_none):
        assert facet_data_with_none[0].to_dict() == facet_data_with_none[1]

    def test_from_dict_full(self, facet_data):
        assert FacetData.from_dict(facet_data[1]) == facet_data[0]

    def test_from_dict_required_only(self, facet_data_required_only):
        assert FacetData.from_dict(facet_data_required_only[1]) == facet_data_required_only[0]

    def test_from_dict_with_none(self, facet_data_with_none):
        assert FacetData.from_dict(facet_data_with_none[1]) == facet_data_with_none[0]
