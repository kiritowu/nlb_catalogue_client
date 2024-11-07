import pytest

from nlb_catalogue_client.models.facet import Facet
from nlb_catalogue_client.models.facet_data import FacetData
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def facet_data_instance():
    return FacetData(id="audioBook", data="Audio Book", count=100)


@pytest.fixture()
def facet_full(facet_data_instance: FacetData) -> tuple[Facet, dict]:
    return Facet(id="materialType", name="Material Type", values=[facet_data_instance]), {
        "id": "materialType",
        "name": "Material Type",
        "values": [facet_data_instance.to_dict()],
    }


@pytest.fixture()
def facet_required_only():
    return Facet(), {}


@pytest.fixture()
def facet_with_none():
    return Facet(id=None, name=None, values=None), {"id": None, "name": None, "values": None}


class TestFacet:
    @pytest.mark.parametrize(
        "id,name,values",
        [
            (
                "materialType",
                "Material Type",
                [FacetData(id="book", data="Book", count=100)],
            ),
            (None, None, None),
            (UNSET, UNSET, UNSET),
        ],
    )
    def test_basic_initialization(self, id, name, values):
        facet = Facet(id=id, name=name, values=values)
        assert facet.id == id
        assert facet.name == name
        assert facet.values == values

    def test_to_dict_full(self, facet_full):
        assert facet_full[0].to_dict() == facet_full[1]

    def test_to_dict_required_only(self, facet_required_only):
        assert facet_required_only[0].to_dict() == facet_required_only[1]

    def test_to_dict_with_none(self, facet_with_none):
        assert facet_with_none[0].to_dict() == facet_with_none[1]

    def test_from_dict_full(self, facet_full):
        assert Facet.from_dict(facet_full[1]) == facet_full[0]

    def test_from_dict_required_only(self, facet_required_only):
        assert Facet.from_dict(facet_required_only[1]) == facet_required_only[0]

    def test_from_dict_with_none(self, facet_with_none):
        assert Facet.from_dict(facet_with_none[1]) == facet_with_none[0]

    @pytest.mark.parametrize(
        "input_data,expected_id,expected_name,expected_values",
        [
            (
                {"id": "materialType", "name": "Material Type", "values": "invalid_value"},
                "materialType",
                "Material Type",
                "invalid_value",
            ),
        ],
    )
    def test_from_dict_edge_cases(self, input_data, expected_id, expected_name, expected_values):
        facet = Facet.from_dict(input_data)
        assert facet.id == expected_id
        assert facet.name == expected_name
        assert facet.values == expected_values
