from nlb_catalogue_client.models.get_availability_info_response_v2 import GetAvailabilityInfoResponseV2
from nlb_catalogue_client.models.item import Item
from nlb_catalogue_client.models.location import Location
from nlb_catalogue_client.models.media import Media
from nlb_catalogue_client.models.transaction_status import TransactionStatus
from nlb_catalogue_client.models.usage_level import UsageLevel
from nlb_catalogue_client.types import UNSET


class TestGetAvailabilityInfoResponseV2:
    def setup_method(self):
        """Setup common test objects"""
        self.media = Media(code="BK", name="BOOKS")
        self.usage_level = UsageLevel(code="A", name="Adult")
        self.location = Location(code="AMKL", name="Ang Mo Kio Library")
        self.transaction_status = TransactionStatus(code="A", name="Available")
        self.item = Item(
            media=self.media,
            usage_level=self.usage_level,
            location=self.location,
            transaction_status=self.transaction_status,
        )

    def test_basic_initialization(self):
        """Test initialization with all fields"""
        response = GetAvailabilityInfoResponseV2(
            set_id=123, total_records=100, count=20, has_more_records=True, next_records_offset=20, items=[self.item]
        )

        assert response.set_id == 123
        assert response.total_records == 100
        assert response.count == 20
        assert response.has_more_records is True
        assert response.next_records_offset == 20
        assert response.items == [self.item]

    def test_initialization_with_required_only(self):
        """Test initialization with no fields (all optional)"""
        response = GetAvailabilityInfoResponseV2()

        assert response.set_id is UNSET
        assert response.total_records is UNSET
        assert response.count is UNSET
        assert response.has_more_records is False  # Default value
        assert response.next_records_offset is UNSET
        assert response.items is UNSET

    def test_to_dict_full(self):
        """Test converting to dictionary with all fields"""
        response = GetAvailabilityInfoResponseV2(
            set_id=123, total_records=100, count=20, has_more_records=True, next_records_offset=20, items=[self.item]
        )

        expected = {
            "setId": 123,
            "totalRecords": 100,
            "count": 20,
            "hasMoreRecords": True,
            "nextRecordsOffset": 20,
            "items": [
                {
                    "media": {"code": "BK", "name": "BOOKS"},
                    "usageLevel": {"code": "A", "name": "Adult"},
                    "location": {"code": "AMKL", "name": "Ang Mo Kio Library"},
                    "transactionStatus": {"code": "A", "name": "Available"},
                }
            ],
        }

        assert response.to_dict() == expected

    def test_to_dict_required_only(self):
        """Test converting to dictionary with no fields set"""
        response = GetAvailabilityInfoResponseV2()

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
            "items": [
                {
                    "media": {"code": "BK", "name": "BOOKS"},
                    "usageLevel": {"code": "A", "name": "Adult"},
                    "location": {"code": "AMKL", "name": "Ang Mo Kio Library"},
                    "transactionStatus": {"code": "A", "name": "Available"},
                }
            ],
        }

        response = GetAvailabilityInfoResponseV2.from_dict(data)

        assert response.set_id == 123
        assert response.total_records == 100
        assert response.count == 20
        assert response.has_more_records is True
        assert response.next_records_offset == 20
        assert response.items
        assert len(response.items) == 1
        assert isinstance(response.items[0], Item)
        assert response.items[0].media.code == "BK"

    def test_from_dict_required_only(self):
        """Test creating object from empty dictionary"""
        data = {}

        response = GetAvailabilityInfoResponseV2.from_dict(data)

        assert response.set_id is UNSET
        assert response.total_records is UNSET
        assert response.count is UNSET
        assert response.has_more_records is UNSET
        assert response.next_records_offset is UNSET
        assert response.items == []
