from nlb_catalogue_client.models.bib_format import BibFormat
from nlb_catalogue_client.models.facet import Facet
from nlb_catalogue_client.models.facet_data import FacetData
from nlb_catalogue_client.models.search_titles_response_v2 import SearchTitlesResponseV2
from nlb_catalogue_client.models.title_record import TitleRecord
from nlb_catalogue_client.models.title_summary import TitleSummary
from nlb_catalogue_client.types import UNSET


class TestSearchTitlesResponseV2:
    def setup_method(self):
        """Setup common test objects"""
        self.format_ = BibFormat(code="BK", name="BOOKS")

        self.title_record = TitleRecord(
            format_=self.format_,
        )
        self.facet_data = FacetData(id="audioBook", data="Audio Book", count=17)
        self.title_summary = TitleSummary(
            title="Sample Book",
            native_title="样本书",
            series_title=["Series 1"],
            native_series_title=["系列 1"],
            author="John Doe",
            native_author="约翰·多伊",
            cover_url=UNSET,
            records=[self.title_record],
        )
        self.facet = Facet(id="audioBook", name="Audio Book", values=[self.facet_data])

    def test_basic_initialization(self):
        """Test initialization with all fields"""
        response = SearchTitlesResponseV2(
            total_records=100,
            count=1,
            next_records_offset=10,
            has_more_records=True,
            titles=[self.title_summary],
            facets=[self.facet],
        )

        assert response.total_records == 100
        assert response.count == 1
        assert response.next_records_offset == 10
        assert response.has_more_records is True
        assert response.titles == [self.title_summary]
        assert response.facets == [self.facet]

    def test_initialization_with_unset(self):
        """Test initialization with UNSET values"""
        response = SearchTitlesResponseV2()

        assert response.total_records is UNSET
        assert response.count is UNSET
        assert response.next_records_offset is UNSET
        assert response.has_more_records is False
        assert response.titles == UNSET
        assert response.facets == UNSET

    def test_to_dict_full(self):
        """Test converting to dictionary with all fields"""
        response = SearchTitlesResponseV2(
            total_records=100,
            count=1,
            next_records_offset=10,
            has_more_records=True,
            titles=[self.title_summary],
            facets=[self.facet],
        )

        expected = {
            "totalRecords": 100,
            "count": 1,
            "nextRecordsOffset": 10,
            "hasMoreRecords": True,
            "titles": [self.title_summary.to_dict()],
            "facets": [self.facet.to_dict()],
        }

        assert response.to_dict() == expected

    def test_to_dict_empty(self):
        """Test converting to dictionary with no fields set"""
        response = SearchTitlesResponseV2()

        assert response.to_dict() == {"hasMoreRecords": False}

    def test_from_dict(self):
        """Test creating object from dictionary"""
        data = {
            "totalRecords": 100,
            "count": 1,
            "nextRecordsOffset": 10,
            "hasMoreRecords": True,
            "titles": [self.title_summary.to_dict()],
            "facets": [self.facet.to_dict()],
        }
        response = SearchTitlesResponseV2.from_dict(data)
        assert response.total_records == 100
        assert response.count == 1
        assert response.next_records_offset == 10
        assert response.has_more_records is True
        assert response.titles == [self.title_summary]
        assert response.facets == [self.facet]

    def test_from_dict_with_unset(self):
        """Test creating object from dictionary with unset fields"""
        data = {}
        response = SearchTitlesResponseV2.from_dict(data)
        assert response.has_more_records is UNSET
        assert response.total_records is UNSET
        assert response.count is UNSET
        assert response.next_records_offset is UNSET
        assert response.titles == []
        assert response.facets == []
