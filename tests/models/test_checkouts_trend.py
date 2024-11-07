import pytest

from nlb_catalogue_client.models.checkouts_title import CheckoutsTitle
from nlb_catalogue_client.models.checkouts_trend import CheckoutsTrend
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def sample_checkouts_title():
    return CheckoutsTitle(
        title="Test Book",
        native_title="测试书",
        author="John Doe",
        native_author="约翰",
        isbns=["1234567890"],
        checkouts_count=5,
    )


@pytest.fixture()
def checkouts_trend_full(sample_checkouts_title) -> tuple[CheckoutsTrend, dict]:
    return CheckoutsTrend(
        language="English",
        age_level="A",
        fiction=True,
        singapore_collection=False,
        checkouts_titles=[sample_checkouts_title],
    ), {
        "language": "English",
        "ageLevel": "A",
        "fiction": True,
        "singaporeCollection": False,
        "checkoutsTitles": [sample_checkouts_title.to_dict()],
    }


@pytest.fixture()
def checkouts_trend_with_none() -> tuple[CheckoutsTrend, dict]:
    return CheckoutsTrend(language=None, age_level=None, checkouts_titles=None), {
        "language": None,
        "ageLevel": None,
        "checkoutsTitles": None,
    }


class TestCheckoutsTrend:
    @pytest.mark.parametrize(
        "language,age_level,fiction,singapore_collection,checkouts_titles,expected_titles_len",
        [
            ("English", "A", True, False, [CheckoutsTitle(title="Test Book")], 1),
            (None, None, True, False, None, None),
            (UNSET, UNSET, UNSET, UNSET, UNSET, None),
        ],
    )
    def test_basic_initialization(
        self, language, age_level, fiction, singapore_collection, checkouts_titles, expected_titles_len
    ):
        trend = CheckoutsTrend(
            language=language,
            age_level=age_level,
            fiction=fiction,
            singapore_collection=singapore_collection,
            checkouts_titles=checkouts_titles,
        )
        assert trend.language == language
        assert trend.age_level == age_level
        assert trend.fiction == fiction
        assert trend.singapore_collection == singapore_collection
        assert trend.checkouts_titles == checkouts_titles
        if expected_titles_len:
            assert isinstance(trend.checkouts_titles, list)
            assert len(trend.checkouts_titles) == expected_titles_len

    def test_to_dict_full(self, checkouts_trend_full):
        assert checkouts_trend_full[0].to_dict() == checkouts_trend_full[1]

    def test_to_dict_with_none(self, checkouts_trend_with_none):
        assert checkouts_trend_with_none[0].to_dict() == checkouts_trend_with_none[1]

    def test_to_dict_with_unset(self):
        trend = CheckoutsTrend()
        assert trend.to_dict() == {}

    def test_from_dict_full(self, checkouts_trend_full):
        assert CheckoutsTrend.from_dict(checkouts_trend_full[1]) == checkouts_trend_full[0]

    def test_from_dict_with_none(self, checkouts_trend_with_none):
        assert CheckoutsTrend.from_dict(checkouts_trend_with_none[1]) == checkouts_trend_with_none[0]

    @pytest.mark.parametrize(
        "input_data,expected_language,expected_age_level,expected_fiction,expected_singapore_collection,expected_checkouts_titles",
        [
            ({"language": "English", "fiction": True}, "English", UNSET, True, UNSET, UNSET),
            (
                {
                    "language": "English",
                    "ageLevel": "A",
                    "fiction": True,
                    "singaporeCollection": False,
                    "checkoutsTitles": "invalid_value",
                },
                "English",
                "A",
                True,
                False,
                "invalid_value",
            ),
            (
                {
                    "language": UNSET,
                    "ageLevel": UNSET,
                    "fiction": UNSET,
                    "singaporeCollection": UNSET,
                    "checkoutsTitles": UNSET,
                },
                UNSET,
                UNSET,
                UNSET,
                UNSET,
                UNSET,
            ),
        ],
    )
    def test_from_dict_edge_cases(
        self,
        input_data,
        expected_language,
        expected_age_level,
        expected_fiction,
        expected_singapore_collection,
        expected_checkouts_titles,
    ):
        trend = CheckoutsTrend.from_dict(input_data)
        assert trend.language == expected_language
        assert trend.age_level == expected_age_level
        assert trend.fiction == expected_fiction
        assert trend.singapore_collection == expected_singapore_collection
        assert trend.checkouts_titles == expected_checkouts_titles
