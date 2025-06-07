from datetime import datetime

from nlb_catalogue_client.models.course_code import CourseCode
from nlb_catalogue_client.models.item import Item
from nlb_catalogue_client.models.location import Location
from nlb_catalogue_client.models.media import Media
from nlb_catalogue_client.models.status import Status
from nlb_catalogue_client.models.transaction_status import TransactionStatus
from nlb_catalogue_client.models.usage_level import UsageLevel
from nlb_catalogue_client.types import UNSET, Unset


class TestItem:
    def setup_method(self):
        """Setup common test objects"""
        self.media = Media(code="DV18", name="Digital Video for M18")
        self.usage_level = UsageLevel(code="001", name="Junior Picture Adult Lending")
        self.location = Location(code="AMKPL", name="Ang Mo Kio Public Library")
        self.course_code = CourseCode(code="N1001", cluster_name="Lifestyle Design", category_name="Culture & Society")
        self.transaction_status = TransactionStatus(
            code="I",
            name="In Transit",
            date=datetime(2019, 7, 21, 14, 32, 45),
            in_transit_from=Location(code="AMKPL", name="Ang Mo Kio Public Library"),
            in_transit_to=Location(code="BBPL", name="Bukit Batok Public Library"),
        )
        self.status = Status(code="A", name="Available")

    def test_basic_initialization(self):
        item = Item(
            media=self.media,
            usage_level=self.usage_level,
            location=self.location,
            transaction_status=self.transaction_status,
            irn=99999999,
            item_id="BxxxxxxxJ",
            brn=99999999,
            volume_name="2023 issue 1",
            call_number="123.123 ART",
            formatted_call_number="English 123.123 -[ART]",
            course_code=self.course_code,
            language="English",
            suffix="-[ART]",
            donor="Donated by abc",
            price=9999.99,
            status=self.status,
            min_age_limit=13,
        )

        assert item.media == self.media
        assert item.usage_level == self.usage_level
        assert item.location == self.location
        assert item.transaction_status == self.transaction_status
        assert item.irn == 99999999
        assert item.item_id == "BxxxxxxxJ"
        assert item.brn == 99999999
        assert item.volume_name == "2023 issue 1"
        assert item.call_number == "123.123 ART"
        assert item.formatted_call_number == "English 123.123 -[ART]"
        assert item.course_code == self.course_code
        assert item.language == "English"
        assert item.suffix == "-[ART]"
        assert item.donor == "Donated by abc"
        assert item.price == 9999.99
        assert item.status == self.status
        assert item.min_age_limit == 13

    def test_initialization_required_only(self):
        item = Item(
            media=self.media,
            usage_level=self.usage_level,
            location=self.location,
            transaction_status=self.transaction_status,
        )

        assert item.media == self.media
        assert item.usage_level == self.usage_level
        assert item.location == self.location
        assert item.transaction_status == self.transaction_status
        assert item.irn is UNSET
        assert item.item_id is UNSET
        assert item.volume_name is UNSET
        assert item.course_code is UNSET
        assert item.status is UNSET

    def test_to_dict_full(self):
        item = Item(
            media=self.media,
            usage_level=self.usage_level,
            location=self.location,
            transaction_status=self.transaction_status,
            irn=99999999,
            item_id="BxxxxxxxJ",
            brn=99999999,
            volume_name="2023 issue 1",
            call_number="123.123 ART",
            formatted_call_number="English 123.123 -[ART]",
            course_code=self.course_code,
            language="English",
            suffix="-[ART]",
            donor="Donated by abc",
            price=9999.99,
            status=self.status,
            min_age_limit=13,
        )

        result = item.to_dict()
        assert result["media"] == self.media.to_dict()
        assert result["usageLevel"] == self.usage_level.to_dict()
        assert result["location"] == self.location.to_dict()
        assert result["transactionStatus"] == self.transaction_status.to_dict()
        assert result["irn"] == 99999999
        assert result["itemId"] == "BxxxxxxxJ"
        assert result["brn"] == 99999999
        assert result["volumeName"] == "2023 issue 1"
        assert result["callNumber"] == "123.123 ART"
        assert result["formattedCallNumber"] == "English 123.123 -[ART]"
        assert result["courseCode"] == self.course_code.to_dict()
        assert result["language"] == "English"
        assert result["donor"] == "Donated by abc"
        assert result["price"] == 9999.99
        assert result["status"] == self.status.to_dict()
        assert result["minAgeLimit"] == 13

    def test_to_dict_required_only(self):
        item = Item(
            media=self.media,
            usage_level=self.usage_level,
            location=self.location,
            transaction_status=self.transaction_status,
        )

        expected = {
            "media": {"code": "DV18", "name": "Digital Video for M18"},
            "usageLevel": {"code": "001", "name": "Junior Picture Adult Lending"},
            "location": {"code": "AMKPL", "name": "Ang Mo Kio Public Library"},
            "transactionStatus": {
                "code": "I",
                "name": "In Transit",
                "date": "2019-07-21T14:32:45",
                "inTransitFrom": {"code": "AMKPL", "name": "Ang Mo Kio Public Library"},
                "inTransitTo": {"code": "BBPL", "name": "Bukit Batok Public Library"},
            },
        }

        result = item.to_dict()
        assert result == expected

    def test_from_dict_full(self):
        data = {
            "media": {"code": "DV18", "name": "Digital Video for M18"},
            "usageLevel": {"code": "001", "name": "Junior Picture Adult Lending"},
            "location": {"code": "AMKPL", "name": "Ang Mo Kio Public Library"},
            "transactionStatus": {
                "code": "I",
                "name": "In Transit",
                "date": "2019-07-21T14:32:45",
                "inTransitFrom": {"code": "AMKPL", "name": "Ang Mo Kio Public Library"},
                "inTransitTo": {"code": "BBPL", "name": "Bukit Batok Public Library"},
            },
            "irn": 99999999,
            "itemId": "BxxxxxxxJ",
            "brn": 99999999,
            "volumeName": "2023 issue 1",
            "callNumber": "123.123 ART",
            "formattedCallNumber": "English 123.123 -[ART]",
            "courseCode": {"code": "N1001", "clusterName": "Lifestyle Design", "categoryName": "Culture & Society"},
            "language": "English",
            "suffix": "-[ART]",
            "donor": "Donated by abc",
            "price": 9999.99,
            "status": {"code": "A", "name": "Available"},
            "minAgeLimit": 13,
        }

        item = Item.from_dict(data)

        # Test required fields
        assert item.media.code == "DV18"
        assert item.media.name == "Digital Video for M18"
        assert item.usage_level.code == "001"
        assert item.usage_level.name == "Junior Picture Adult Lending"
        assert item.location.code == "AMKPL"
        assert item.location.name == "Ang Mo Kio Public Library"
        assert item.transaction_status.code == "I"
        assert item.transaction_status.name == "In Transit"

        # Test optional fields
        assert item.irn == 99999999
        assert item.item_id == "BxxxxxxxJ"
        assert item.brn == 99999999
        assert item.volume_name == "2023 issue 1"
        assert item.call_number == "123.123 ART"
        assert item.formatted_call_number == "English 123.123 -[ART]"
        assert not isinstance(item.course_code, Unset)
        assert item.course_code.code == "N1001"
        assert item.course_code.cluster_name == "Lifestyle Design"
        assert item.course_code.category_name == "Culture & Society"
        assert item.language == "English"
        assert item.suffix == "-[ART]"
        assert item.donor == "Donated by abc"
        assert item.price == 9999.99
        assert not isinstance(item.status, Unset)
        assert item.status.code == "A"
        assert item.status.name == "Available"
        assert item.min_age_limit == 13

    def test_from_dict_required_only(self):
        data = {
            "media": {"code": "DV18", "name": "Digital Video for M18"},
            "usageLevel": {"code": "001", "name": "Junior Picture Adult Lending"},
            "location": {"code": "AMKPL", "name": "Ang Mo Kio Public Library"},
            "transactionStatus": {
                "code": "I",
                "name": "In Transit",
                "date": "2019-07-21T14:32:45",
                "inTransitFrom": {"code": "AMKPL", "name": "Ang Mo Kio Public Library"},
                "inTransitTo": {"code": "BBPL", "name": "Bukit Batok Public Library"},
            },
        }

        item = Item.from_dict(data)

        # Test required fields are present
        assert item.media.code == "DV18"
        assert item.media.name == "Digital Video for M18"
        assert item.usage_level.code == "001"
        assert item.usage_level.name == "Junior Picture Adult Lending"
        assert item.location.code == "AMKPL"
        assert item.location.name == "Ang Mo Kio Public Library"
        assert item.transaction_status.code == "I"
        assert item.transaction_status.name == "In Transit"

        # Test optional fields are UNSET
        assert item.irn is UNSET
        assert item.item_id is UNSET
        assert item.brn is UNSET
        assert item.volume_name is UNSET
        assert item.call_number is UNSET
        assert item.formatted_call_number is UNSET
        assert item.course_code is UNSET
        assert item.language is UNSET
        assert item.suffix is UNSET
        assert item.donor is UNSET
        assert item.price is UNSET
        assert item.status is UNSET
        assert item.min_age_limit is UNSET

    def test_from_dict_with_none(self):
        data = {
            "media": {"code": "DV18", "name": "Digital Video for M18"},
            "usageLevel": {"code": "001", "name": "Junior Picture Adult Lending"},
            "location": {"code": "AMKPL", "name": "Ang Mo Kio Public Library"},
            "transactionStatus": {"code": "I", "name": "In Transit"},
            "volumeName": None,
            "suffix": None,
            "donor": None,
            "price": None,
        }

        item = Item.from_dict(data)

        # Test required fields
        assert item.media.code == "DV18"
        assert item.media.name == "Digital Video for M18"
        assert item.usage_level.code == "001"
        assert item.usage_level.name == "Junior Picture Adult Lending"
        assert item.location.code == "AMKPL"
        assert item.location.name == "Ang Mo Kio Public Library"
        assert item.transaction_status.code == "I"
        assert item.transaction_status.name == "In Transit"

        # Test fields with None values
        assert item.volume_name is None
        assert item.suffix is None
        assert item.donor is None
        assert item.price is None

        # Test remaining fields are UNSET
        assert item.course_code is UNSET
        assert item.status is UNSET
