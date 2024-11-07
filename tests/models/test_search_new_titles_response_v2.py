from nlb_catalogue_client.models.bib_format import BibFormat
from nlb_catalogue_client.models.new_arrival_title import NewArrivalTitle
from nlb_catalogue_client.models.search_new_titles_response_v2 import SearchNewTitlesResponseV2
from nlb_catalogue_client.types import UNSET


class TestSearchNewTitlesResponseV2:
    def setup_method(self):
        """Setup common test objects"""
        self.format_ = BibFormat(code="BK", name="BOOKS")
        self.new_arrival_title = NewArrivalTitle(
            format_=self.format_,
            brn=99999999,
            digital_id="overdrive123",
            other_titles=["Alternative Title 1"],
            native_other_titles=["其他标题 1"],
            variant_titles=["Variant 1"],
            native_variant_titles=["变体 1"],
            other_authors=["Jane Smith"],
            native_other_authors=["简·史密斯"],
            isbns=["9709999999"],
            issns=["9999-9999"],
            edition=["First Edition"],
            native_edition=["第一版"],
            publisher=["Sample Publisher"],
            native_publisher=["示例出版社"],
            publish_date="2023",
            subjects=["Fiction"],
            physical_description=["300 pages"],
            native_physical_description=["300页"],
            summary=["A story"],
            native_summary=["故事"],
            contents=["Chapter 1"],
            native_contents=["第一章"],
            thesis=["PhD Thesis"],
            native_thesis=["博士论文"],
            notes=["Special Edition"],
            native_notes=["特别版"],
            allow_reservation=True,
            is_restricted=False,
            active_reservations_count=3,
            audience=["General", "Adult"],
            audience_imda=["NC16", "PG"],
            language=["English", "Chinese"],
            serial=False,
            volume_note=["Volume 1"],
            native_volume_note=["第一卷"],
            frequency=["Monthly"],
            native_frequency=["每月"],
            credits_=["Editor: John"],
            native_credits=["编辑：约翰"],
            performers=["Actor: Jane"],
            native_performers=["演员：简"],
            availability=True,
            source="Library",
            volumes=["2023 issue 1"],
            title="Sample Book",
            native_title="样本书",
            series_title=["Series 1"],
            native_series_title=["系列 1"],
            author="John Doe",
            native_author="约翰·多伊",
        )

    def test_basic_initialization(self):
        """Test initialization with all fields"""
        response = SearchNewTitlesResponseV2(
            total_records=100,
            count=1,
            has_more_records=True,
            next_records_offset=10,
            titles=[self.new_arrival_title],
        )

        assert response.total_records == 100
        assert response.count == 1
        assert response.has_more_records is True
        assert response.next_records_offset == 10
        assert response.titles == [self.new_arrival_title]

    def test_initialization_with_unset(self):
        """Test initialization with UNSET values"""
        response = SearchNewTitlesResponseV2()

        assert response.total_records is UNSET
        assert response.count is UNSET
        assert response.has_more_records is False
        assert response.next_records_offset is UNSET
        assert response.titles is UNSET

    def test_to_dict_full(self):
        """Test converting to dictionary with all fields"""
        response = SearchNewTitlesResponseV2(
            total_records=100,
            count=1,
            has_more_records=True,
            next_records_offset=10,
            titles=[self.new_arrival_title],
        )

        expected = {
            "totalRecords": 100,
            "count": 1,
            "hasMoreRecords": True,
            "nextRecordsOffset": 10,
            "titles": [
                {
                    "format": {"code": "BK", "name": "BOOKS"},
                    "brn": 99999999,
                    "digitalId": "overdrive123",
                    "otherTitles": ["Alternative Title 1"],
                    "nativeOtherTitles": ["其他标题 1"],
                    "variantTitles": ["Variant 1"],
                    "nativeVariantTitles": ["变体 1"],
                    "otherAuthors": ["Jane Smith"],
                    "nativeOtherAuthors": ["简·史密斯"],
                    "isbns": ["9709999999"],
                    "issns": ["9999-9999"],
                    "edition": ["First Edition"],
                    "nativeEdition": ["第一版"],
                    "publisher": ["Sample Publisher"],
                    "nativePublisher": ["示例出版社"],
                    "publishDate": "2023",
                    "subjects": ["Fiction"],
                    "physicalDescription": ["300 pages"],
                    "nativePhysicalDescription": ["300页"],
                    "summary": ["A story"],
                    "nativeSummary": ["故事"],
                    "contents": ["Chapter 1"],
                    "nativeContents": ["第一章"],
                    "thesis": ["PhD Thesis"],
                    "nativeThesis": ["博士论文"],
                    "notes": ["Special Edition"],
                    "nativeNotes": ["特别版"],
                    "allowReservation": True,
                    "isRestricted": False,
                    "activeReservationsCount": 3,
                    "audience": ["General", "Adult"],
                    "audienceImda": ["NC16", "PG"],
                    "language": ["English", "Chinese"],
                    "serial": False,
                    "volumeNote": ["Volume 1"],
                    "nativeVolumeNote": ["第一卷"],
                    "frequency": ["Monthly"],
                    "nativeFrequency": ["每月"],
                    "credits": ["Editor: John"],
                    "nativeCredits": ["编辑：约翰"],
                    "performers": ["Actor: Jane"],
                    "nativePerformers": ["演员：简"],
                    "availability": True,
                    "source": "Library",
                    "volumes": ["2023 issue 1"],
                    "title": "Sample Book",
                    "nativeTitle": "样本书",
                    "seriesTitle": ["Series 1"],
                    "nativeSeriesTitle": ["系列 1"],
                    "author": "John Doe",
                    "nativeAuthor": "约翰·多伊",
                }
            ],
        }

        assert response.to_dict() == expected

    def test_from_dict_full(self):
        """Test creating object from dictionary with all fields"""
        data = {
            "totalRecords": 100,
            "count": 1,
            "hasMoreRecords": True,
            "nextRecordsOffset": 10,
            "titles": [
                {
                    "format": {"code": "BK", "name": "BOOKS"},
                    "brn": 99999999,
                    "digitalId": "overdrive123",
                    "otherTitles": ["Alternative Title 1"],
                    "nativeOtherTitles": ["其他标题 1"],
                    "variantTitles": ["Variant 1"],
                    "nativeVariantTitles": ["变体 1"],
                    "otherAuthors": ["Jane Smith"],
                    "nativeOtherAuthors": ["简·史密斯"],
                    "isbns": ["9709999999"],
                    "issns": ["9999-9999"],
                    "edition": ["First Edition"],
                    "nativeEdition": ["第一版"],
                    "publisher": ["Sample Publisher"],
                    "nativePublisher": ["示例出版社"],
                    "publishDate": "2023",
                    "subjects": ["Fiction"],
                    "physicalDescription": ["300 pages"],
                    "nativePhysicalDescription": ["300页"],
                    "summary": ["A story"],
                    "nativeSummary": ["故事"],
                    "contents": ["Chapter 1"],
                    "nativeContents": ["第一章"],
                    "thesis": ["PhD Thesis"],
                    "nativeThesis": ["博士论文"],
                    "notes": ["Special Edition"],
                    "nativeNotes": ["特别版"],
                    "allowReservation": True,
                    "isRestricted": False,
                    "activeReservationsCount": 3,
                    "audience": ["General", "Adult"],
                    "audienceImda": ["NC16", "PG"],
                    "language": ["English", "Chinese"],
                    "serial": False,
                    "volumeNote": ["Volume 1"],
                    "nativeVolumeNote": ["第一卷"],
                    "frequency": ["Monthly"],
                    "nativeFrequency": ["每月"],
                    "credits": ["Editor: John"],
                    "nativeCredits": ["编辑：约翰"],
                    "performers": ["Actor: Jane"],
                    "nativePerformers": ["演员：简"],
                    "availability": True,
                    "source": "Library",
                    "volumes": ["2023 issue 1"],
                    "title": "Sample Book",
                    "nativeTitle": "样本书",
                    "seriesTitle": ["Series 1"],
                    "nativeSeriesTitle": ["系列 1"],
                    "author": "John Doe",
                    "nativeAuthor": "约翰·多伊",
                }
            ],
        }

        response = SearchNewTitlesResponseV2.from_dict(data)

        assert response.total_records == 100
        assert response.count == 1
        assert response.has_more_records is True
        assert response.next_records_offset == 10
        assert response.titles
        assert len(response.titles) == 1
        title = response.titles[0]
        assert isinstance(title, NewArrivalTitle)
        assert title.format_.code == "BK"
        assert title.format_.name == "BOOKS"
        assert title.brn == 99999999

    def test_from_dict_with_none(self):
        """Test creating object from dictionary with None values"""
        data = {
            "totalRecords": None,
            "count": None,
            "hasMoreRecords": None,
            "nextRecordsOffset": None,
            "titles": None,
        }

        response = SearchNewTitlesResponseV2.from_dict(data)

        assert response.total_records is None
        assert response.count is None
        assert response.has_more_records is None
        assert response.next_records_offset is None
        assert response.titles == []
