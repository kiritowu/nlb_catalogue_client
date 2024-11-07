import pytest

from nlb_catalogue_client.models.bib_format import BibFormat


@pytest.fixture()
def bib_format_full() -> tuple[BibFormat, dict]:
    return BibFormat(code="BK", name="BOOKS"), {"code": "BK", "name": "BOOKS"}


class TestBibFormat:
    @pytest.mark.parametrize(
        "code,name",
        [
            ("BK", "BOOKS"),
            ("SR", "SERIALS"),
            ("", ""),
        ],
    )
    def test_basic_initialization(self, code, name):
        bib_format = BibFormat(code=code, name=name)
        assert bib_format.code == code
        assert bib_format.name == name

    def test_to_dict_full(self, bib_format_full):
        assert bib_format_full[0].to_dict() == bib_format_full[1]

    def test_from_dict_full(self, bib_format_full):
        assert BibFormat.from_dict(bib_format_full[1]) == bib_format_full[0]
