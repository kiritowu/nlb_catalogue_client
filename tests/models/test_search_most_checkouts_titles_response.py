from nlb_catalogue_client.models.checkouts_title import CheckoutsTitle
from nlb_catalogue_client.models.checkouts_trend import CheckoutsTrend
from nlb_catalogue_client.models.search_most_checkouts_titles_response import SearchMostCheckoutsTitlesResponse
from nlb_catalogue_client.types import UNSET


class TestSearchMostCheckoutsTitlesResponse:
    def setup_method(self):
        """Setup common test objects"""
        self.checkouts_title = CheckoutsTitle(
            title="Sample Book",
            native_title="样本书",
            author="John Doe",
            native_author="约翰·多伊",
            isbns=["9709999999"],
            checkouts_count=100,
        )

        self.checkouts_trend = CheckoutsTrend(
            language="English",
            age_level="A",
            fiction=True,
            singapore_collection=False,
            checkouts_titles=[self.checkouts_title],
        )

    def test_basic_initialization(self):
        """Test initialization with all fields"""
        response = SearchMostCheckoutsTitlesResponse(
            checkouts_trends=[self.checkouts_trend],
        )

        assert response.checkouts_trends == [self.checkouts_trend]

    def test_initialization_with_unset(self):
        """Test initialization with UNSET values"""
        response = SearchMostCheckoutsTitlesResponse()

        assert response.checkouts_trends is UNSET

    def test_to_dict_full(self):
        """Test converting to dictionary with all fields"""
        response = SearchMostCheckoutsTitlesResponse(
            checkouts_trends=[self.checkouts_trend],
        )

        expected = {
            "checkoutsTrends": [
                {
                    "language": "English",
                    "ageLevel": "A",
                    "fiction": True,
                    "singaporeCollection": False,
                    "checkoutsTitles": [
                        {
                            "title": "Sample Book",
                            "nativeTitle": "样本书",
                            "author": "John Doe",
                            "nativeAuthor": "约翰·多伊",
                            "isbns": ["9709999999"],
                            "checkoutsCount": 100,
                        }
                    ],
                }
            ]
        }

        assert response.to_dict() == expected

    def test_to_dict_unset(self):
        """Test converting to dictionary with no fields set"""
        response = SearchMostCheckoutsTitlesResponse()

        expected = {}

        assert response.to_dict() == expected

    def test_from_dict_full(self):
        """Test creating object from dictionary with all fields"""
        data = {
            "checkoutsTrends": [
                {
                    "language": "English",
                    "ageLevel": "A",
                    "fiction": True,
                    "singaporeCollection": False,
                    "checkoutsTitles": [
                        {
                            "title": "Sample Book",
                            "nativeTitle": "样本书",
                            "author": "John Doe",
                            "nativeAuthor": "约翰·多伊",
                            "isbns": ["9709999999"],
                            "checkoutsCount": 100,
                        }
                    ],
                }
            ]
        }

        response = SearchMostCheckoutsTitlesResponse.from_dict(data)

        assert len(response.checkouts_trends) == 1
        trend = response.checkouts_trends[0]
        assert trend.language == "English"
        assert trend.age_level == "A"
        assert trend.fiction is True
        assert trend.singapore_collection is False
        assert len(trend.checkouts_titles) == 1
        title = trend.checkouts_titles[0]
        assert title.title == "Sample Book"
        assert title.native_title == "样本书"
        assert title.author == "John Doe"
        assert title.native_author == "约翰·多伊"
        assert title.isbns == ["9709999999"]
        assert title.checkouts_count == 100

    def test_from_dict_empty(self):
        """Test creating object from empty dictionary"""
        data = {}

        response = SearchMostCheckoutsTitlesResponse.from_dict(data)

        assert response.checkouts_trends == []

    def test_from_dict_with_none(self):
        """Test creating object from dictionary with None values"""
        data = {
            "checkoutsTrends": [
                {
                    "language": None,
                    "ageLevel": None,
                    "checkoutsTitles": None,
                }
            ]
        }

        response = SearchMostCheckoutsTitlesResponse.from_dict(data)
        trend = response.checkouts_trends[0]

        assert trend.language is None
        assert trend.age_level is None
        assert trend.checkouts_titles is None

    def test_from_dict_with_invalid_values(self):
        """Test creating object from dictionary with invalid field types"""
        data = {
            "checkoutsTrends": [
                {
                    "language": 123,  # Should be string
                    "ageLevel": True,  # Should be string
                    "fiction": "Not a boolean",  # Should be boolean
                    "singaporeCollection": "Not a boolean",  # Should be boolean
                    "checkoutsTitles": [
                        {
                            "title": 123,  # Should be string
                            "isbns": "Not a list",  # Should be list
                            "checkoutsCount": "Not an integer",  # Should be integer
                        }
                    ],
                }
            ]
        }

        response = SearchMostCheckoutsTitlesResponse.from_dict(data)
        trend = response.checkouts_trends[0]
        title = trend.checkouts_titles[0]

        # Verify invalid values are returned as-is
        assert trend.language == 123
        assert trend.age_level is True
        assert trend.fiction == "Not a boolean"
        assert trend.singapore_collection == "Not a boolean"
        assert title.title == 123
        assert title.isbns == "Not a list"
        assert title.checkouts_count == "Not an integer"
