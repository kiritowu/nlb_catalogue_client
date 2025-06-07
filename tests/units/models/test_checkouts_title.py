import pytest

from nlb_catalogue_client.models.checkouts_title import CheckoutsTitle
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def checkouts_title_full() -> tuple[CheckoutsTitle, dict]:
    return CheckoutsTitle(
        title="Test Book",
        native_title="测试书",
        author="John Doe",
        native_author="约翰",
        isbns=["1234567890"],
        checkouts_count=5,
    ), {
        "title": "Test Book",
        "nativeTitle": "测试书",
        "author": "John Doe",
        "nativeAuthor": "约翰",
        "isbns": ["1234567890"],
        "checkoutsCount": 5,
    }


@pytest.fixture()
def checkouts_title_required_only():
    return CheckoutsTitle(), {}


@pytest.fixture()
def checkouts_title_with_none():
    return CheckoutsTitle(
        title=None, native_title=None, author=None, native_author=None, isbns=None, checkouts_count=0
    ), {"title": None, "nativeTitle": None, "author": None, "nativeAuthor": None, "isbns": None, "checkoutsCount": 0}


class TestCheckoutsTitle:
    @pytest.mark.parametrize(
        "title,native_title,author,native_author,isbns,checkouts_count",
        [
            ("Test Book", "测试书", "John Doe", "约翰", ["1234567890"], 5),
            (None, None, None, None, None, 0),
            (UNSET, UNSET, UNSET, UNSET, UNSET, UNSET),
        ],
    )
    def test_basic_initialization(self, title, native_title, author, native_author, isbns, checkouts_count):
        checkout = CheckoutsTitle(
            title=title,
            native_title=native_title,
            author=author,
            native_author=native_author,
            isbns=isbns,
            checkouts_count=checkouts_count,
        )
        assert checkout.title == title
        assert checkout.native_title == native_title
        assert checkout.author == author
        assert checkout.native_author == native_author
        assert checkout.isbns == isbns
        assert checkout.checkouts_count == checkouts_count

    def test_to_dict_full(self, checkouts_title_full):
        assert checkouts_title_full[0].to_dict() == checkouts_title_full[1]

    def test_to_dict_required_only(self, checkouts_title_required_only):
        assert checkouts_title_required_only[0].to_dict() == checkouts_title_required_only[1]

    def test_to_dict_with_none(self, checkouts_title_with_none):
        assert checkouts_title_with_none[0].to_dict() == checkouts_title_with_none[1]

    def test_from_dict_full(self, checkouts_title_full):
        assert CheckoutsTitle.from_dict(checkouts_title_full[1]) == checkouts_title_full[0]

    def test_from_dict_required_only(self, checkouts_title_required_only):
        assert CheckoutsTitle.from_dict(checkouts_title_required_only[1]) == checkouts_title_required_only[0]

    def test_from_dict_with_none(self, checkouts_title_with_none):
        assert CheckoutsTitle.from_dict(checkouts_title_with_none[1]) == checkouts_title_with_none[0]

    @pytest.mark.parametrize(
        "input_data,expected_title,expected_isbns",
        [
            (
                {"title": "Test Book", "checkoutsCount": 5},
                "Test Book",
                UNSET,
            ),
            (
                {"title": None, "isbns": 123},
                None,
                123,
            ),
        ],
    )
    def test_from_dict_edge_cases(self, input_data, expected_title, expected_isbns):
        checkout = CheckoutsTitle.from_dict(input_data)
        assert checkout.title == expected_title
        assert checkout.isbns == expected_isbns
