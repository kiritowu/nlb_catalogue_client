from nlb_catalogue_client.models.bib_format import BibFormat
from nlb_catalogue_client.models.get_titles_response_v2 import GetTitlesResponseV2
from nlb_catalogue_client.models.title import Title
from nlb_catalogue_client.types import UNSET


class TestGetTitlesResponseV2:
    def setup_method(self):
        """Setup common test objects"""
        self.format_ = BibFormat(code="BK", name="BOOKS")
        self.title = Title(
            format_=self.format_,
            title="Sample Book",
            author="John Doe",
            brn=99999999,
        )

    def test_basic_initialization(self):
        """Test initialization with all fields"""
        response = GetTitlesResponseV2(
            set_id=123,
            total_records=100,
            count=20,
            has_more_records=True,
            next_records_offset=20,
            titles=[self.title],
        )

        assert response.set_id == 123
        assert response.total_records == 100
        assert response.count == 20
        assert response.has_more_records is True
        assert response.next_records_offset == 20
        assert response.titles == [self.title]

    def test_initialization_with_required_only(self):
        """Test initialization with no fields (all optional)"""
        response = GetTitlesResponseV2()

        assert response.set_id is UNSET
        assert response.total_records is UNSET
        assert response.count is UNSET
        assert response.has_more_records is False  # Default value
        assert response.next_records_offset is UNSET
        assert response.titles is UNSET

    def test_to_dict_full(self):
        """Test converting to dictionary with all fields"""
        response = GetTitlesResponseV2(
            set_id=123,
            total_records=100,
            count=20,
            has_more_records=True,
            next_records_offset=20,
            titles=[self.title],
        )

        expected = {
            "setId": 123,
            "totalRecords": 100,
            "count": 20,
            "hasMoreRecords": True,
            "nextRecordsOffset": 20,
            "titles": [
                {
                    "format": {"code": "BK", "name": "BOOKS"},
                    "title": "Sample Book",
                    "author": "John Doe",
                    "brn": 99999999,
                    "allowReservation": True,
                    "isRestricted": False,
                    "serial": False,
                }
            ],
        }

        assert response.to_dict() == expected

    def test_to_dict_required_only(self):
        """Test converting to dictionary with no fields set"""
        response = GetTitlesResponseV2()

        # Only hasMoreRecords should be included as it has a default value
        expected = {"hasMoreRecords": False}

        assert response.to_dict() == expected

    def test_from_dict_full(self):
        """Test creating object from dictionary with all fields"""
        data = {
            "setId": 123,
            "totalRecords": 100,
            "count": 20,
            "hasMoreRecords": True,
            "nextRecordsOffset": 20,
            "titles": [
                {
                    "format": {"code": "BK", "name": "BOOKS"},
                    "title": "Sample Book",
                    "author": "John Doe",
                    "brn": 99999999,
                    "allowReservation": True,
                    "isRestricted": False,
                    "serial": False,
                }
            ],
        }

        response = GetTitlesResponseV2.from_dict(data)

        assert response.set_id == 123
